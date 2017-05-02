import cv2
import numpy as np
import math

from Rectangle import Rectangle
from RectangleResizer import RectangleResizer
from DetectionToOneAsparagusAnalysis import DetectionToOneAsparagusAnalysis
from SnipFromImage import SnipFromImage
from ImageResizer import ImageResizer
from PositionConverter import PositionConverter


class AsparagusesDetector2(object):
    def __init__(self,
                 global_threshold,
                 high_width_ratio,
                 minimum_area,
                 detection_resolution):

        self.global_threshold = global_threshold
        self.high_width_ratio = high_width_ratio
        self.minimum_area = minimum_area
        self.detection_resolution = detection_resolution

    def data_to_analysis_one_asparagus_images(self, image):
        image_detection_on = self.image_detection_on(image)
        candidate_contours = self.get_candidate_contours(image_detection_on)
        asparagus_contours_bounding_rectangles = self.asparagus_contours_bounding_rectangles(candidate_contours)

        to_asparagus_analysis = []

        for opencv_rectangle in asparagus_contours_bounding_rectangles:

            rectangle_on_original_image = self.rectangle_on_original_rotated_image(image.shape[:2],
                                                                                   image_detection_on,
                                                                                   opencv_rectangle)

            original_rotated_image = self.rotate_about_center(image,
                                                              angle=opencv_rectangle[2])

            # scale_back_x, scale_back_y = PositionConverter(
            #     original_position=[candidate.top_left_x, candidate.top_left_y],
            #     original_resolution=image_detection_on.shape[0:2],
            #     target_resolution=image.shape[0:2]).target_position
            #
            # scale_back_w, scale_back_h = PositionConverter(original_position=[candidate.width, candidate.high],
            #                                                original_resolution=image_detection_on.shape[0:2],
            #                                                target_resolution=image.shape[0:2]).target_position
            #
            # image_one_asparagus = SnipFromImage(image=original_rotated_image,
            #                                     x=scale_back_x,
            #                                     y=scale_back_y,
            #                                     w=scale_back_w,
            #                                     h=scale_back_h).snipped_image
            #
            # original_top_left_corner = self.calculate_original_coordinate_before_rotation(
            #     image=image,
            #     angle=candidate.angle,
            #     vertex=[scale_back_x, scale_back_y])
            #
            # rectangle_on_original_image = Rectangle(top_left_x=original_top_left_corner[0],
            #                                         top_left_y=original_top_left_corner[1],
            #                                         width=scale_back_w,
            #                                         high=scale_back_h,
            #                                         angle=candidate.angle)
            #
            # actual_detection_to_one_asparagus_analysis = DetectionToOneAsparagusAnalysis(
            #     image=image_one_asparagus,
            #     rectangle_on_original_image=rectangle_on_original_image)
            #
            # to_asparagus_analysis.append(actual_detection_to_one_asparagus_analysis)

        return to_asparagus_analysis

    def image_detection_on(self, image):
        gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        rescaled_image = ImageResizer(gray_image, target_resolution=self.detection_resolution).resized_snipped_image
        return rescaled_image

    def get_candidate_contours(self, image_detection_on):
        _, thresholded_image = cv2.threshold(image_detection_on, self.global_threshold, 255, cv2.THRESH_BINARY)
        kernel = np.ones((5, 5), np.uint8)
        closed_thresholded_image = cv2.morphologyEx(thresholded_image, cv2.MORPH_CLOSE, kernel)
        _, contours, _ = cv2.findContours(closed_thresholded_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        return contours

    def asparagus_contours_bounding_rectangles(self, candidate_contours):
        asparagus_contours = []

        for cnt in candidate_contours:
            x = cv2.contourArea(cnt)
            if cv2.contourArea(cnt) < self.minimum_area:
                continue

            rect = cv2.minAreaRect(cnt)

            if abs(rect[2]) <= 45 and rect[1][1] / rect[1][0] < self.high_width_ratio:
                continue

            if abs(rect[2]) >= 45 and rect[1][0] / rect[1][1] < self.high_width_ratio:
                continue

            asparagus_contours.append(rect)

        return asparagus_contours

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

    def rectangle_on_original_image(self, image_shape, image_detection_on, opencv_rectangle):

        top_left_x = opencv_rectangle[0][0] - opencv_rectangle[1][1]/2
        top_left_y = opencv_rectangle[0][1] - opencv_rectangle[1][0]/2

        rectangle = Rectangle(top_left_x=top_left_x,
                              top_left_y=top_left_y,
                              width=opencv_rectangle[1][1],
                              high=opencv_rectangle[1][0],
                              angle=opencv_rectangle[2])

        rectangle_resizer = RectangleResizer(original_resolution=image_detection_on.shape[:2],
                                             target_resolution=image_shape)

        rectangle_on_original_image = rectangle_resizer.resize(rectangle)

        return rectangle_on_original_image




    # def rectangle_on_original_rotated_image(self, image_shape, image_detection_on, opencv_rectangle):
    #     rectangle_center_after_rotation = self.calculate_original_coordinate_before_rotation(
    #                                                             image=image_detection_on,
    #                                                             angle=opencv_rectangle[2],
    #                                                             vertex=opencv_rectangle[0])
    #
    #     top_left_x = int(rectangle_center_after_rotation[0] - opencv_rectangle[1][0]/2)
    #     top_left_y = int(rectangle_center_after_rotation[1] - opencv_rectangle[1][1]/2)
    #
    #     rectangle_back_rotated_image = Rectangle(top_left_x=top_left_x,
    #                                              top_left_y=top_left_y,
    #                                              width=int(opencv_rectangle[1][0]),
    #                                              high=int(opencv_rectangle[1][1]))
    #
    #     rectangle_resizer = RectangleResizer(original_resolution=image_detection_on.shape[:2],
    #                                          target_resolution=image_shape)
    #
    #
    #     rectangle_on_back_rotated_original_image = rectangle_resizer.resize(rectangle_back_rotated_image)
    #
    #     return rectangle_on_back_rotated_original_image





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

