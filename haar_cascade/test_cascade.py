from moviepy.editor import *
import cv2
import numpy as np
import json
import math

from Rectangle import Rectangle
from IsRectangleOnOriginalImage import IsRectangleOnOriginalImage


# PARAMS
with open('config/config-local.json') as json_data:
    config = json.load(json_data)


STRECH_PARAMETER = 0.25
ROTATION_ANGLE = 15
MIN_AREA = 1

CASCADE_FILE = config["dropbox_folder_path"] + '/haar_cascade/data_whole_rotate/cascade.xml'
VIDEO_FILE = config["dropbox_folder_path"] + '/videos/live_test_2.avi'
RESULT_IMAGE_FOLDER = config["dropbox_folder_path"] + '/haar_cascade/detected_asparaguses/'


def is_asparagus(w, h, min_area):
    if h*w > min_area:
        return True

    return False


def rotate_about_center(src, angle, scale=1.):
    w = src.shape[1]
    h = src.shape[0]
    rangle = np.deg2rad(angle)  # angle in radians
    # now calculate new image width and height
    nw = (abs(np.sin(rangle)*h) + abs(np.cos(rangle)*w))*scale
    nh = (abs(np.cos(rangle)*h) + abs(np.sin(rangle)*w))*scale
    # ask OpenCV for the rotation matrix
    rot_mat = cv2.getRotationMatrix2D((nw*0.5, nh*0.5), angle, scale)
    # calculate the move from the old center to the new center combined
    # with the rotation
    rot_move = np.dot(rot_mat, np.array([(nw-w)*0.5, (nh-h)*0.5,0]))
    # the move only affects the translation, so update the translation
    # part of the transform
    rot_mat[0,2] += rot_move[0]
    rot_mat[1,2] += rot_move[1]
    return cv2.warpAffine(src, rot_mat, (int(math.ceil(nw)), int(math.ceil(nh))), flags=cv2.INTER_LANCZOS4)


# this is the cascade we just made. Call what you want
asparagus_cascade = cv2.CascadeClassifier(CASCADE_FILE)

clip = VideoFileClip(VIDEO_FILE)

t = np.arange(30, 60, 0.2)


i = 1

for x in t:
    act_str = '00:00:' + str(x)

    act_frame_brg = clip.get_frame(act_str)

    act_frame_brg = cv2.resize(act_frame_brg,
                               None,
                               fx=STRECH_PARAMETER,
                               fy=STRECH_PARAMETER,
                               interpolation=cv2.INTER_CUBIC)

    act_frame_rgb = cv2.cvtColor(act_frame_brg, cv2.COLOR_BGR2RGB)
    act_frame_grey = cv2.cvtColor(act_frame_rgb, cv2.COLOR_RGB2GRAY)

    # add this
    # image, reject levels level weights.
    for angle in range(-45, 45):

        rotated_act_frame_grey = rotate_about_center(act_frame_grey, angle)
        ratated_act_frame_rgb = rotate_about_center(act_frame_rgb, angle)

        asparaguses = asparagus_cascade.detectMultiScale(rotated_act_frame_grey, 4, 31)

        # add this
        for (x, y, w, h) in asparaguses:
            act_rectangle = Rectangle(x, y, w, h)
            isRectangleOnOriginalImage = IsRectangleOnOriginalImage(act_frame_grey,
                                                                    act_rectangle,
                                                                    angle)
            # if (is_asparagus(w, h, MIN_AREA) and is_rectangle_on_original_image(rectangle=act_rectangle,
            #                                                                    original_image=act_frame_grey,
            #                                                                    rotated_image=rotated_act_frame_grey,
            #                                                                    angle=angle)):
            if isRectangleOnOriginalImage.is_it:
                cv2.imwrite(RESULT_IMAGE_FOLDER + str(i) + ".jpg", ratated_act_frame_rgb[y:y + h, x:x + w, :])
                cv2.rectangle(ratated_act_frame_rgb, (x, y), (x + w, y + h), (255, 255, 0), 2)
                act_rectangle = Rectangle(x, y, w, h)
                i += 1

                print "get one"


        cv2.imshow('img', ratated_act_frame_rgb)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

cv2.destroyAllWindows()
