class AsparagusCandidate:
    def __init__(self,
                 top_left_x=0,
                 top_left_y=0,
                 width=0,
                 high=0,
                 angle=0):

        self.top_left_x = top_left_x
        self.top_left_y = top_left_y
        self.width = width
        self.high = high
        self.angle = angle
        self.top_left_corner = [top_left_x, top_left_y]
