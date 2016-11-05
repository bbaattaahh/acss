class IsRectangleOnImage:
    def __init__(self,
                 rectangle,
                 image):

        self.rectangle = rectangle
        self.image = image
        self.x_lower = 0
        self.x_upper = image.shape[1]
        self.y_lower = 0
        self.y_upper = image.shape[0]

    def is_it(self):
        for vertex in self.rectangle.vertices:
            if self.x_lower > vertex[0]:
                return False
            if self.x_upper < vertex[0]:
                return False

            if self.y_lower > vertex[1]:
                return False
            if self.y_upper < vertex[1]:
                return False

        return True