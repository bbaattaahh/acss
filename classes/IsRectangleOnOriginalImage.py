import numpy as np


class IsRectangleOnOriginalImage:
    def __init__(self,
                 original_image,
                 rectangle_on_rotated_image,
                 angle):

        self.original_image = original_image
        self.rectangle_on_rotated_image = rectangle_on_rotated_image
        self.angle = angle
        self.is_it = self.is_rectangle_on_original_image()

    def is_rectangle_on_original_image(self):
        for vertex in self.rectangle_on_rotated_image.vertices:
            original_vertex = self.calulate_original_coordinat_before_rotation(vertex)

            if not self.is_vertex_on_original_image(original_vertex):
                return False

        return True

    def calulate_original_coordinat_before_rotation(self, vertex):
        point_numpy = np.array([[vertex[0]],[vertex[1]]])

        w_original = self.original_image.shape[1]
        h_original = self.original_image.shape[0]

        # now calculate new image width and height
        rangle = np.deg2rad(self.angle)  # angle in radians
        w_rotated = abs(np.sin(rangle) * h_original) + abs(np.cos(rangle) * w_original)
        h_rotated = abs(np.cos(rangle) * h_original) + abs(np.sin(rangle) * w_original)


        # From top left coorner to centrum of image
        centrum_vector = np.array([[-w_rotated / 2], [-h_rotated / 2]])

        point_relative_to_centrum = point_numpy + centrum_vector

        # Rotation back
        theta = np.deg2rad(self.angle)
        rotMatrix = np.array([[np.cos(theta), -np.sin(theta)],
                              [np.sin(theta), np.cos(theta)]])
        rotated_point_relative_to_centrum = np.dot(rotMatrix, point_relative_to_centrum)

        # Centrum to top left coorner
        top_left_centrum_point = rotated_point_relative_to_centrum - centrum_vector

        # Compenyation with picture growth
        w_growth_on_one_side = (w_rotated - w_original) / 2
        h_growth_on_one_side = (h_rotated - h_original) / 2
        compensation_vector = np.array([[w_growth_on_one_side], [h_growth_on_one_side]])

        original_point = top_left_centrum_point - compensation_vector
        original_point_list = original_point.tolist()
        original_point_list_single_level = [original_point_list[0][0], original_point_list[1][0]]

        return (original_point_list_single_level)

    def is_vertex_on_original_image(self, vertex):
        if 0 > vertex[0]:
            return False
        if self.original_image.shape[1] < vertex[0]:
            return False
        if 0 > vertex[1]:
            return False
        if self.original_image.shape[0] < vertex[1]:
            return False

        return True
