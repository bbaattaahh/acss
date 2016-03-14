__author__ = 'Henrik'


class asparagus:
    def __init__(self, width_pixel, hight_pixel, width_millimeter, hight_millimeter, classification):
        self.width_pixel = width_pixel
        self.hight_pixel = hight_pixel
        self.width_millimeter = width_millimeter
        self.hight_millimeter = hight_millimeter
        self.classification = classification

def define_default_asparagus():
    return asparagus(0, 0, 0, 0, "None")