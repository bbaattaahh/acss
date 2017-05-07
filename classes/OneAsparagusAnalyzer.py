import cv2
import numpy as np

from SnipFromImage import SnipFromImage
from Asparagus import Asparagus
from KeepNLargestAreaContours import KeepNLargestAreaContours


class OneAsparagusAnalyzer:
    def __init__(self,
                 asparagus_head_classifier):

        self.asparagus_head_classifier = asparagus_head_classifier

    def asparagus(self, one_asparagus_image):
        # Speed up one calculate asparagus contour
        #asparagus_contour = self.asparagus_contour(one_asparagus_image)

        asparagus = Asparagus(length=self.asparagus_length(one_asparagus_image),
                              thickness=self.asparagus_thickness(one_asparagus_image),
                              white_head=False,
                              no_head=False,
                              purple_head=False,
                              open_head=False,
                              piper=False)

        head_label = self.head_label(one_asparagus_image)
        if head_label == "white":
            asparagus.white_head = True
        if head_label == "no_head":
            asparagus.no_head = True
        if head_label == "purple":
            asparagus.purple_head = True
        if head_label == "open_head":
            asparagus.no_head = True

        return asparagus

    def head_label(self, one_asparagus_image):
        head_label = self.asparagus_head_classifier.predict(one_asparagus_image)
        return head_label

    def asparagus_contour(self, one_asparagus_image):

        gray_image = cv2.cvtColor(one_asparagus_image, cv2.COLOR_BGR2GRAY)

        ret, th = cv2.threshold(gray_image,
                                0,
                                255,
                                cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        th_to_snip_asparagus_contour = KeepNLargestAreaContours(image=th,
                                                                kept_contour_number=1,
                                                                invert_flag=False).kept_n_largest_area_contours_image

        th_to_find_contours = th.copy()
        _, contours, hierarchy = cv2.findContours(th_to_find_contours, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        largest_contour = self.largest_contour(contours)
        min_area_bounding_rectangle = cv2.minAreaRect(largest_contour)

        asparagus_contour = self.subimage(image=th_to_snip_asparagus_contour,
                                          center=min_area_bounding_rectangle[0],
                                          theta=min_area_bounding_rectangle[2],
                                          width=min_area_bounding_rectangle[1][0],
                                          height=min_area_bounding_rectangle[1][1])

        asparagus_contour = self.orientation_correction(asparagus_contour)

        kernel = np.ones((5, 5), np.uint8)

        opened_asparagus_contour = cv2.morphologyEx(asparagus_contour, cv2.MORPH_OPEN, kernel)

        return opened_asparagus_contour

    # TODO : test
    def asparagus_thickness_and_length(self, one_asparagus_image):
        asparagus_contour = self.asparagus_contour(one_asparagus_image)

        thicknesses = (asparagus_contour != 0).sum(1)
        thicknesses_sorted = np.sort(thicknesses)
        thicknesses_narrowed = thicknesses_sorted[0:int(len(thicknesses_sorted)*0.8)]
        thicknesses_max = max(thicknesses_narrowed)

        length = asparagus_contour.shape[0]
        return [thicknesses_max, length]


    def asparagus_length(self, one_asparagus_image):
        return self.asparagus_contour(one_asparagus_image).shape[0]

    def asparagus_thickness(self, one_asparagus_image):
        thicknesses = (self.asparagus_contour(one_asparagus_image) != 0).sum(1)
        thicknesses_sorted = np.sort(thicknesses)
        thicknesses_narrowed = thicknesses_sorted[0:int(len(thicknesses_sorted)*0.8)]
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
    def subimage(image, center, theta, width, height):
        theta *= 3.14159 / 180  # convert to rad

        v_x = (np.cos(theta), np.sin(theta))
        v_y = (-np.sin(theta), np.cos(theta))
        s_x = center[0] - v_x[0] * (width / 2) - v_y[0] * (height / 2)
        s_y = center[1] - v_x[1] * (width / 2) - v_y[1] * (height / 2)

        mapping = np.array([[v_x[0], v_y[0], s_x],
                            [v_x[1], v_y[1], s_y]])

        return cv2.warpAffine(image, mapping, (int(width), int(height)), flags=cv2.WARP_INVERSE_MAP,
                              borderMode=cv2.BORDER_REPLICATE)

    @staticmethod
    def orientation_correction(image):
        if image.shape[0] < image.shape[1]:
            image = np.rot90(image)

        return image

