from moviepy.editor import *
import cv2
import json
import os

from DetectAsparaguses import DetectAsparaguses
from OneAsparagusAnalysis import OneAsparagusAnalysis
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
for actual_video_file in video_files:
    clip = VideoFileClip(actual_video_file)
    actual_basename = os.path.basename(actual_video_file)
    actual_class_name = os.path.splitext(actual_basename)[0]

    for x in clip.iter_frames():

        act_frame_rgb = cv2.cvtColor(x, cv2.COLOR_BGR2RGB)

        data_to_analysis_one_asparagus_images = DetectAsparaguses(
            image=act_frame_rgb,
            cascade_file=config["dropbox_folder_path"] + config["haar_cascade_file"],
            detection_resolution=(120, 160),
            swing_angle=15).data_to_analysis_one_asparagus_images

        if len(data_to_analysis_one_asparagus_images) != 0:
            for data_to_analysis_one_asparagus_image in data_to_analysis_one_asparagus_images:
                act_detection = OneAsparagusAnalysis(
                    data_to_analysis_one_asparagus_image).asparagus_in_smallest_enclosing_box
                act_top_part = AsparagusHeadImage(act_detection,
                                                  top_part_to_keep_ratio=0.15,
                                                  output_resolution=(50, 50)).resized_top_part

                if act_top_part.shape == (50, 50, 3):
                    i += 1
                    file_name = config["dropbox_folder_path"] \
                                + config["head_classification"]["head_pictures_folder"] \
                                + actual_class_name \
                                + "_" \
                                + str(i) \
                                + ".jpg"
                    cv2.imwrite(file_name, act_top_part)
                else:
                    print("Gebasz van")

                    # cv2.imshow('img', act_detection)
                    # k = cv2.waitKey(30) & 0xff
                    # if k == 27:
                    #     break

cv2.destroyAllWindows()
