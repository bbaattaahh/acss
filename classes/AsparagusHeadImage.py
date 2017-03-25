from ImageResizer import ImageResizer

class AsparagusHeadImage:

    def __init__(self,
                 image,
                 top_part_to_keep_ratio,
                 output_resolution):

        self.image = image
        self.top_part_to_keep_ratio = top_part_to_keep_ratio
        self.output_resolution = output_resolution

    @property
    def resized_top_part(self):
        resized_top_part = ImageResizer(image=self.top_part,
                                        target_resolution=self.output_resolution).resized_image
        return resized_top_part

    @property
    def top_part(self):
        h, _, _ = self.image.shape
        top_part = self.image[ :int(self.top_part_to_keep_ratio*h), :, :]
        return top_part
