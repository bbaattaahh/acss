import cv2
import numpy as np


class RGBTemplateMatching:

    cv2_matching_method = cv2.TM_CCOEFF_NORMED

    def __init__(self,
                 rgb_image,
                 rgb_template,
                 threshold=2.3):

        self.rgb_image = rgb_image
        self.rgb_template = rgb_template
        self.threshold = threshold
        _, self.width, _ = self.rgb_template.shape

    @property
    def rectangle_top_left_vertices(self):

        top_left_corners = []

        y_coordinate = int(np.mean(self.locations[0]))
        x_coordinates = self.get_x_coordinates()

        for x_coordinate in x_coordinates:
            top_left_corners.append([x_coordinate, y_coordinate])

        return top_left_corners

    @property
    def locations(self):
        match_red = cv2.matchTemplate(self.rgb_image[:, :, 0],
                                      self.rgb_template[:, :, 0],
                                      RGBTemplateMatching.cv2_matching_method)

        match_green = cv2.matchTemplate(self.rgb_image[:, :, 1],
                                        self.rgb_template[:, :, 1],
                                        RGBTemplateMatching.cv2_matching_method)

        match_blue = cv2.matchTemplate(self.rgb_image[:, :, 2],
                                       self.rgb_template[:, :, 2],
                                       RGBTemplateMatching.cv2_matching_method)

        match_rgb = match_red + match_green + match_blue

        locations = np.where(match_rgb >= self.threshold)

        return locations


    def get_x_coordinates(self):
        x_coordinates_to_one_match = []

        sorted_x_coordinates = np.sort(self.locations[1])
        numeric_derivation_of_sorted_x_coordinates = np.diff(sorted_x_coordinates)
        fractures = np.where(numeric_derivation_of_sorted_x_coordinates >= self.width)
        fractures = self.tuple_numpy_array_to_list(fractures)
        fractures = self.numerical_derivation_position_correction(fractures)

        fractures = [0] + fractures + [len(sorted_x_coordinates)]

        for fracture_index in range(len(fractures)-1):
            one_group_x_coordinates = sorted_x_coordinates[fractures[fracture_index]:fractures[fracture_index+1]]
            mean_x_coordinate = int(np.mean(one_group_x_coordinates))
            x_coordinates_to_one_match.append(mean_x_coordinate)

        return x_coordinates_to_one_match

    @staticmethod
    def tuple_numpy_array_to_list(tuple_numpy_array):
        np_array = np.asarray(tuple_numpy_array)[0]
        python_list = np_array.tolist()
        return python_list

    @staticmethod
    def numerical_derivation_position_correction(series):
        return map(lambda x: x + 1, series)
