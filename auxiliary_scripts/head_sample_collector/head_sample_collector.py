from moviepy.editor import *
import cv2
import json

from DetectAsparaguses import DetectAsparaguses
from OneAsparagusAnalysis import OneAsparagusAnalysis

# PARAMS
with open('config/config-local.json') as json_data:
    config = json.load(json_data)


STRECH_PARAMETER = 0.25
ROTATION_ANGLE = 15
MIN_AREA = 1

CASCADE_FILE = config["dropbox_folder_path"] + '/haar_cascade/data_whole_rotate/cascade.xml'
VIDEO_FILE = config["dropbox_folder_path"] + '/videos/live_test_2.avi'
RESULT_IMAGE_FOLDER = config["dropbox_folder_path"] + '/head_sample_collector/'


def is_asparagus(w, h, min_area):
    if h*w > min_area:
        return True

    return False


# this is the cascade we just made. Call what you want
asparagus_cascade = cv2.CascadeClassifier(CASCADE_FILE)

clip = VideoFileClip(VIDEO_FILE)

i = 0
for x in clip.iter_frames():

    act_frame_rgb = cv2.cvtColor(x, cv2.COLOR_BGR2RGB)

    detect_asparaguses = DetectAsparaguses(image = act_frame_rgb,
                                           cascade_file = CASCADE_FILE,
                                           detection_resolution=(120, 160),
                                           swing_angle=15)

    if len(detect_asparaguses.data_to_analysis_one_asparagus_images) <> 0:
        act_detection = detect_asparaguses.data_to_analysis_one_asparagus_images[0].image
        one_asparagus_analysis = OneAsparagusAnalysis(detect_asparaguses.data_to_analysis_one_asparagus_images[0])
        act_asparagus_enclosing_box_image = one_asparagus_analysis.asparagus_in_smallest_enclosing_box
        i += 1
        file_name = RESULT_IMAGE_FOLDER + str(i) + ".jpg"
        cv2.imwrite(file_name, act_asparagus_enclosing_box_image)

        # cv2.imshow('img', act_detection)
        # k = cv2.waitKey(30) & 0xff
        # if k == 27:
        #     break

cv2.destroyAllWindows()
