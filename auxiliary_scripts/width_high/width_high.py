from moviepy.editor import *
import cv2
import json
import numpy as np
import datetime

from BucketsDetector import BucketsDetector
from AsparagusesDetector import AsparagusesDetector
from OneAsparagusAnalyzer import OneAsparagusAnalyzer
from MergeBucketsAndAsparagusesPositions import MergeBucketsAndAsparagusPositions
from MeasurementsEvaulatorWidthHigh import MeasurementsEvaluatorWidthHigh
from DisplayClassification import DisplayClassification


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

asparaguses_detector = AsparagusesDetector(config["asparaguses_detector"]["cascade_file"],
                                           tuple(config["asparaguses_detector"]["detection_resolution"]),
                                           config["asparaguses_detector"]["swing_angle"])

one_asparagus_analyzer = OneAsparagusAnalyzer(asparagus_head_classifier=None)

measurements_evaluator = MeasurementsEvaluatorWidthHigh(
                                config["measurements_evaluator_width_high"]["minimum_repeated_measurement_number"],
                                config["measurements_evaluator_width_high"]["no_on_screen_time_before_display"],
                                config["measurements_evaluator_width_high"]["survive_time"])

displayer = DisplayClassification()

clip = VideoFileClip("/Users/h.bata/Dropbox/acss/videos/live_test_2.avi")
snip = clip.get_frame("00:00:18")
snip = cv2.cvtColor(snip, cv2.COLOR_BGR2RGB)
cv2.imwrite("snip.png", snip)

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

    start_asparagus_detection = datetime.datetime.now()
    data_to_analysis_one_asparagus_images = asparaguses_detector.data_to_analysis_one_asparagus_images(frame)
    end_asparagus_detection = datetime.datetime.now()
    print("Asparagus detection:")
    print(end_asparagus_detection - start_asparagus_detection)



    actual_asparaguses_bounding_rectangle = []
    actual_shape = []

    for data_to_analysis_one_asparagus_image in data_to_analysis_one_asparagus_images:
        actual_asparaguses_bounding_rectangle.append(data_to_analysis_one_asparagus_image.rectangle_on_original_image)
        frame = frame.copy()

        p1 = (int(data_to_analysis_one_asparagus_image.rectangle_on_original_image.top_left_x),
              int(data_to_analysis_one_asparagus_image.rectangle_on_original_image.top_left_y))
        p2 = (int(data_to_analysis_one_asparagus_image.rectangle_on_original_image.top_left_x + data_to_analysis_one_asparagus_image.rectangle_on_original_image.width),
              int(data_to_analysis_one_asparagus_image.rectangle_on_original_image.top_left_y + data_to_analysis_one_asparagus_image.rectangle_on_original_image.high))


        cv2.rectangle(frame,
                      p1,
                      p2,
                      (255, 0, 0),
                      2)
    #
    #     thickness = one_asparagus_analyzer.asparagus_thickness(data_to_analysis_one_asparagus_image.image)
    #     length = one_asparagus_analyzer.asparagus_length(data_to_analysis_one_asparagus_image.image)
    #
    #     actual_shape.append(str(thickness) + "___" + str(length))

    start_bucket_detection = datetime.datetime.now()
    buckets = buckets_detector.buckets_on_image(frame)
    end_bucket_detection = datetime.datetime.now()
    print("Bucket detection time:")
    print(end_bucket_detection - start_bucket_detection)


    if buckets:
        for bucket in buckets:
            frame[:, bucket.start, :] = 0
            print(bucket.bucket_number)

    bucket_markers = buckets_detector.bucket_markers(frame)
    if bucket_markers:
        bucket_marker_image = bucket_markers[0].bucket_marker_image
        cv2.imshow('bucket_marker', bucket_marker_image)

    # bucket_asparagus_pairs = MergeBucketsAndAsparagusPositions(buckets,
    #                                                            actual_asparaguses_bounding_rectangle,
    #                                                            actual_shape).bucket_asparagus_pairs

    # for bucket_asparagus_pair in bucket_asparagus_pairs:
    #     displayer.add_new_result(bucket_asparagus_pair[0], bucket_asparagus_pair[1])

    cv2.imshow('frame', frame)


    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

    end_1 = datetime.datetime.now()
    print("Loop time:")
    print(end_1 - start_1)

cv2.destroyAllWindows()
end = datetime.datetime.now()
# cap.release()

print(end - start)