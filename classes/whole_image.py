__author__ = 'Henrik'

class whole_image:
    def __init__(self, original_picture, picture_with_modifications, list_of_asparagus_subimages, list_of_asparaguses):
        self.original_picture = original_picture
        self.picture_with_modifications = picture_with_modifications
        self.list_of_asparagus_subimages = list_of_asparagus_subimages
        self.list_of_asparaguses = list_of_asparaguses


    def add_asparagus_subimage(self, subimage):
        self.list_of_asparagus_subimages.append(subimage)


    def add_asparagus(self, asparagus):
        self.list_of_asparaguses.append(asparagus)


    def calculate_sub_image(self, index):
        act_sum_img = self.list_of_asparagus_subimages[index]
        self.sub_image = self.original_picture[act_sum_img.top_left_corner_y : act_sum_img.top_left_corner_y + act_sum_img.hight,
                                               act_sum_img.top_left_corner_x : act_sum_img.top_left_corner_x + act_sum_img.width]


