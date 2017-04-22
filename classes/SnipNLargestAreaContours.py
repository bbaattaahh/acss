import numpy as np
import cv2

from operator import itemgetter

from SnipFromImage import SnipFromImage


class SnipNLargestAreaContours:
    def __init__(self,
                 image,
                 n,
                 invert_flag=False):

        self.image = image
        self.n = n
        self.invert_flag = invert_flag

    @property
    def n_largest_area_contours_images(self):
        if self.invert_flag:
            self.image = self.invert_image(self.image)

        self.delete_contours()

        contours_to_snip = self.first_level_contours

        bounding_rectangles = []
        for contour_to_snip in contours_to_snip:
            x, y, w, h = cv2.boundingRect(contour_to_snip)
            bounding_rectangles.append([x, y, w, h])

        sorted_bounding_rectangles = sorted(bounding_rectangles, key=itemgetter(0))

        snipped_images = []
        for bounding_rectangle in sorted_bounding_rectangles:
            actual_snipped_image = SnipFromImage(self.image,
                                                 x=bounding_rectangle[0],
                                                 y=bounding_rectangle[1],
                                                 w=bounding_rectangle[2],
                                                 h=bounding_rectangle[3]).snipped_image

            if self.invert_flag:
                actual_snipped_image = self.invert_image(actual_snipped_image)

            snipped_images.append(actual_snipped_image)

        return snipped_images

    @staticmethod
    def invert_image(image):
        image = 255 - image
        return image

    def delete_contours(self):
        for contour_to_delete in self.contours_to_delete:
            cv2.drawContours(self.image, [contour_to_delete], 0, 0, -1)

    @property
    def contours_to_delete(self):
        contours_to_delete = []

        if len(self.first_level_contours) <= self.n:
            return contours_to_delete

        for contour in self.first_level_contours:
            if cv2.contourArea(contour) < self.area_limit:
                contours_to_delete.append(contour)

        return contours_to_delete

    @property
    def area_limit(self):
        contour_areas = []

        for actual_contour in self.first_level_contours:
            actual_area = cv2.contourArea(actual_contour)
            contour_areas.append(actual_area)

        area_limit = np.sort(contour_areas)[-1 * self.n]

        return area_limit

    @property
    def first_level_contours(self):
        first_level_contours = []
        copy_to_detect_contours = self.image.copy()
        _, contours, hierarchy = cv2.findContours(copy_to_detect_contours, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        actual_contour_index = 0

        while actual_contour_index != -1 and contours:
            first_level_contours.append(contours[actual_contour_index])
            actual_contour_index = hierarchy[0][actual_contour_index][0]

        return first_level_contours
