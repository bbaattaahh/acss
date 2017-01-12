class PositionConverter:

    def __init__(self,
                 original_position,
                 original_resolution,
                 target_resolution):

        self.original_position = original_position
        self.original_resolution = original_resolution
        self.target_resolution = target_resolution

    @property
    def get_target_position(self):
        scale_factor_height = float(self.target_resolution[0]) / float(self.original_resolution[0])
        scale_factor_width = float(self.target_resolution[1]) / float(self.original_resolution[1])

        scaled_x = int(self.original_position[0] * scale_factor_width)
        scaled_y = int(self.original_position[1] * scale_factor_height)

        return scaled_x, scaled_y
