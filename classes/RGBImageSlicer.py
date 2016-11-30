###########
#  I |II  #
# ---+--- #
# III|VI  #
###########


class RGBImageSlicer:

    def __init__(self,
                 image):

        self.image = image
        self.height, self.width, _ = image.shape

    @property
    def first_quarter(self):
        width_from = 0
        width_to = self.width / 2

        height_from = 0
        height_to = self.height / 2

        first_quarter_image = self.image[height_from:height_to, width_from:width_to, :]

        return first_quarter_image

    @property
    def second_quarter(self):
        width_from = self.width / 2
        width_to = self.width

        height_from = 0
        height_to = self.height / 2

        second_quarter_image = self.image[height_from:height_to, width_from:width_to, :]

        return second_quarter_image

    @property
    def third_quarter(self):
        width_from = 0
        width_to = self.width / 2

        height_from = self.height / 2
        height_to = self.height

        third_quarter_image = self.image[height_from:height_to, width_from:width_to, :]

        return third_quarter_image

    @property
    def fourth_quarter(self):
        width_from = self.width / 2
        width_to = self.width

        height_from = self.height / 2
        height_to = self.height

        fourth_quarter_image = self.image[height_from:height_to, width_from:width_to, :]

        return fourth_quarter_image
