class BucketMarker:
    def __init__(self,
                 marker_image,
                 bounding_rectangle_on_original_image,
                 right_bucket_number,
                 left_bucket_number):

        self.marker_image = marker_image
        self.bounding_rectangle_on_original_image = bounding_rectangle_on_original_image
        self.right_bucket_number = right_bucket_number
        self.left_bucket_number = left_bucket_number

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    @property
    def middle_x(self):
        middle_x = int(self.bounding_rectangle_on_original_image.top_left_x +
                       self.bounding_rectangle_on_original_image.width/2)
        return middle_x

