import cv2
import numpy as np
import math

from Rectangle import Rectangle
from IsRectangleOnOriginalImage import IsRectangleOnOriginalImage
from AsparagusCandidate import AsparagusCandidate
from ChooseFinalCandidates import ChooseFinalCandidates


class DetectAsparaguses(object):

    def __init__(self,
                 image,
                 cascade_file,
                 detection_scale=0.25,
                 swing_angle=45):
        self.image = image
        self.cascade_file = cascade_file
        self.detection_scale = detection_scale
        self.swing_angle = swing_angle
        self.image_detection_on = self.image_detection_on()
        self.asparagus_candidates = self.get_asparagus_candidates()


    # def get_original_one_asparagus_images(self):
    #     images = []
    #     for candidate in self.asparagus_candidates:
    #         original_rotated_image = self.rotate_about_center


    def image_detection_on(self):
        grey_image = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
        rescaled_image = cv2.resize(grey_image,
                                    None,
                                    fx=self.detection_scale,
                                    fy=self.detection_scale,
                                    interpolation=cv2.INTER_CUBIC)
        return rescaled_image


    def get_asparagus_candidates(self):
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
                        actual_asparagus_candidate = AsparagusCandidate(top_left_x=actual_asparagus_candidate[0].tolist(),
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
        rangle = np.deg2rad(angle)  # angle in radians
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
