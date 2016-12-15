import cv2


class ImageResizer:
    def __init__(self,
                 image,
                 target_resolution,
                 parent_image_resolution=None):

        self.image = image
        self.image_height, self.image_width = self.image.shape[0:2]
        self.target_height, self.target_width = target_resolution
        
        if parent_image_resolution is None:
            self.parent_image_height = self.image_height
            self.parent_image_width = self.image_width
        else:
            self.parent_image_height, self.parent_image_width = parent_image_resolution

    @property
    def resized_image(self):
        resized_image = cv2.resize(self.image,
                                   None,
                                   fx=self.scale_factores[1],
                                   fy=self.scale_factores[0],
                                   interpolation=cv2.INTER_CUBIC)
        return resized_image

    @property
    def scale_factores(self):
        scale_y = float(self.new_sizes[0]) / float(self.image_height)
        scale_x = float(self.new_sizes[1]) / float(self.image_width)
        return scale_y, scale_x

    @property
    def new_sizes(self):
        new_height = int(float(self.target_height)/self.parent_image_height * self.image_height)
        new_width = int(float(self.target_width)/self.parent_image_width * self.image_width)
        return new_height, new_width
