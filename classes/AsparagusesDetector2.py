import cv2
import numpy as np
import math

from Rectangle import Rectangle
from RectangleResizer import RectangleResizer
from DetectionToOneAsparagusAnalysis import DetectionToOneAsparagusAnalysis
from SnipFromImage import SnipFromImage
from ImageResizer import ImageResizer
from PositionConverter import PositionConverter
from SnipRectangleFromImage import SnipRectangleFromImage


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

            snipped_asparagus_image = SnipRectangleFromImage(image=image,
                                                             rectangle=rectangle_on_original_image)

            actual_detection_to_one_asparagus_analysis = DetectionToOneAsparagusAnalysis(
                image=snipped_asparagus_image,
                rectangle_on_original_image=rectangle_on_original_image)

            to_asparagus_analysis.append(actual_detection_to_one_asparagus_analysis)

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
    def rectangle_on_original_image(image_shape, image_detection_on, opencv_rectangle):

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
