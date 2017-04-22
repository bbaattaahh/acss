import numpy as np

from SnipFromImage import SnipFromImage


class BucketMarker:
    def __init__(self,
                 image,
                 bounding_rectangle,
                 bucket_number_identifier):

        self.image = image
        self.bounding_rectangle = bounding_rectangle

        self.bucket_marker_image = SnipFromImage(self.image,
                                                 x=self.bounding_rectangle.top_left_x,
                                                 y=self.bounding_rectangle.top_left_y,
                                                 w=self.bounding_rectangle.width,
                                                 h=self.bounding_rectangle.high).snipped_image

        self.left_bucket_number=bucket_number_identifier.left_bucket_number(self.bucket_marker_image)
        self.right_bucket_number=bucket_number_identifier.right_bucket_number(self.bucket_marker_image)

    def __eq__(self, other):
        if not np.array_equal(self.image, other.image):
            return False

        if self.bounding_rectangle != other.bounding_rectangle:
            return False

        return True

    @property
    def middle_x(self):
        middle_x = int(self.bounding_rectangle.top_left_x +
                       self.bounding_rectangle.width / 2)
        return middle_x
