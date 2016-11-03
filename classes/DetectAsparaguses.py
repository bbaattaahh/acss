import cv2
import numpy as np
import math

import Rectangle

class DetectAsparaguses(object):

    def __init__(self,
                 image,
                 cascade_classifier_file,
                 detection_scale=0.25,
                 swing_angle=45):
        self.image = image
        self.cascade_classifier_file = cascade_classifier_file
        self.detection_scale=detection_scale
        self.swing_angle=swing_angle

    def image_detection_on(self):
        grey_image = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
        rescaled_image = cv2.resize(grey_image,
                               None,
                               fx=self.detection_scale,
                               fy=self.detection_scale,
                               interpolation=cv2.INTER_CUBIC)
        return rescaled_image

    def rectangles_contain_asparaguses(self):
        detections = dict()

        for angle in range(-self.swing_angle, self.swing_angle):
            rotated_image_detection_on = self.rotate_about_center(self.image_detection_on(), angle)
            asparagus_cascade = cv2.CascadeClassifier(self.cascade_classifier_file)
            detected_asparaguses = asparagus_cascade.detectMultiScale(rotated_image_detection_on, 4, 31)

            for (x, y, w, h) in detected_asparaguses:
                act_rectangle = Rectangle(x, y, w, h)

                if self.is_rectangle_on_orignal_image(rectangle=act_rectangle,
                                                      original_image=self.image_detection_on(),
                                                      rotated_image=rotated_image_detection_on,
                                                      angle=angle):
                    detected_rectangles_in_this_angle = detections.get(angle, [])
                    detections[angle] = detected_rectangles_in_this_angle.append([x, y, w, h])

        return detections

    def rotate_about_center(src, angle, scale=1.):
        w = src.shape[1]
        h = src.shape[0]
        rangle = np.deg2rad(angle)  # angle in radians
        # now calculate new image width and height
        nw = (abs(np.sin(rangle) * h) + abs(np.cos(rangle) * w)) * scale
        nh = (abs(np.cos(rangle) * h) + abs(np.sin(rangle) * w)) * scale
        # ask OpenCV for the rotation matrix
        rot_mat = cv2.getRotationMatrix2D((nw * 0.5, nh * 0.5), angle, scale)
        # calculate the move from the old center to the new center combined
        # with the rotation
        rot_move = np.dot(rot_mat, np.array([(nw - w) * 0.5, (nh - h) * 0.5, 0]))
        # the move only affects the translation, so update the translation
        # part of the transform
        rot_mat[0, 2] += rot_move[0]
        rot_mat[1, 2] += rot_move[1]
        return cv2.warpAffine(src, rot_mat, (int(math.ceil(nw)), int(math.ceil(nh))), flags=cv2.INTER_LANCZOS4)


    def is_rectangle_on_orignal_image(self, original_image, rotated_image, rectangle, angle):
        xy_limits = self.image_borders(original_image)

        for vertex in rectangle.vertices:
            original_vertex = self.calulate_original_coordinat_before_rotation(original_image,
                                                                               rotated_image,
                                                                               point=vertex,
                                                                               angle=angle)

            if not (xy_limits["x"][0] <= original_vertex[0] and original_vertex[0] <= xy_limits["x"][1]):
                return False

            if not (xy_limits["y"][0] <= original_vertex[1] and original_vertex[1] <= xy_limits["y"][1]):
                return False

        return True


    def calulate_original_coordinat_before_rotation(original_image, rotated_image, point, angle):
        point_numpy = np.array([[point[0]],[point[1]]])

        w_original = original_image.shape[1]
        h_original = original_image.shape[0]

        w_rotated = rotated_image.shape[1]
        h_rotated = rotated_image.shape[0]

        # From top left coorner to centrum of image
        centrum_vector = np.array([[-w_rotated / 2], [-h_rotated / 2]])

        point_relative_to_centrum = point_numpy + centrum_vector

        # Rotation back
        theta = np.deg2rad(angle)
        rotMatrix = np.array([[np.cos(theta), -np.sin(theta)],
                              [np.sin(theta), np.cos(theta)]])
        rotated_point_relative_to_centrum = np.dot(rotMatrix, point_relative_to_centrum)

        # Centrum to top left coorner
        top_left_centrum_point = rotated_point_relative_to_centrum - centrum_vector

        # Compenyation with picture growth
        w_growth_on_one_side = (w_rotated - w_original) / 2
        h_growth_on_one_side = (h_rotated - h_original) / 2
        compensation_vector = np.array([[w_growth_on_one_side], [h_growth_on_one_side]])

        original_point = top_left_centrum_point - compensation_vector
        original_point_list = original_point.tolist()
        original_point_list_single_level = [original_point_list[0][0], original_point_list[1][0]]

        return (original_point_list_single_level)


    def image_borders(image):
        x_min = 0
        y_min = 0

        x_max = image.shape[1]
        y_max = image.shape[0]

        return {"x": [x_min, x_max], "y": [y_min, y_max]}
