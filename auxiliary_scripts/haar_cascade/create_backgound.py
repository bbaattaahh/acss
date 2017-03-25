from moviepy.editor import *
import cv2
import numpy as np
import json


# PARAMS
with open('config/config-local.json') as json_data:
    config = json.load(json_data)

VIDEO_FILE = config["dropbox_folder_path"] + '/videos/live_test_2.avi'
BACKGROUND_IMAGE_FOLDER = config["dropbox_folder_path"] + '/haar_cascade/neg/'
BACKGROUND_DESCRIPTION_FILE = config["dropbox_folder_path"] + '/haar_cascade/bg.txt'

RESIZE_FACTOR = 0.5
t = np.arange(0, 30, 0.015)
i = 1

rot_90_factor = 1

clip = VideoFileClip(VIDEO_FILE)

with open(BACKGROUND_DESCRIPTION_FILE, "w") as text_file:
    for x in t:
        act_str = '00:00:' + str(x)
        act_frame_brg = clip.get_frame(act_str)
        act_frame_rgb = cv2.cvtColor(act_frame_brg, cv2.COLOR_BGR2RGB)

        act_frame_grey = cv2.cvtColor(act_frame_rgb, cv2.COLOR_BGR2GRAY)

        act_frame_grey_resized = cv2.resize(act_frame_grey,
                                            None,
                                            fx=RESIZE_FACTOR,
                                            fy=RESIZE_FACTOR,
                                            interpolation=cv2.INTER_CUBIC)

        filename = BACKGROUND_IMAGE_FOLDER + str(i) + ".jpg"
        rotated_image = np.rot90(act_frame_grey_resized)
        cv2.imwrite(filename, rotated_image)

        file_name_to_description_file = "neg/" + str(i) + ".jpg\n"
        text_file.write(file_name_to_description_file)

        i += 1

