__author__ = 'Henrik'

import datetime

class whole_image:
    def __init__(self,
                 original_picture,
                 picture_with_modifications = None,
                 background_mask = None,
                 creation_time_original_image = datetime.datetime.now(),
                 asparaguses = []):

        self.original_picture = original_picture
        self.picture_with_modifications = picture_with_modifications
        self.background_mask = background_mask
        self.creation_time_original_image = creation_time_original_image
        self.asparaguses = asparaguses


    def add_asparagus(self, asparagus):
        self.asparaguses.append(asparagus)
