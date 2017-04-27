from moviepy.editor import *
import cv2
import numpy as np
import json
import numpy as np

from Rectangle import Rectangle



# PARAMS
with open('config/config-local.json') as json_data:
    config = json.load(json_data)


MIN_AREA = 1
ROTATION_FACTOR = 1

CASCADE_FILE = config["dropbox_folder_path"] + '/haar_cascade/data_whole_rotate/cascade.xml'
CASCADE_FILE = config["dropbox_folder_path"] + '/haar_cascade/data_vertical/cascade.xml'
CASCADE_FILE = "/Users/h.bata/opencv_work_space/data/cascade.xml"
VIDEO_FILE = config["dropbox_folder_path"] + '/videos/live_test_2.avi'
VIDEO_FILE = "/Users/h.bata/Videos/acss/two_lamps/Video 1.mp4"
RESULT_IMAGE_FOLDER = config["dropbox_folder_path"] + '/haar_cascade/detected_asparaguses/'


def is_asparagus(w, h, min_area):
    if h*w > min_area:
        return True

    return False


# this is the cascade we just made. Call what you want
asparagus_cascade = cv2.CascadeClassifier(CASCADE_FILE)

clip = VideoFileClip(VIDEO_FILE)


clip = VideoFileClip(VIDEO_FILE)
i = 1

for act_frame_brg in clip.iter_frames():

    act_frame_brg = np.rot90(act_frame_brg, ROTATION_FACTOR)

    act_frame_brg = cv2.resize(act_frame_brg,
                               (180, 320),
                               interpolation=cv2.INTER_CUBIC)

    act_frame_rgb = cv2.cvtColor(act_frame_brg, cv2.COLOR_BGR2RGB)
    act_frame_grey = cv2.cvtColor(act_frame_rgb, cv2.COLOR_RGB2GRAY)

    # add this
    # image, reject levels level weights.
    asparaguses = asparagus_cascade.detectMultiScale(act_frame_grey, 4, 31)

    # add this
    for (x, y, w, h) in asparaguses:
        act_rectangle = Rectangle(x, y, w, h)
        cv2.rectangle(act_frame_rgb, (x, y), (x + w, y + h), (255, 255, 0), 2)
        act_rectangle = Rectangle(x, y, w, h)
        i += 1

        print ("get one")

    cv2.imshow('img', act_frame_rgb)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cv2.destroyAllWindows()
