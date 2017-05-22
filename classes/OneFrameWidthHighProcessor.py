import json
import cv2

from BucketsDetector import BucketsDetector
from AsparagusesDetector2 import AsparagusesDetector2
from OneAsparagusAnalyzer import OneAsparagusAnalyzer
from MergeBucketsAndAsparagusesPositionsWidthHigh import MergeBucketsAndAsparagusPositionsWidthHigh


class OneFrameWidthHighProcessor(object):
    def __init__(self,
                 config_file):

        with open(config_file) as data_file:
            config = json.load(data_file)

        bucket_marker_template = cv2.imread(config["bucket_detector"]["template"])

        self.buckets_detector = BucketsDetector(bucket_marker_template,
                                           tuple(
                                               config["bucket_detector"]["bucket_marker_template_original_resolution"]),
                                           tuple(config["bucket_detector"]["template_matching_resolution"]),
                                           config["bucket_detector"]["max_bucket_number"],
                                           config["bucket_detector"]["expected_template_matching_threshold"],
                                           config["bucket_detector"]["numbers_folder"],
                                           config["bucket_detector"]["number_matching_resolution"])

        self.asparaguses_detector = AsparagusesDetector2(
                                                config["asparaguses_detector"]["global_threshold"],
                                                config["asparaguses_detector"]["high_width_ratio"],
                                                config["asparaguses_detector"]["minimum_area"],
                                                tuple(config["asparaguses_detector"]["detection_resolution"]),
                                                config["asparaguses_detector"]["vertical_extension_factor"],
                                                config["asparaguses_detector"]["horizontal_extension_factor"])

        self.one_asparagus_analyzer = OneAsparagusAnalyzer(asparagus_head_classifier=None)
        self.mm_pixel_ratio = config["asparagus_classifier"]["millimeter_pixel_ratio"]

    def process_frame(self, frame):

        data_to_analysis_one_asparagus_images = self.asparaguses_detector.data_to_analysis_one_asparagus_images(frame)

        actual_width_high = []
        actual_asparaguses_bounding_rectangle = []

        for data_to_analysis_one_asparagus_image in data_to_analysis_one_asparagus_images:

            asparagus_contour = self.one_asparagus_analyzer.asparagus_contour(data_to_analysis_one_asparagus_image.image)

            raw_thickness = self.one_asparagus_analyzer.asparagus_thickness(asparagus_contour)
            thickness = self.change_pixel_to_mm(raw_thickness)

            raw_length = self.one_asparagus_analyzer.asparagus_length(asparagus_contour)
            length = self.change_pixel_to_mm(raw_length)

            actual_asparaguses_bounding_rectangle.append(
                data_to_analysis_one_asparagus_image.opencv_rectangle_on_original_image)
            actual_width_high.append([thickness, length])

        buckets = self.buckets_detector.buckets_on_image(frame)

        bucket_asparagus_pairs = MergeBucketsAndAsparagusPositionsWidthHigh(buckets,
                                                                            actual_asparaguses_bounding_rectangle,
                                                                            actual_width_high).bucket_asparagus_pairs

        return bucket_asparagus_pairs

    def change_pixel_to_mm(self, measurement):
        measurement = measurement * self.mm_pixel_ratio
        measurement = round(measurement, 1)
        return measurement
