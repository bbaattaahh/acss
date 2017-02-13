import numpy as np
import cv2


class KeepNLargestAreaContours:
    def __init__(self,
                 image,
                 kept_contour_number,
                 invert_flag=False):

        self.image = image
        self.kept_contour_number = kept_contour_number
        self.invert_flag = invert_flag

    @property
    def kept_n_largest_area_contours_image(self):
        if self.invert_flag:
            self.invert_image()

        self.delete_contours()

        if self.invert_flag:
            self.invert_image()

        return self.image

    def invert_image(self):
        self.image = 255 - self.image

    def delete_contours(self):
        for contour_to_delete in self.contours_to_delete:
            cv2.drawContours(self.image, [contour_to_delete], 0, 0, -1)

    @property
    def contours_to_delete(self):
        contours_to_delete = []

        if len(self.first_level_contours) <= self.kept_contour_number:
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

        area_limit = np.sort(contour_areas)[-1*self.kept_contour_number]

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
