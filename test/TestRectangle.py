import unittest
from Rectangle import Rectangle
import math
import numpy as np


class TestRectangle(unittest.TestCase):
    def test_vertices_calculation_when_angel_is_zero(self):
        # given
        x_top_left = 0
        y_top_left = 0
        width = 10
        high = 20
        angle = 0

        expected_vertices = [[ 0,  0],
                             [10,  0],
                             [10, 20],
                             [ 0, 20]]

        # when
        rectangle = Rectangle(x_top_left,
                              y_top_left,
                              width,
                              high,
                              angle)

        actual_vertices = rectangle.vertices

        # that
        self.assertEqual(actual_vertices, expected_vertices)

    def test_vertices_calculation_when_angel_is_45(self):
        # given
        x_top_left = 0
        y_top_left = 0
        width = 10
        high = 10
        angle = 45

        a = 5 * math.sqrt(2)

        expected_vertices = [[0,   0],
                             [a,   a],
                             [0, 2*a],
                             [-a,  a]]

        # when
        rectangle = Rectangle(x_top_left,
                              y_top_left,
                              width,
                              high,
                              angle)

        actual_vertices = rectangle.vertices

        # that
        self.assertEqual((np.round(actual_vertices, 2) == np.round(expected_vertices, 2)).all(), True)

    def test_to_vector(self):
        # given
        x = 6784
        y = 6784

        expected_vector = np.array([[6784], [6784]])

        # when
        rectangle = Rectangle()
        actual_vector = rectangle.to_vector(x, y)

        # that
        self.assertEqual((actual_vector == expected_vector).all(), True)

    def test_rotation_matrix(self):
        # given
        expected_rotation_matrix = np.array([[1, -0],
                                             [0,  1]])

        # when
        angle = 0
        rectangle = Rectangle()
        actual_rotation_matrix = rectangle.rotation_matrix(angle)

        # that
        self.assertEqual((actual_rotation_matrix == expected_rotation_matrix).all(), True)

    def test_vector_to_list(self):
        # given
        expected_list = [6784, 6784]

        # when
        vector = np.array([[6784], [6784]])
        rectangle = Rectangle()
        actual_list = rectangle.vector_to_list(vector)

        # that
        self.assertEqual(actual_list , expected_list)


if __name__ == '__main__':
    unittest.main()