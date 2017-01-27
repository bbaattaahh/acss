import cv2
import numpy as np
import math

from Rectangle import Rectangle
from IsRectangleOnOriginalImage import IsRectangleOnOriginalImage
from ChooseFinalCandidates import ChooseFinalCandidates
from DetectionToOneAsparagusAnalysis import DetectionToOneAsparagusAnalysis
from SnipFromImage import SnipFromImage
from ImageResizer import ImageResizer
from PositionConverter import PositionConverter


class DetectAsparaguses(object):

    def __init__(self,
                 image,
                 cascade_file,
                 detection_resolution=(480, 640),
                 swing_angle=45):

        self.image = image
        self.cascade_file = cascade_file
        self.detection_resolution = detection_resolution
        self.swing_angle = swing_angle

    @property
    def data_to_analysis_one_asparagus_images(self):
        to_asparagus_analysis = []
        for candidate in self.asparagus_candidates:
            original_rotated_image = self.rotate_about_center(self.image,
                                                              angle=candidate.angle)

            scale_back_x, scale_back_y = PositionConverter(original_position=[candidate.top_left_x, candidate.top_left_y],
                                                           original_resolution=self.image_detection_on.shape[0:2],
                                                           target_resolution=self.image.shape[0:2]).get_target_position

            scale_back_w, scale_back_h = PositionConverter(original_position=[candidate.width, candidate.high],
                                                           original_resolution=self.image_detection_on.shape[0:2],
                                                           target_resolution=self.image.shape[0:2]).get_target_position


            image_one_asparagus = SnipFromImage(image=original_rotated_image,
                                                x=scale_back_x,
                                                y=scale_back_y,
                                                w=scale_back_w,
                                                h=scale_back_h).snipped_image

            original_top_left_corner = self.calculate_original_coordinate_before_rotation(
                                                                        image=self.image,
                                                                        angle=candidate.angle,
                                                                        vertex=[scale_back_x, scale_back_y])

            rectangle_on_original_image = Rectangle(top_left_x=original_top_left_corner[0],
                                                    top_left_y=original_top_left_corner[1],
                                                    width=scale_back_w,
                                                    high=scale_back_h,
                                                    angle=candidate.angle)

            actual_detection_to_one_asparagus_analysis = DetectionToOneAsparagusAnalysis(
                                                            image=image_one_asparagus,
                                                            rectangle_on_original_image=rectangle_on_original_image)

            to_asparagus_analysis.append(actual_detection_to_one_asparagus_analysis)

        return to_asparagus_analysis

    @property
    def image_detection_on(self):
        gray_image = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
        rescaled_image = ImageResizer(gray_image, target_resolution=self.detection_resolution).resized_image
        return rescaled_image

    @property
    def asparagus_candidates(self):
        detections = []

        for angle in range(-self.swing_angle, self.swing_angle+1):
            rotated_image_detection_on = self.rotate_about_center(self.image_detection_on, angle)
            asparagus_cascade = cv2.CascadeClassifier(self.cascade_file)
            actual_asparagus_candidates = asparagus_cascade.detectMultiScale(rotated_image_detection_on, 4, 31)
            if len(actual_asparagus_candidates) != 0:
                for actual_asparagus_candidate in actual_asparagus_candidates:
                    rectangle = Rectangle(top_left_x=actual_asparagus_candidate[0].tolist(),
                                          top_left_y=actual_asparagus_candidate[1].tolist(),
                                          width=actual_asparagus_candidate[2].tolist(),
                                          high=actual_asparagus_candidate[3].tolist(),
                                          angle=0)
                    is_rectangle_on_original_image = IsRectangleOnOriginalImage(self.image_detection_on,
                                                                                rectangle_on_rotated_image=rectangle,
                                                                                angle=angle)

                    if is_rectangle_on_original_image.is_it:
                        actual_asparagus_candidate = Rectangle(
                                                top_left_x=actual_asparagus_candidate[0].tolist(),
                                                top_left_y=actual_asparagus_candidate[1].tolist(),
                                                width=actual_asparagus_candidate[2].tolist(),
                                                high=actual_asparagus_candidate[3].tolist(),
                                                angle=angle)

                        detections.append(actual_asparagus_candidate)

        choose_final_candidates = ChooseFinalCandidates(detections, 5)
        final_candidates = choose_final_candidates.final_candidates

        return final_candidates

    @staticmethod
    def rotate_about_center(image, angle):
        w = image.shape[1]
        h = image.shape[0]
        # angle in radians
        rangle = np.deg2rad(angle)
        # now calculate new image width and height
        nw = abs(np.sin(rangle) * h) + abs(np.cos(rangle) * w)
        nh = abs(np.cos(rangle) * h) + abs(np.sin(rangle) * w)
        # ask OpenCV for the rotation matrix
        rot_mat = cv2.getRotationMatrix2D((nw * 0.5, nh * 0.5), angle, scale=1)
        # calculate the move from the old center to the new center combined
        # with the rotation
        rot_move = np.dot(rot_mat, np.array([(nw - w) * 0.5, (nh - h) * 0.5, 0]))
        # the move only affects the translation, so update the translation
        # part of the transform
        rot_mat[0, 2] += rot_move[0]
        rot_mat[1, 2] += rot_move[1]
        return cv2.warpAffine(image,
                              rot_mat,
                              (int(math.ceil(nw)), int(math.ceil(nh))),
                              flags=cv2.INTER_LANCZOS4)

    @staticmethod
    def calculate_original_coordinate_before_rotation(image, angle, vertex):
        point_numpy = np.array([[vertex[0]], [vertex[1]]])

        w_original = image.shape[1]
        h_original = image.shape[0]

        # now calculate new image width and height
        radian_angle = np.deg2rad(angle)  # angle in radians
        w_rotated = abs(np.sin(radian_angle) * h_original) + abs(np.cos(radian_angle) * w_original)
        h_rotated = abs(np.cos(radian_angle) * h_original) + abs(np.sin(radian_angle) * w_original)

        # From top left corner to central of image
        central_vector = np.array([[-w_rotated / 2], [-h_rotated / 2]])

        point_relative_to_central = point_numpy + central_vector

        # Rotation back
        theta = np.deg2rad(angle)
        rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)],
                                    [np.sin(theta), np.cos(theta)]])
        rotated_point_relative_to_central = np.dot(rotation_matrix, point_relative_to_central)

        # Central to top left corner
        top_left_central_point = rotated_point_relative_to_central - central_vector

        # Compensation with picture growth
        w_growth_on_one_side = (w_rotated - w_original) / 2
        h_growth_on_one_side = (h_rotated - h_original) / 2
        compensation_vector = np.array([[w_growth_on_one_side], [h_growth_on_one_side]])

        original_point = top_left_central_point - compensation_vector
        original_point_list = original_point.tolist()
        original_point_list_single_level = original_point_list[0] + original_point_list[1]

        return original_point_list_single_level
