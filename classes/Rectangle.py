import numpy as np


class Rectangle:
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
        self.vertices = [self.top_left_corner(),
                         self.top_right_corner(),
                         self.bottom_right_corner(),
                         self.bottom_left_corner()]

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def top_left_corner(self):
        return [self.top_left_x, self.top_left_y]

    def top_right_corner(self):
        top_left_corner = self.to_vector(self.top_left_x, self.top_left_y)
        non_rotated_vector = self.to_vector(self.width, 0)
        rot_matrix = self.rotation_matrix(self.angle)
        rotated_vector = np.dot(rot_matrix, non_rotated_vector)
        top_right_corner = top_left_corner + rotated_vector
        top_right_corner_list = self.vector_to_list(top_right_corner)
        return top_right_corner_list

    def bottom_right_corner(self):
        top_left_corner = self.to_vector(self.top_left_x, self.top_left_y)
        non_rotated_vector = self.to_vector(self.width, self.high)
        rot_matrix = self.rotation_matrix(self.angle)
        rotated_vector = np.dot(rot_matrix, non_rotated_vector)
        bottom_right_corner = top_left_corner + rotated_vector
        bottom_right_corner_list = self.vector_to_list(bottom_right_corner)
        return bottom_right_corner_list

    def bottom_right_corner(self):
        top_left_corner = self.to_vector(self.top_left_x, self.top_left_y)
        non_rotated_vector = self.to_vector(self.width, self.high)
        rot_matrix = self.rotation_matrix(self.angle)
        rotated_vector = np.dot(rot_matrix, non_rotated_vector)
        bottom_right_corner = top_left_corner + rotated_vector
        bottom_right_corner_list = self.vector_to_list(bottom_right_corner)
        return bottom_right_corner_list

    def bottom_left_corner(self):
        top_left_corner = self.to_vector(self.top_left_x, self.top_left_y)
        non_rotated_vector = self.to_vector(0, self.high)
        rot_matrix = self.rotation_matrix(self.angle)
        rotated_vector = np.dot(rot_matrix, non_rotated_vector)
        bottom_left_corner = top_left_corner + rotated_vector
        bottom_left_corner_list = self.vector_to_list(bottom_left_corner)
        return bottom_left_corner_list

    @staticmethod
    def to_vector(x, y):
        return np.array([[x], [y]])

    @staticmethod
    def rotation_matrix(angle):
        rad = np.deg2rad(angle)
        rot_matrix = np.array([[np.cos(rad), -np.sin(rad)],
                              [np.sin(rad), np.cos(rad)]])
        return rot_matrix

    @staticmethod
    def vector_to_list(vector):
        return vector[0].tolist() + vector[1].tolist()

    @property
    def middle_x(self):
        return int(self.top_left_x + self.width/2)
