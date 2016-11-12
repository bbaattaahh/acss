class DetectionToOneAsparagusAnalysis:
    def __init__(self,
                 image,
                 x_top_left_on_original_image,
                 y_top_left_on_original_image,
                 width_on_original_image,
                 high_on_original_image,
                 angle_on_original_image):

        self.image = image
        self.x_top_left_on_original_image = x_top_left_on_original_image
        self.y_top_left_on_original_image = y_top_left_on_original_image
        self.width_on_original_image = width_on_original_image
        self.high_on_original_image = high_on_original_image
        self.angle_on_original_image = angle_on_original_image