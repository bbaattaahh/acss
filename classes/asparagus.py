__author__ = 'Henrik'


class asparagus:
    def __init__(self,
                 sub_image = None,
                 top_left_corner_x = None,
                 top_left_corner_y = None,
                 width_pixel = None,
                 hight_pixel = None,
                 width_millimeter = None,
                 hight_millimeter = None,
                 classification = None):

        self.sub_image = sub_image
        self.top_left_corner_x = top_left_corner_x
        self.top_left_corner_y = top_left_corner_y
        self.width_pixel = width_pixel
        self.hight_pixel = hight_pixel
        self.width_millimeter = width_millimeter
        self.hight_millimeter = hight_millimeter
        self.classification = classification


def define_default_asparagus():
    return asparagus(0, 0, 0, 0, "None")