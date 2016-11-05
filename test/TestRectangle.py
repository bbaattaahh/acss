import unittest
from Rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_vertices_calculation(self):
        # given
        x_top_left = 0
        y_top_left = 0
        width = 10
        high = 20

        expected_vertices = [[ 0,  0],
                             [10,  0],
                             [ 0, 20],
                             [10, 20]]

        # when
        rectangle = Rectangle(x_top_left,
                              y_top_left,
                              width,
                              high)

        actual_vertices = rectangle.vertices

        # that
        self.assertEqual(actual_vertices, expected_vertices)



if __name__ == '__main__':
    unittest.main()