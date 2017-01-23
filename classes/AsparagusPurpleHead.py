import cv2
import numpy as np


class AsparagusPurpleHead:

    def __init__(self,
                 image,
                 bounder=([200, 127, 200], [255, 200, 255])):

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
