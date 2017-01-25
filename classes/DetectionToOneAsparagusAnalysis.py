import numpy as np


class DetectionToOneAsparagusAnalysis:
    def __init__(self,
                 image,
                 rectangle_on_original_image):
        self.image = image
        self.rectangle_on_original_image = rectangle_on_original_image

    def __eq__(self, other):
        if not np.array_equal(self.image, other.image):
            return False

        if not (self.rectangle_on_original_image == other.rectangle_on_original_image):
            return False

        return True
