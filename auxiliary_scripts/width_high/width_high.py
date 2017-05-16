from moviepy.editor import *
import cv2
import json
import numpy as np
import datetime

from BucketsDetector import BucketsDetector
from AsparagusesDetector2 import AsparagusesDetector2
from OneAsparagusAnalyzer import OneAsparagusAnalyzer
from MergeBucketsAndAsparagusesPositionsWidthHigh import MergeBucketsAndAsparagusPositionsWidthHigh
from MeasurementsEvaulatorWidthHigh import MeasurementsEvaluatorWidthHigh
from DisplayClassification import DisplayClassification


def change_pixel_to_mm(measurement, mm_pixel_ratio):
    measurement = measurement * mm_pixel_ratio
    measurement = round(measurement, 1)
    return measurement

with open('./auxiliary_scripts/width_high/config_width_high.json') as data_file:
    config = json.load(data_file)


bucket_marker_template = cv2.imread(config["bucket_detector"]["template"])


buckets_detector = BucketsDetector(bucket_marker_template,
                                   tuple(config["bucket_detector"]["bucket_marker_template_original_resolution"]),
                                   tuple(config["bucket_detector"]["template_matching_resolution"]),
                                   config["bucket_detector"]["max_bucket_number"],
                                   config["bucket_detector"]["expected_template_matching_threshold"],
                                   config["bucket_detector"]["numbers_folder"],
                                   config["bucket_detector"]["number_matching_resolution"])

asparaguses_detector = AsparagusesDetector2(config["asparaguses_detector"]["global_threshold"],
                                            config["asparaguses_detector"]["high_width_ratio"],
                                            config["asparaguses_detector"]["minimum_area"],
                                            tuple(config["asparaguses_detector"]["detection_resolution"]),
                                            config["asparaguses_detector"]["extension_factor"])

one_asparagus_analyzer = OneAsparagusAnalyzer(asparagus_head_classifier=None)

measurements_evaluator = MeasurementsEvaluatorWidthHigh(
                                config["measurements_evaluator_width_high"]["minimum_repeated_measurement_number"],
                                config["measurements_evaluator_width_high"]["no_on_screen_time_before_display"],
                                config["measurements_evaluator_width_high"]["survive_time"])

mm_pixel_ratio = config["asparagus_classifier"]["millimeter_pixel_ratio"]

displayer = DisplayClassification()

clip = VideoFileClip("/Users/h.bata/Videos/acss/two_lamps/Video 8.mp4")

# cap = cv2.VideoCapture(0)
# cap.set(3, config["web_camera_distribution"][0])
# cap.set(4, config["web_camera_distribution"][1])

#while True:
start = datetime.datetime.now()

for x in clip.iter_frames():
    start_1 = datetime.datetime.now()
    #_, frame = cap.read()

    frame = cv2.cvtColor(x, cv2.COLOR_BGR2RGB)
    frame = np.array(np.rot90(frame, config["rotation_factor"]))

    # start_asparagus_detection = datetime.datetime.now()
    data_to_analysis_one_asparagus_images = asparaguses_detector.data_to_analysis_one_asparagus_images(frame)
    # end_asparagus_detection = datetime.datetime.now()
    # print("Asparagus detection:")
    # print(end_asparagus_detection - start_asparagus_detection)

    actual_width_high = []
    actual_asparaguses_bounding_rectangle = []

    for data_to_analysis_one_asparagus_image in data_to_analysis_one_asparagus_images:
        # box = cv2.boxPoints(data_to_analysis_one_asparagus_image.opencv_rectangle_on_original_image)
        # box = np.int0(box)
        # frame = frame.copy()
        # cv2.drawContours(frame, [box], 0, (0, 0, 255), 2)

        asparagus_contour = one_asparagus_analyzer.asparagus_contour(data_to_analysis_one_asparagus_image.image)

        # ac_small = cv2.resize(asparagus_contour, (0, 0), fx=0.3, fy=0.3)
        # cv2.imshow('ac', ac_small)

        raw_thickness = one_asparagus_analyzer.asparagus_thickness(asparagus_contour)
        thickness = change_pixel_to_mm(raw_thickness, mm_pixel_ratio)

        raw_length = one_asparagus_analyzer.asparagus_length(asparagus_contour)
        length = change_pixel_to_mm(raw_length, mm_pixel_ratio)

        actual_asparaguses_bounding_rectangle.append(data_to_analysis_one_asparagus_image.opencv_rectangle_on_original_image)
        actual_width_high.append([thickness, length])

    # start_bucket_detection = datetime.datetime.now()
    buckets = buckets_detector.buckets_on_image(frame)
    # end_bucket_detection = datetime.datetime.now()
    # print("Bucket detection time:")
    # print(end_bucket_detection - start_bucket_detection)


    # if buckets:
    #     for bucket in buckets:
    #         frame[:, bucket.start, :] = 0
    #         # print(bucket.bucket_number)

    bucket_markers = buckets_detector.bucket_markers(frame)
    # if bucket_markers:
    #     bucket_marker_image = bucket_markers[0].bucket_marker_image
    #     cv2.imshow('bucket_marker', bucket_marker_image)

    bucket_asparagus_pairs = MergeBucketsAndAsparagusPositionsWidthHigh(buckets,
                                                                        actual_asparaguses_bounding_rectangle,
                                                                        actual_width_high).bucket_asparagus_pairs

    if bucket_asparagus_pairs:
        print(bucket_asparagus_pairs)
        for bucket_asparagus_pair in bucket_asparagus_pairs:
            measurements_evaluator.add_measurement(bucket_number=bucket_asparagus_pair[0],
                                                   width=bucket_asparagus_pair[1][0],
                                                   high=bucket_asparagus_pair[1][1])

    else:
        print("No detection")



    small = cv2.resize(frame, (0, 0), fx=0.3, fy=0.3)
    cv2.imshow('frame', small)

    actual_raw_feed = measurements_evaluator.get_display_feed()

    if actual_raw_feed:
        # print(actual_raw_feed)
        width_high_data = str(actual_raw_feed[1]) + "    " + str(actual_raw_feed[2])
        displayer.add_new_result(actual_raw_feed[0], width_high_data)

    displayer.display_actual()


    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

    end_1 = datetime.datetime.now()
    #print("Loop time:")
    #print(end_1 - start_1)

cv2.destroyAllWindows()
end = datetime.datetime.now()
# cap.release()

print(end - start)
displayer.kill()
