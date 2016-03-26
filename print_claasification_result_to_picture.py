__author__ = 'Henrik'
import numpy as np
import cv2
from matplotlib import pyplot as plt


def print_classification_result_to_picture(my_calss):
    for asparagus in my_calss.asparaguses:
        cv2.putText(my_calss.picture_with_modifications,
                    asparagus.classification,
                    (400, int(my_calss.picture_with_modifications.shape[0])),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    10,
                    255,
                    thickness = 20)


    return None