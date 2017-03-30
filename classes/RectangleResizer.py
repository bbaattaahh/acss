from Rectangle import Rectangle


class RectangleResizer:
    def __init__(self,
                 original_resolution,
                 target_resolution):

        self.x_scale_factor = target_resolution[1] / original_resolution[1]
        self.y_scale_factor = target_resolution[0] / original_resolution[0]

    def resize(self, rectangle):
        new_top_left_x = int(rectangle.top_left_x * self.x_scale_factor)
        new_top_left_y = int(rectangle.top_left_y * self.y_scale_factor)
        new_width = int(rectangle.width * self.x_scale_factor)
        new_high = int(rectangle.high * self.y_scale_factor)

        resized_rectangle = Rectangle(top_left_x=new_top_left_x,
                                      top_left_y=new_top_left_y,
                                      width=new_width,
                                      high=new_high)
        return resized_rectangle
