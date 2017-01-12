class SnipFromImage(object):

    def __init__(self,
                 image,
                 x,
                 y,
                 w,
                 h):

        self.image = image
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    @property
    def snipped_image(self):
        # gray image
        if len(self.image.shape) == 2:
            return self.image[self.y: self.y + self.h, self.x: self.x + self.w]

        # rgb image
        if len(self.image.shape) == 3:
            return self.image[self.y: self.y + self.h, self.x: self.x + self.w, :]
