__author__ = 'Henrik'

def calculate_millimeter_value_from_pixel_value(pixel_millimeter_ratio, asparagus):

    asparagus.width_millimeter = asparagus.width_pixel * pixel_millimeter_ratio
    asparagus.hight_millimeter = asparagus.hight_pixel * pixel_millimeter_ratio

    return None