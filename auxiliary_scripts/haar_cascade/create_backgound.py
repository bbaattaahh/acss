from moviepy.editor import *
import cv2
import numpy as np
import json


# PARAMS
with open('config/config-local.json') as json_data:
    config = json.load(json_data)

VIDEO_FILE = config["dropbox_folder_path"] + '/videos/live_test_2.avi'
VIDEO_FILE = '/Users/h.bata/Videos/acss/two_lamps/Video 6.mp4'

BACKGROUND_IMAGE_FOLDER = config["dropbox_folder_path"] + '/haar_cascade/neg/'
BACKGROUND_DESCRIPTION_FILE = config["dropbox_folder_path"] + '/haar_cascade/bg.txt'

RESIZE_FACTOR = 0.5
t = np.arange(0, 30, 0.015)
i = 1

rot_90_factor = 1

clip = VideoFileClip(VIDEO_FILE)
clip = VideoFileClip(VIDEO_FILE)


with open(BACKGROUND_DESCRIPTION_FILE, "w") as text_file:
    for x in clip.iter_frames():
        act_frame_brg = x
        act_frame_rgb = cv2.cvtColor(x, cv2.COLOR_BGR2RGB)

        act_frame_grey = cv2.cvtColor(act_frame_rgb, cv2.COLOR_BGR2GRAY)
        act_frame_grey = np.rot90(act_frame_grey)
        act_frame_grey_resized = cv2.resize(act_frame_grey,
                                            (90, 160),
                                            interpolation=cv2.INTER_CUBIC)

        filename = BACKGROUND_IMAGE_FOLDER + str(i) + ".jpg"
        cv2.imwrite(filename, act_frame_grey_resized)

        file_name_to_description_file = "neg/" + str(i) + ".jpg\n"
        text_file.write(file_name_to_description_file)

        i += 1

