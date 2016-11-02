class Rectangle:
    def __init__(self,
                 top_left_x=0,
                 top_left_y=0,
                 width=0,
                 high=0):

        self.top_left_x = top_left_x
        self.top_left_y = top_left_y
        self.width = width
        self.high = high
        self.vertices = [[top_left_x, top_left_y],
                         [top_left_x + width, top_left_y],
                         [top_left_x, top_left_y + high],
                         [top_left_x + width, top_left_y + high]]

