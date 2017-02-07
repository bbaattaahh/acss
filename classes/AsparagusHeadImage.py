class AsparagusHeadImage:

    def __init__(self,
                 image,
                 top_part_to_keep_ratio,
                 output_resolution):

        self.image = image
        self.top_part_to_keep_ratio = top_part_to_keep_ratio
        self.output_resolution = output_resolution

    @property
    def top_part(self):
        _, w, _ = self.image.shape
        top_part = self.image[:, int((1-self.top_part_to_keep_ratio)*w):w, :]
        return top_part
