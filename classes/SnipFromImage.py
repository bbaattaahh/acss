class SnipFromImage(object):

    def __init__(self,
                 image,
                 x,
                 y,
                 w,
                 h):

        self.image = image
        if x < 0:
            self.x1 = 0
        else:
            self.x1 = x

        if y < 0:
            self.y1 = 0
        else:
            self.y1 = y

        if x + w > image.shape[1]:
            self.x2 = image.shape[1]
        else:
            self.x2 = x + w

        if y + h > image.shape[0]:
            self.y2 = image.shape[0]
        else:
            self.y2 = y + h

    @property
    def snipped_image(self):
        # gray image
        if len(self.image.shape) == 2:
            return self.image[self.y1 : self.y2, self.x1 : self.x2]

        # rgb image
        if len(self.image.shape) == 3:
            return self.image[self.y1: self.y2, self.x1 : self.x2, :]
