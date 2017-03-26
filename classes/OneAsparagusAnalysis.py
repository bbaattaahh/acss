import cv2
import numpy as np

from SnipFromImage import SnipFromImage
from Asparagus import Asparagus


class OneAsparagusAnalysis:
    def __init__(self,
                 one_asparagus_image,
                 asparagus_head_classifier):

        self.one_asparagus_image = one_asparagus_image
        self.asparagus_head_classifier = asparagus_head_classifier

    @property
    def asparagus(self):
        asparagus = Asparagus(length=self.asparagus_length(),
                              thickness=self.asparagus_thickness(),
                              white_head=False,
                              no_head=False,
                              purple_head=False,
                              open_head=False,
                              piper=False)

        head_label = self.head_label
        if head_label == "white":
            asparagus.white_head = True
        if head_label == "no_head":
            asparagus.no_head = True
        if head_label == "purple":
            asparagus.purple_head = True
        if head_label == "open_head":
            asparagus.no_head = True

        return asparagus

    @property
    def head_label(self):
        head_label = self.asparagus_head_classifier.predict(self.one_asparagus_image)
        return head_label

    @property
    def asparagus_contour(self):

        gray_image = cv2.cvtColor(self.one_asparagus_image, cv2.COLOR_BGR2GRAY)

        ret, th = cv2.threshold(gray_image,
                                0,
                                255,
                                cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        th_to_find_contours = th.copy()
        _, contours, hierarchy = cv2.findContours(th_to_find_contours, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        largest_contour = self.largest_contour(contours)
        x, y, w, h = cv2.boundingRect(largest_contour)
        asparagus_contour = SnipFromImage(image=th, x=x, y=y, w=w, h=h).snipped_image

        kernel = np.ones((5, 5), np.uint8)

        opened_asparagus_contour = cv2.morphologyEx(asparagus_contour, cv2.MORPH_OPEN, kernel)

        return opened_asparagus_contour

    @property
    def asparagus_in_smallest_enclosing_box(self):

        gray_image = cv2.cvtColor(self.one_asparagus_image, cv2.COLOR_BGR2GRAY)

        ret, th = cv2.threshold(gray_image,
                                0,
                                255,
                                cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        th_to_find_contours = th.copy()
        _, contours, hierarchy = cv2.findContours(th_to_find_contours, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        largest_contour = self.largest_contour(contours)
        x, y, w, h = cv2.boundingRect(largest_contour)
        asparagus_in_smallest_enclosing_box = SnipFromImage(image=self.one_asparagus_image,
                                                            x=x,
                                                            y=y,
                                                            w=w,
                                                            h=h).snipped_image

        return asparagus_in_smallest_enclosing_box

    def asparagus_length(self):
        return self.asparagus_contour.shape[0]

    def asparagus_thickness(self):
        thicknesses = (self.asparagus_contour != 0).sum(1)
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
