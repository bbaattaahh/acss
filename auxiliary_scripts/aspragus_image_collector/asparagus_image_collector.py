from moviepy.editor import *
import cv2
import json
import numpy as np

from AsparagusesDetector import AsparagusesDetector
from OneAsparagusAnalyzer import OneAsparagusAnalyzer
from AsparagusHeadImage import AsparagusHeadImage

with open('config/config-local.json') as json_data:
    config = json.load(json_data)


def get_video_file_names(config):
    video_file_names = []
    for actual_video_file_name in config["head_classification"]["videos"]:
        actual_full_name = config["dropbox_folder_path"] + actual_video_file_name
        video_file_names.append(actual_full_name)

    return video_file_names


i = 0

video_files = get_video_file_names(config)
# video_files = "/Users/h.bata/Videos/acss/two_lamps/Video 1.mp4"
class_labels = config["head_classification"]["class_labels"]

rotation_factor = 1
asparaguses_detector = AsparagusesDetector(cascade_file=config["dropbox_folder_path"] + config["haar_cascade_file"],
                                           detection_resolution=(160, 120),
                                           swing_angle=45)



for j in range(0, len(video_files)):
    clip = VideoFileClip(video_files[j])
    actual_class_name = class_labels[j]

    for x in clip.iter_frames():

        act_frame_rgb = cv2.cvtColor(x, cv2.COLOR_BGR2RGB)
        act_frame_rgb = np.rot90(act_frame_rgb, rotation_factor)

        data_to_analysis_one_asparagus_images = \
            asparaguses_detector.data_to_analysis_one_asparagus_images(act_frame_rgb)

        if len(data_to_analysis_one_asparagus_images) != 0:
            for data_to_analysis_one_asparagus_image in data_to_analysis_one_asparagus_images:

                i = i + 1

                act_detection = OneAsparagusAnalyzer(None).asparagus_in_smallest_enclosing_box(data_to_analysis_one_asparagus_image.image)

                file_name = config["dropbox_folder_path"] \
                            + config["head_classification"]["asparagus_pictures_folder"] \
                            + actual_class_name \
                            + "_" \
                            + str(i) \
                            + ".jpg"
                cv2.imwrite(file_name, data_to_analysis_one_asparagus_image.image)

        cv2.imshow('img', act_frame_rgb)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

cv2.destroyAllWindows()
