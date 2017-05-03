import numpy as np
import cv2
import math


class SnipRectangleFromImage(object):

    def __init__(self,
                 image,
                 rectangle):

        self.image = image
        self.rectangle = rectangle

    @property
    def snipped_image(self):

        new_top_left_corner = self.calculate_new_coordinate_after_rotation(
            image=self.image,
            angle=self.rectangle.angle,
            vertex=self.rectangle.vertices[0]
        )

        rotated_image = self.rotate_about_center(self.image, -1*self.rectangle.angle)

        cv2.imwrite("temp.png", rotated_image)

        x1 = int(new_top_left_corner[0])
        x2 = int(new_top_left_corner[0] + self.rectangle.width)
        y1 = int(new_top_left_corner[1])
        y2 = int(new_top_left_corner[1] + self.rectangle.high)

        # gray image
        if len(self.image.shape) == 2:
            return rotated_image[y1: y2, x1: x2]

        # rgb image
        if len(self.image.shape) == 3:
            return rotated_image[y1: y2, x1: x2, :]

    @staticmethod
    def calculate_original_coordinate_before_rotation(image, angle, vertex):
        point_numpy = np.array([[vertex[0]], [vertex[1]]])

        w_original = image.shape[1]
        h_original = image.shape[0]

        # now calculate new image width and height
        radian_angle = np.deg2rad(angle)  # angle in radians
        w_rotated = abs(np.sin(radian_angle) * h_original) + abs(np.cos(radian_angle) * w_original)
        h_rotated = abs(np.cos(radian_angle) * h_original) + abs(np.sin(radian_angle) * w_original)

        # From top left corner to central of image
        central_vector = np.array([[-w_rotated / 2], [-h_rotated / 2]])

        point_relative_to_central = point_numpy + central_vector

        # Rotation back
        theta = np.deg2rad(angle)
        rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)],
                                    [np.sin(theta), np.cos(theta)]])
        rotated_point_relative_to_central = np.dot(rotation_matrix, point_relative_to_central)

        # Central to top left corner
        top_left_central_point = rotated_point_relative_to_central - central_vector

        # Compensation with picture growth
        w_growth_on_one_side = (w_rotated - w_original) / 2
        h_growth_on_one_side = (h_rotated - h_original) / 2
        compensation_vector = np.array([[w_growth_on_one_side], [h_growth_on_one_side]])

        original_point = top_left_central_point - compensation_vector
        original_point_list = original_point.tolist()
        original_point_list_single_level = original_point_list[0] + original_point_list[1]
        return original_point_list_single_level

    @staticmethod
    def calculate_new_coordinate_after_rotation(image, angle, vertex):
        point_numpy = np.array([[vertex[0]], [vertex[1]]])

        w_original = image.shape[1]
        h_original = image.shape[0]

        # now calculate new image width and height
        radian_angle = np.deg2rad(angle)  # angle in radians
        w_rotated = abs(np.sin(radian_angle) * h_original) + abs(np.cos(radian_angle) * w_original)
        h_rotated = abs(np.cos(radian_angle) * h_original) + abs(np.sin(radian_angle) * w_original)

        # From top left corner to central of image
        central_vector = np.array([[-w_original / 2], [-h_original / 2]])

        # Compensation with picture growth
        w_growth_on_one_side = (w_rotated - w_original) / 2
        h_growth_on_one_side = (h_rotated - h_original) / 2
        compensation_vector = np.array([[w_growth_on_one_side], [h_growth_on_one_side]])

        point_relative_to_central = point_numpy + central_vector

        # Rotation back
        theta = np.deg2rad(angle)
        rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)],
                                    [np.sin(theta), np.cos(theta)]])
        rotated_point = np.dot(rotation_matrix, point_relative_to_central)

        x = rotated_point - central_vector + compensation_vector

        original_point_list = x.tolist()
        original_point_list_single_level = original_point_list[0] + original_point_list[1]
        return original_point_list_single_level



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

