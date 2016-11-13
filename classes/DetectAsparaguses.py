import cv2
import numpy as np
import math

from Rectangle import Rectangle
from IsRectangleOnOriginalImage import IsRectangleOnOriginalImage
from ChooseFinalCandidates import ChooseFinalCandidates
from DetectionToOneAsparagusAnalysis import DetectionToOneAsparagusAnalysis


class DetectAsparaguses(object):

    def __init__(self,
                 image,
                 cascade_file,
                 detection_scale=0.25,
                 swing_angle=45):

        self.image = image
        self.cascade_file = cascade_file
        self.detection_scale = detection_scale
        self.swing_angle = swing_angle
        self.image_detection_on = self.image_detection_on()
        self.asparagus_candidates = self.get_asparagus_candidates()
        self.data_to_analysis_one_asparagus_images = self.data_to_analysis_one_asparagus_images()

    def data_to_analysis_one_asparagus_images(self):
        to_asparagus_analysis = []
        for candidate in self.asparagus_candidates:
            original_rotated_image = self.rotate_about_center(self.image,
                                                              angle=candidate.angle)

            scale_back_x = candidate.top_left_x / self.detection_scale
            scale_back_y = candidate.top_left_y / self.detection_scale
            scale_back_w = candidate.width / self.detection_scale
            scale_back_h = candidate.high / self.detection_scale

            image_one_asparagus = self.snip_from_rgb_image(original_rotated_image,
                                                           scale_back_x,
                                                           scale_back_y,
                                                           scale_back_w,
                                                           scale_back_h)

            original_top_left_corner = self.calculate_original_coordinate_before_rotation(
                                                                        image=self.image,
                                                                        angle=candidate.angle,
                                                                        vertex=[scale_back_x, scale_back_y])

            rectangle_on_original_image = Rectangle(top_left_x=original_top_left_corner[0],
                                                    top_left_y=original_top_left_corner[1],
                                                    width=scale_back_w,
                                                    high=scale_back_h,
                                                    angle=candidate.angle)

            actual_detection_to_one_asparagus_analysis = DetectionToOneAsparagusAnalysis(
                                                            image=image_one_asparagus,
                                                            rectangle_on_original_image=rectangle_on_original_image)

            to_asparagus_analysis.append(actual_detection_to_one_asparagus_analysis)

        return to_asparagus_analysis

    def image_detection_on(self):
        grey_image = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
        rescaled_image = cv2.resize(grey_image,
                                    None,
                                    fx=self.detection_scale,
                                    fy=self.detection_scale,
                                    interpolation=cv2.INTER_CUBIC)
        return rescaled_image

    def get_asparagus_candidates(self):
        detections = []

        for angle in range(-self.swing_angle, self.swing_angle+1):
            rotated_image_detection_on = self.rotate_about_center(self.image_detection_on, angle)
            asparagus_cascade = cv2.CascadeClassifier(self.cascade_file)
            actual_asparagus_candidates = asparagus_cascade.detectMultiScale(rotated_image_detection_on, 4, 31)
            if len(actual_asparagus_candidates) != 0:
                for actual_asparagus_candidate in actual_asparagus_candidates:
                    rectangle = Rectangle(top_left_x=actual_asparagus_candidate[0].tolist(),
                                          top_left_y=actual_asparagus_candidate[1].tolist(),
                                          width=actual_asparagus_candidate[2].tolist(),
                                          high=actual_asparagus_candidate[3].tolist(),
                                          angle=0)
                    is_rectangle_on_original_image = IsRectangleOnOriginalImage(self.image_detection_on,
                                                                                rectangle_on_rotated_image=rectangle,
                                                                                angle=angle)

                    if is_rectangle_on_original_image.is_it:
                        actual_asparagus_candidate = Rectangle(
                                                top_left_x=actual_asparagus_candidate[0].tolist(),
                                                top_left_y=actual_asparagus_candidate[1].tolist(),
                                                width=actual_asparagus_candidate[2].tolist(),
                                                high=actual_asparagus_candidate[3].tolist(),
                                                angle=angle)

                        detections.append(actual_asparagus_candidate)

        choose_final_candidates = ChooseFinalCandidates(detections, 5)
        final_candidates = choose_final_candidates.final_candidates

        return final_candidates

    @staticmethod
    def rotate_about_center(image, angle):
        w = image.shape[1]
        h = image.shape[0]
        # angle in radians
        rangle = np.deg2rad(angle)
        # now calculate new image width and height
        nw = abs(np.sin(rangle) * h) + abs(np.cos(rangle) * w)
        nh = abs(np.cos(rangle) * h) + abs(np.sin(rangle) * w)
        # ask OpenCV for the rotation matrix
        rot_mat = cv2.getRotationMatrix2D((nw * 0.5, nh * 0.5), angle, scale=1)
        # calculate the move from the old center to the new center combined
        # with the rotation
        rot_move = np.dot(rot_mat, np.array([(nw - w) * 0.5, (nh - h) * 0.5, 0]))
        # the move only affects the translation, so update the translation
        # part of the transform
        rot_mat[0, 2] += rot_move[0]
        rot_mat[1, 2] += rot_move[1]
        return cv2.warpAffine(image,
                              rot_mat,
                              (int(math.ceil(nw)), int(math.ceil(nh))),
                              flags=cv2.INTER_LANCZOS4)

    @staticmethod
    def snip_from_rgb_image(image, x, y, w, h):
        return image[y : y+h, x : x+w, :]

    @staticmethod
    def calculate_original_coordinate_before_rotation(image, angle, vertex):
        point_numpy = np.array([[vertex[0]], [vertex[1]]])

        w_original = image.shape[1]
        h_original = image.shape[0]

        # now calculate new image width and height
        rangle = np.deg2rad(angle)  # angle in radians
        w_rotated = abs(np.sin(rangle) * h_original) + abs(np.cos(rangle) * w_original)
        h_rotated = abs(np.cos(rangle) * h_original) + abs(np.sin(rangle) * w_original)


        # From top left coorner to centrum of image
        central_vector = np.array([[-w_rotated / 2], [-h_rotated / 2]])

        point_relative_to_centrum = point_numpy + central_vector

        # Rotation back
        theta = np.deg2rad(angle)
        rotMatrix = np.array([[np.cos(theta), -np.sin(theta)],
                              [np.sin(theta), np.cos(theta)]])
        rotated_point_relative_to_centrum = np.dot(rotMatrix, point_relative_to_centrum)

        # Centrum to top left coorner
        top_left_centrum_point = rotated_point_relative_to_centrum - central_vector

        # Compenyation with picture growth
        w_growth_on_one_side = (w_rotated - w_original) / 2
        h_growth_on_one_side = (h_rotated - h_original) / 2
        compensation_vector = np.array([[w_growth_on_one_side], [h_growth_on_one_side]])

        original_point = top_left_centrum_point - compensation_vector
        original_point_list = original_point.tolist()
        original_point_list_single_level = original_point_list[0] + original_point_list[1]

        return original_point_list_single_level
