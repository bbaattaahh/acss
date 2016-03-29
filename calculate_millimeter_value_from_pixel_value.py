__author__ = 'Henrik'

import whole_image

def calculate_millimeter_value_from_pixel_value(pixel_millimeter_ratio, my_whole_image):

    for act_asparagus in my_whole_image.asparaguses:
        act_asparagus.width_millimeter = act_asparagus.width_pixel * pixel_millimeter_ratio
        act_asparagus.hight_millimeter = act_asparagus.hight_pixel * pixel_millimeter_ratio

    return None