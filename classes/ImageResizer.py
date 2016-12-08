import cv2


class ImageResizer:
    def __init__(self,
                 image,
                 target_resolution,
                 parent_image_resolution=None):

        self.image = image
        self.image_height, self.image_width = self.image.shape
        self.target_height, self.target_width = target_resolution

        if parent_image_resolution is None:
            self.parent_image_height, self.parent_image_width = image.shape[0:2]
        else:
            self.parent_image_height, self.parent_image_width = parent_image_resolution

    @property
    def resized_image(self):
        resized_image = cv2.resize(self.image,
                                   None,
                                   fx=self.new_size[1],
                                   fy=self.new_size[0],
                                   interpolation=cv2.INTER_CUBIC)
        return resized_image

    @property
    def new_size(self):
        new_height = self.target_height/self.parent_image_height * self.image_height
        new_width = self.target_width/self.parent_image_width * self.image_width
        return new_height, new_width
