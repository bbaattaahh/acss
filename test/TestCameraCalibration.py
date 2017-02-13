import unittest
import cv2
import numpy as np

from CameraCalibration import CameraCalibration


class TestCameraCalibration(unittest.TestCase):
    def test_CameraCalibration_working(self):
        # given
        square_page_length_in_millimeter = 20.0
        image = cv2.imread("./images/CameraCalibration/test_CameraCalibration_working.jpg")
        chessboard_row_number = 8
        chessboard_column_number = 8
        camera_calibration = CameraCalibration(square_page_length_in_millimeter=square_page_length_in_millimeter,
                                               image=image,
                                               chessboard_row_number=chessboard_row_number,
                                               chessboard_column_number=chessboard_column_number)

        expected_pixel_millimeter_ratio = 3.5965961456298827
        expected_millimeter_pixel_ratio = 0.27804066942991928
        expected_variance_square_page_length = np.float32(1.4898456)

        # when
        actual_pixel_millimeter_ratio = camera_calibration.pixel_millimeter_ratio
        actual_millimeter_pixel_ratio = camera_calibration.millimeter_pixel_ratio
        actual_variance_square_page_length = camera_calibration.variance_square_page_length

        # that
        self.assertEqual(actual_pixel_millimeter_ratio, expected_pixel_millimeter_ratio)
        self.assertEqual(actual_millimeter_pixel_ratio, expected_millimeter_pixel_ratio)
        self.assertEqual(actual_variance_square_page_length, expected_variance_square_page_length)


if __name__ == '__main__':
    unittest.main()