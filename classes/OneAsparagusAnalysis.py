import cv2
import numpy as np


class OneAsparagusAnalysis:
    def __init__(self,
                 detection_to_one_asparagus_analysis):

        self.detection_to_one_asparagus_analysis = detection_to_one_asparagus_analysis
        self.asparagus_contour = self.get_asparagus_contour()

    def get_asparagus_contour(self):

        gray_image = cv2.cvtColor(self.detection_to_one_asparagus_analysis.image, cv2.COLOR_BGR2GRAY)

        ret, th = cv2.threshold(gray_image,
                                0,
                                255,
                                cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        th_to_find_conours = th.copy()
        contours, hierarchy = cv2.findContours(th_to_find_conours, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        largest_contour = self.largest_contour(contours)
        x, y, w, h = cv2.boundingRect(largest_contour)
        asparagus_contour = self.snip_from_grey_image(th, x, y, w, h)

        kernel = np.ones((5, 5), np.uint8)

        opened_asparagus_contour = cv2.morphologyEx(asparagus_contour, cv2.MORPH_OPEN, kernel)

        return opened_asparagus_contour

    def asparagus_length(self):
        return self.asparagus_contour.shape[1]

    def asparagus_thickness(self):
        thicknesses = (self.asparagus_contour != 0).sum(0)
        thicknesses_sorted = np.sort(thicknesses)
        thicknesses_narrowed = thicknesses_sorted[0:int(len(thicknesses_sorted)*0.9)]
        thicknesses_max = max(thicknesses_narrowed)
        return thicknesses_max

    @staticmethod
    def largest_contour(contours):
        largest_contour = contours[0]

        for actual_contour in contours:
            if cv2.contourArea(actual_contour) > cv2.contourArea(largest_contour):
                largest_contour = actual_contour

        return largest_contour

    @staticmethod
    def snip_from_grey_image(image, x, y, w, h):
        return image[y : y+h, x : x+w]