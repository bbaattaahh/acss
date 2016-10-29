from moviepy.editor import *
import cv2
import numpy as np
import json


# PARAMS
with open('config/config-local.json') as json_data:
    config = json.load(json_data)

STRECH_PARAMETER = 1
ROTATION_ANGLE = 15
MIN_AREA = 15000

CASCADE_FILE = config["dropbox_folder_path"] + '/haar_cascade/data_middle_part_05/cascade.xml'
VIDEO_FILE = config["dropbox_folder_path"] + '/videos/live_test_2.avi'
RESULT_IMAGE_FOLDER = config["dropbox_folder_path"] + '/haar_cascade/detected_asparaguses/'

def is_asparagus(w, h, min_area):
    if h*w > min_area:
        return True

    return False


# this is the cascade we just made. Call what you want
asparagus_cascade = cv2.CascadeClassifier(CASCADE_FILE)

clip = VideoFileClip(VIDEO_FILE)

t = np.arange(30,60,0.2)


i = 1

for x in t:
    act_str = '00:00:' + str(x)


    act_frame_brg = clip.get_frame(act_str)

    act_frame_brg = cv2.resize(act_frame_brg, None, fx=STRECH_PARAMETER, fy=STRECH_PARAMETER, interpolation=cv2.INTER_CUBIC)

    act_frame_rgb = cv2.cvtColor(act_frame_brg, cv2.COLOR_BGR2RGB)
    act_frame_grey = cv2.cvtColor(act_frame_rgb, cv2.COLOR_RGB2GRAY)

    # add this
    # image, reject levels level weights.
    asparaguses = asparagus_cascade.detectMultiScale(act_frame_grey, 3, 10)

    # add this
    for (x, y, w, h) in asparaguses:
        if is_asparagus(w, h, MIN_AREA):
            cv2.imwrite(RESULT_IMAGE_FOLDER + str(i) + ".jpg", act_frame_rgb[y:y + h, x:x + w, :])
            cv2.rectangle(act_frame_rgb, (x, y), (x + w, y + h), (255, 255, 0), 2)
            i += 1
            print "get one"


    cv2.imshow('img', act_frame_rgb)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cv2.destroyAllWindows()