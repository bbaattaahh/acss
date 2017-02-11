import numpy as np
import cv2


class CameraCalibration:
    def __init__(self,
                 square_page_length_in_millimeter,
                 image,
                 chessboard_row_number=8,
                 chessboard_column_number=8):

        self.square_page_length_in_millimeter = square_page_length_in_millimeter
        self.image = image
        self.chessboard_row_number = chessboard_row_number
        self.chessboard_column_number = chessboard_column_number

    @property
    def pixel_millimeter_ratio(self):
        square_page_length = self.mean_square_page_length_in_pixel
        return square_page_length / self.square_page_length_in_millimeter

    @property
    def millimeter_pixel_ratio(self):
        square_page_length = self.mean_square_page_length_in_pixel
        return self.square_page_length_in_millimeter / square_page_length

    @property
    def mean_square_page_length_in_pixel(self):
        return np.mean(self.square_page_length_in_rows_in_pixel)

    @property
    def variance_square_page_length(self):
        return np.var(self.square_page_length_in_rows_in_pixel)

    @property
    def square_page_length_in_rows_in_pixel(self):
        corners = self.corner_points
        neighbour_distances = []
        for column in range(0, self.chessboard_column_number - 1):
            for row in range(0, self.chessboard_row_number - 2):
                actual_point = corners[column * (self.chessboard_row_number - 1) + row][0]
                left_neighbour = corners[column * (self.chessboard_row_number - 1) + row + 1][0]
                actual_distance = np.linalg.norm(actual_point - left_neighbour)
                neighbour_distances.append(actual_distance)

        return neighbour_distances

    @property
    def __gray_image(self):
        gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        return gray_image

    @property
    def corner_points(self):
        gray_image = self.__gray_image
        ret, corners = cv2.findChessboardCorners(gray_image,
                                                 (self.chessboard_row_number - 1, self.chessboard_column_number - 1),
                                                 None)
        return corners
