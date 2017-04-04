import cv2
import json

from BucketsDetector import BucketsDetector
from AsparagusesDetector import AsparagusesDetector
from AsparagusClassifier import AsparagusClassifier
from AsparagusHeadClassifier import AsparagusHeadClassifier


__author__ = 'Henrik'

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

asparagus_classifier = AsparagusClassifier(config["asparagus_classifier"]["millimeter_pixel_ratio"],
                                           config["asparagus_classifier"]["classification_specification_file"])

asparagus_head_classifier = \
    AsparagusHeadClassifier(config["asparagus_head_classifier"]["neural_network_hierarchy_file"],
                            config["asparagus_head_classifier"]["neural_network_weights_file"],
                            config["asparagus_head_classifier"]["classification_labels"],
                            config["asparagus_head_classifier"]["top_part_to_keep_ratio"],
                            tuple(config["asparagus_head_classifier"]["head_classification_resolution"]))

cap = cv2.VideoCapture(0)
cap.set(3, config["web_camera_distribution"][0])
cap.set(4, config["web_camera_distribution"][1])

while True:
    _, frame = cap.read()

    cv2.imshow('frame', frame)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
