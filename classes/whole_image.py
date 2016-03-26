__author__ = 'Henrik'

from datetime import datetime

class whole_image:
    def __init__(self,
                 original_picture,
                 picture_with_modifications,
                 creation_time_original_image = datetime.now(),
                 asparagus_subimages = [] ,
                 asparaguses = []):

        self.original_picture = original_picture
        self.picture_with_modifications = picture_with_modifications
        self.creation_time_original_image = creation_time_original_image,
        self.asparagus_subimages = asparagus_subimages
        self.asparaguses = asparaguses


    def add_asparagus_subimage(self, subimage):
        self.asparagus_subimages.append(subimage)


    def add_asparagus(self, asparagus):
        self.asparaguses.append(asparagus)


    def calculate_sub_image(self, index):
        act_sum_img = self.list_of_asparagus_subimages[index]
        self.sub_image = self.original_picture[act_sum_img.top_left_corner_y : act_sum_img.top_left_corner_y + act_sum_img.hight,
                                               act_sum_img.top_left_corner_x : act_sum_img.top_left_corner_x + act_sum_img.width]


