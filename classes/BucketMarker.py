import numpy as np

from SnipFromImage import SnipFromImage
from BucketNumbersIdentifier import BucketNumbersIdentifier


class BucketMarker:
    def __init__(self,
                 image,
                 bounding_rectangle_on_original_image):

        self.image = image
        self.bounding_rectangle_on_original_image = bounding_rectangle_on_original_image

        self.bucket_marker_image = SnipFromImage(self.image,
                                            x=self.bounding_rectangle_on_original_image.top_left_x,
                                            y=self.bounding_rectangle_on_original_image.top_left_y,
                                            w=self.bounding_rectangle_on_original_image.width,
                                            h=self.bounding_rectangle_on_original_image.high).snipped_image
        bucket_number_identifier = BucketNumbersIdentifier(self.bucket_marker_image)
        self.left_bucket_number=bucket_number_identifier.left_bucket_number
        self.right_bucket_number=bucket_number_identifier.right_bucket_number

    def __eq__(self, other):
        if not np.array_equal(self.image, other.image):
            return False

        if self.bounding_rectangle_on_original_image != other.bounding_rectangle_on_original_image:
            return False

        return True

    @property
    def middle_x(self):
        middle_x = int(self.bounding_rectangle_on_original_image.top_left_x +
                       self.bounding_rectangle_on_original_image.width/2)
        return middle_x
