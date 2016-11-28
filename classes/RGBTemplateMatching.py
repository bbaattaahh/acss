import cv2
import numpy as np


class RGBTemplateMatching:
    def __init__(self,
                 rgb_image,
                 rgb_template,
                 threshold,
                 cv2_method):

        self.rgb_image = rgb_image
        self.rgb_template = rgb_template
        self.threshold = threshold
        self.cv2_method = cv2_method


    def rgb_match(self):
        w, h, _ = self.template.shape

        resR = cv2.matchTemplate(self.rgb_image[:, :, 0], self.rgb_template[:, :, 0], cv2.TM_CCOEFF_NORMED)
        resG = cv2.matchTemplate(self.rgb_image[:, :, 1], self.rgb_template[:, :, 1], cv2.TM_CCOEFF_NORMED)
        resB = cv2.matchTemplate(self.rgb_image[:, :, 2], self.rgb_template[:, :, 2], cv2.TM_CCOEFF_NORMED)

        resRGB = resR + resG + resB

        loc = np.where(resRGB >= self.threshold)


    @staticmethod
    def get_individual_rectangles(locations, width):

        top_left_corner = []

        y_coordinate = np.mean(locations[0])

        sorted_x_coordinates = np.sort(locations[1])
        numeric_derivation_of_sorted_x_coordinates = np.diff(sorted_x_coordinates)
        fractures = np.where( numeric_derivation_of_sorted_x_coordinates >= width)

        for fracture in fractures:



        return None