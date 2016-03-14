__author__ = 'Henrik'
import numpy as np
import cv2
from matplotlib import pyplot as plt


def print_classification_result_to_picture(my_calss):
    for asparagus in my_calss.list_of_asparaguses:
        cv2.putText(my_calss.original_picture,
                    asparagus.classification,
                    (400, int(my_calss.original_picture.shape[0])),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    10,
                    255,
                    thickness = 20)


    return None