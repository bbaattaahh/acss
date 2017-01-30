import cv2
import numpy as np

from KeepNLargestAreaContours import KeepNLargestAreaContours


class AsparagusPurpleHead:
    def __init__(self,
                 image,
                 bounder=([130, 0, 130], [255, 230, 255])):
        self.image = image
        self.bounder = bounder

    @property
    def color_filtered_image(self):
        lower, upper = self.bounder
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")

        # find the colors within the specified boundaries and apply
        # the mask
        mask = cv2.inRange(self.image, lower, upper)
        output = cv2.bitwise_and(self.image, self.image, mask=mask)

        return output

    @property
    def green_layer(self):
        green_layer = self.asparagus_with_masked_background[:, :, 1]
        return green_layer

    @property
    def asparagus_with_masked_background(self):
        asparagus_with_masked_background = cv2.bitwise_and(self.image, self.image, mask=self.asparagus_mask)
        return asparagus_with_masked_background

    @property
    def asparagus_mask(self):
        gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        ret, th = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        th = self.set_img_frame_black(th)
        kernel = np.ones((5, 5), np.uint8)
        th = cv2.morphologyEx(th, cv2.MORPH_OPEN, kernel)
        keep_largest_area_contour = KeepNLargestAreaContours(image=th, kept_contour_number=1, invert_flag=False)
        one_contour_image = keep_largest_area_contour.kept_n_largest_area_contours_image

        closed_asparagus_contour = cv2.morphologyEx(one_contour_image, cv2.MORPH_CLOSE, kernel, iterations=2)

        return closed_asparagus_contour

    @staticmethod
    def set_img_frame_black(image):
        height, width = image.shape

        image[:, 0] = 0
        image[:, width - 1] = 0
        image[0, :] = 0
        image[height - 1, :] = 0

        return image
