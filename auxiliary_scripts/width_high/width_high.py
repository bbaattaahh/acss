import cv2
import json

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


asparagus_classifier = AsparagusClassifier(config["asparagus_classifier"]["millimeter_pixel_ratio"],
                                           config["asparagus_classifier"]["classification_specification_file"])

asparagus_head_classifier = \
    AsparagusHeadClassifier(config["asparagus_head_classifier"]["neural_network_hierarchy_file"],
                            config["asparagus_head_classifier"]["neural_network_weights_file"],
                            config["asparagus_head_classifier"]["classification_labels"],
                            config["asparagus_head_classifier"]["top_part_to_keep_ratio"],
                            tuple(config["asparagus_head_classifier"]["head_classification_resolution"]))

one_asparagus_analyzer = OneAsparagusAnalyzer(asparagus_head_classifier)

displayer = DisplayClassification()

cap = cv2.VideoCapture(0)
cap.set(3, config["web_camera_distribution"][0])
cap.set(4, config["web_camera_distribution"][1])

while True:
    _, frame = cap.read()

    cv2.imshow('frame', frame)
    data_to_analysis_one_asparagus_images = asparaguses_detector.data_to_analysis_one_asparagus_images(frame)

    if not data_to_analysis_one_asparagus_images:
        continue

    actual_asparaguses_bounding_rectangle = []
    actual_asparagus_classes = []
    for data_to_analysis_one_asparagus_image in data_to_analysis_one_asparagus_images:
        actual_asparaguses_bounding_rectangle.append(data_to_analysis_one_asparagus_image.rectangle_on_original_image)
        asparagus = one_asparagus_analyzer.asparagus(data_to_analysis_one_asparagus_image.image)
        actual_asparagus_classes.append(asparagus_classifier.classify(asparagus))

    buckets = buckets_detector.buckets_on_image(frame)

    bucket_asparagus_pairs = MergeBucketsAndAsparagusPositions(buckets, actual_asparaguses_bounding_rectangle, actual_asparagus_classes).bucket_asparagus_pairs

    for bucket_asparagus_pair in bucket_asparagus_pairs:
        displayer.add_new_result(bucket_asparagus_pair[0], bucket_asparagus_pair[1])

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break


cv2.destroyAllWindows()
cap.release()
