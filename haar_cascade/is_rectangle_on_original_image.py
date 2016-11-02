import numpy as np
import math
import cv2

from Rectangle import Rectangle

def is_rectangle_on_original_image(rectangle, original_image, rotated_image, angle):
    xy_limits = image_borders(original_image)

    for vertex in rectangle.vertices:
        original_vertex = calulate_original_coordinat_before_rotation(original_image,
                                                                      rotated_image,
                                                                      point=vertex,
                                                                      angle=angle)


        if not (xy_limits["x"][0] <= original_vertex[0] and original_vertex[0] <= xy_limits["x"][1]):
            return False

        if not (xy_limits["y"][0] <= original_vertex[1] and original_vertex[1] <= xy_limits["y"][1]):
            return False

    return True


def image_borders(image):
    x_min = 0
    y_min = 0

    x_max = image.shape[1]
    y_max = image.shape[0]

    return {"x" : [x_min, x_max], "y" : [y_min, y_max]}


def calulate_original_coordinat_before_rotation(original_image, rotated_image, point, angle):
    point_numpy = np.array([[point[0]],[point[1]]])

    w_original = original_image.shape[1]
    h_original = original_image.shape[0]

    w_rotated = rotated_image.shape[1]
    h_rotated = rotated_image.shape[0]

    # From top left coorner to centrum of image
    centrum_vector = np.array([[-w_rotated / 2], [-h_rotated / 2]])

    point_relative_to_centrum = point_numpy + centrum_vector

    # Rotation back
    theta = np.deg2rad(angle)
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