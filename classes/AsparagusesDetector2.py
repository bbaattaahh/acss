import cv2
import numpy as np

from DetectionToOneAsparagusAnalysis import DetectionToOneAsparagusAnalysis
from ImageResizer import ImageResizer


class AsparagusesDetector2(object):
    def __init__(self,
                 global_threshold,
                 high_width_ratio,
                 minimum_area,
                 detection_resolution,
                 vertical_extension_factor,
                 horizontal_extension_factor):

        self.global_threshold = global_threshold
        self.high_width_ratio = high_width_ratio
        self.minimum_area = minimum_area
        self.detection_resolution = detection_resolution
        self.vertical_extension_factor = vertical_extension_factor
        self.horizontal_extension_factor = horizontal_extension_factor

    def data_to_analysis_one_asparagus_images(self, image):
        image_detection_on = self.image_detection_on(image)
        candidate_contours = self.get_candidate_contours(image_detection_on)
        asparagus_contours_bounding_rectangles = self.asparagus_contours_bounding_rectangles(candidate_contours)

        to_asparagus_analysis = []

        for opencv_rectangle in asparagus_contours_bounding_rectangles:

            opencv_rectangle_on_original_image = self.opencv_rectangle_on_original_image(
                                                        image_shape=image.shape,
                                                        image_detection_on_shape=image_detection_on.shape,
                                                        opencv_rectangle=opencv_rectangle)

            opencv_rectangle_on_original_image = self.orientation_correction(opencv_rectangle_on_original_image)

            opencv_rectangle_on_original_image = self.extend_opencv_rectangle(opencv_rectangle_on_original_image)


            if self.is_rectangle_vertically_on_image(image.shape[1], opencv_rectangle_on_original_image):

                snipped_asparagus = self.subimage(image, opencv_rectangle_on_original_image)

                actual_detection_to_one_asparagus_analysis = DetectionToOneAsparagusAnalysis(
                    image=snipped_asparagus,
                    opencv_rectangle_on_original_image=opencv_rectangle_on_original_image)

                to_asparagus_analysis.append(actual_detection_to_one_asparagus_analysis)

        return to_asparagus_analysis

    def image_detection_on(self, image):
        gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        rescaled_image = ImageResizer(gray_image, target_resolution=self.detection_resolution).resized_snipped_image
        return rescaled_image

    def get_candidate_contours(self, image_detection_on):
        _, thresholded_image = cv2.threshold(image_detection_on, self.global_threshold, 255, cv2.THRESH_BINARY)
        kernel = np.ones((5, 5), np.uint8)
        opened_thresholded_image = cv2.morphologyEx(thresholded_image, cv2.MORPH_OPEN, kernel)
        _, contours, _ = cv2.findContours(opened_thresholded_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
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
    def opencv_rectangle_on_original_image(image_shape, image_detection_on_shape, opencv_rectangle):

        high_scale = image_shape[0] / image_detection_on_shape[0]
        width_scale = image_shape[1] / image_detection_on_shape[1]

        back_scaled_opencv_rectangle = ((opencv_rectangle[0][0]*high_scale, opencv_rectangle[0][1]*width_scale),
                                        (opencv_rectangle[1][0]*high_scale, opencv_rectangle[1][1]*width_scale),
                                        opencv_rectangle[2])

        return back_scaled_opencv_rectangle

    @staticmethod
    def subimage(image, opencv_rectangle):
        # mapping
        theta = opencv_rectangle[2]
        center = opencv_rectangle[0]
        width = opencv_rectangle[1][0]
        height = opencv_rectangle[1][1]

        theta *= 3.14159 / 180  # convert to rad

        v_x = (np.cos(theta), np.sin(theta))
        v_y = (-np.sin(theta), np.cos(theta))
        s_x = center[0] - v_x[0] * (width / 2) - v_y[0] * (height / 2)
        s_y = center[1] - v_x[1] * (width / 2) - v_y[1] * (height / 2)

        mapping = np.array([[v_x[0], v_y[0], s_x],
                            [v_x[1], v_y[1], s_y]])

        return cv2.warpAffine(image, mapping, (int(width), int(height)), flags=cv2.WARP_INVERSE_MAP,
                              borderMode=cv2.BORDER_REPLICATE)

    def extend_opencv_rectangle(self, opencv_rectangle):

        vertical_extension_factor = 1 + self.vertical_extension_factor
        horizontal_extension_factor = 1 + self.horizontal_extension_factor

        extended_opencv_rectangle = \
            ((opencv_rectangle[0][0], opencv_rectangle[0][1]),
             (opencv_rectangle[1][0]*horizontal_extension_factor, opencv_rectangle[1][1]*vertical_extension_factor),
             opencv_rectangle[2])
        return extended_opencv_rectangle

    @staticmethod
    def orientation_correction(opencv_rectangle):
        if opencv_rectangle[1][0] > opencv_rectangle[1][1]:
            rotated_rectangle = (opencv_rectangle[0],
                                 (opencv_rectangle[1][1], opencv_rectangle[1][0]),
                                 opencv_rectangle[2] + 90)
            return rotated_rectangle

        return opencv_rectangle



    @staticmethod
    def is_rectangle_vertically_on_image(image_width, opencv_rectangle):
        box = cv2.boxPoints(opencv_rectangle)
        box = np.int0(box)
        x_coordinates = box[:, 0]

        if min(x_coordinates) <= 0:
            return False

        if max(x_coordinates) >= image_width:
            return False

        return True
