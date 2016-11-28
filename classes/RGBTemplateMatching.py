import cv2
import numpy as np


class RGBTemplateMatching:
    def __init__(self,
                 rgb_image,
                 rgb_template,
                 threshold,
                 cv2_method):

        self.rgb_image = rgb_image
        self.rgb_template = rgb_template
        self.threshold = threshold
        self.cv2_method = cv2_method
        _, self.width, _ = self.rgb_template.shape
        self.locations = self.rgb_match()

    def rgb_match(self):
        match_red = cv2.matchTemplate(self.rgb_image[:, :, 0], self.rgb_template[:, :, 0], self.cv2_method)
        match_green = cv2.matchTemplate(self.rgb_image[:, :, 1], self.rgb_template[:, :, 1], self.cv2_method)
        match_blue = cv2.matchTemplate(self.rgb_image[:, :, 2], self.rgb_template[:, :, 2], self.cv2_method)

        match_rgb = match_red + match_green + match_blue

        locations = np.where(match_rgb >= self.threshold)

        return locations

    def rectangle_top_left_vertices(self):

        top_left_corners = []

        y_coordinate = int(np.mean(self.locations[0]))

        sorted_x_coordinates = np.sort(self.locations[1])
        numeric_derivation_of_sorted_x_coordinates = np.diff(sorted_x_coordinates)
        fractures = np.where(numeric_derivation_of_sorted_x_coordinates >= self.width)
        fractures = np.asarray(fractures)[0]
        fractures = fractures.tolist()
        fractures = map(lambda x: x + 1, fractures)

        fractures = [0] + fractures + [len(sorted_x_coordinates)]

        for fracture_index in range(len(fractures)-1):
            one_group_x_coordinates = sorted_x_coordinates[fractures[fracture_index]:fractures[fracture_index+1]]
            x_coordinate = int(np.mean(one_group_x_coordinates))
            top_left_corners.append([x_coordinate,y_coordinate])

        return top_left_corners