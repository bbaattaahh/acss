__author__ = 'Henrik'

import datetime

class whole_image:
    def __init__(self,
                 original_picture,
                 original_picture_colourful,
                 picture_with_modifications = None,
                 background_mask = None,
                 creation_time_original_image = datetime.datetime.now(),
                 asparaguses = [],
                 overlap_forward = None,
                 overlap_backward = None):

        self.original_picture = original_picture
        self.original_picture_colourful = original_picture_colourful
        self.picture_with_modifications = picture_with_modifications
        self.background_mask = background_mask
        self.creation_time_original_image = creation_time_original_image
        self.asparaguses = asparaguses
        self.overlap_forward = overlap_forward,
        self.overlap_backward = overlap_backward


    def add_asparagus(self, asparagus):
        self.asparaguses.append(asparagus)
