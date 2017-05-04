import numpy as np


class DetectionToOneAsparagusAnalysis:
    def __init__(self,
                 image,
                 opencv_rectangle_on_original_image):

        self.image = image
        self.opencv_rectangle_on_original_image = opencv_rectangle_on_original_image

    def __eq__(self, other):
        if not np.array_equal(self.image, other.image):
            return False

        if not (self.opencv_rectangle_on_original_image == other.opencv_rectangle_on_original_image):
            return False

        return True
