from moviepy.editor import *
import cv2
import json
import numpy as np

from BucketsDetector import BucketsDetector
from AsparagusesDetector import AsparagusesDetector
from OneAsparagusAnalyzer import OneAsparagusAnalyzer
from AsparagusClassifier import AsparagusClassifier
from AsparagusHeadClassifier import AsparagusHeadClassifier
from MergeBucketsAndAsparagusesPositions import MergeBucketsAndAsparagusPositions
from DisplayClassification import DisplayClassification

with open('./config/config-local.json') as data_file:
    config = json.load(data_file)

bucket_marker_template = cv2.imread(config["bucket_detector"]["template"])


buckets_detector = BucketsDetector(bucket_marker_template,
                                   tuple(config["bucket_detector"]["bucket_marker_template_original_resolution"]),
                                   tuple(config["bucket_detector"]["template_matching_resolution"]),
                                   config["bucket_detector"]["max_bucket_number"],
                                   config["bucket_detector"]["expected_template_matching_threshold"])

asparaguses_detector = AsparagusesDetector(config["asparaguses_detector"]["cascade_file"],
                                           tuple(config["asparaguses_detector"]["detection_resolution"]),
                                           config["asparaguses_detector"]["swing_angle"])




one_asparagus_analyzer = OneAsparagusAnalyzer(asparagus_head_classifier=None)

displayer = DisplayClassification()

clip = VideoFileClip("/Users/h.bata/Videos/acss/two_lamps/Video 6.mp4")
snip = clip.get_frame("00:00:18")
snip = cv2.cvtColor(snip, cv2.COLOR_BGR2RGB)
cv2.imwrite("snip.png", snip)

ROTATION_FACTOR = 1

# cap = cv2.VideoCapture(0)
# cap.set(3, config["web_camera_distribution"][0])
# cap.set(4, config["web_camera_distribution"][1])

#while True:
for x in clip.iter_frames():

    #_, frame = cap.read()


    frame = cv2.cvtColor(x, cv2.COLOR_BGR2RGB)
    frame = np.rot90(frame, ROTATION_FACTOR)
    cv2.imshow('frame', frame)
    data_to_analysis_one_asparagus_images = asparaguses_detector.data_to_analysis_one_asparagus_images(frame)

    # if not data_to_analysis_one_asparagus_images:
    #     continue
    #
    actual_asparaguses_bounding_rectangle = []
    actual_shape = []
    for data_to_analysis_one_asparagus_image in data_to_analysis_one_asparagus_images:
        actual_asparaguses_bounding_rectangle.append(data_to_analysis_one_asparagus_image.rectangle_on_original_image)
        # asparagus = one_asparagus_analyzer.asparagus(data_to_analysis_one_asparagus_image.image)
        thickness = one_asparagus_analyzer.asparagus_thickness(data_to_analysis_one_asparagus_image.image)
        length = one_asparagus_analyzer.asparagus_length(data_to_analysis_one_asparagus_image.image)

        actual_shape.append(str(thickness) + "___" + str(length))

    buckets = buckets_detector.buckets_on_image(frame)

    bucket_asparagus_pairs = MergeBucketsAndAsparagusPositions(buckets,
                                                               actual_asparaguses_bounding_rectangle,
                                                               actual_shape).bucket_asparagus_pairs

    for bucket_asparagus_pair in bucket_asparagus_pairs:
        displayer.add_new_result(bucket_asparagus_pair[0], bucket_asparagus_pair[1])

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break


cv2.destroyAllWindows()
# cap.release()
