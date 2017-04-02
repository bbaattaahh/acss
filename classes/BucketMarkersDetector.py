from RGBTemplateMatcher import RGBTemplateMatcher
from SnipFromImage import SnipFromImage
from BucketNumbersIdentifier import BucketNumbersIdentifier
from BucketNumbersCorrector import BucketNumbersCorrector
from BucketMarker import BucketMarker
from Rectangle import Rectangle
from multiprocessing import Pool


class BucketMarkersDetector:

    always_seen_middle_part_rate = 0.2

    def __init__(self,
                 bucket_marker_template,
                 max_bucket_number,
                 expected_template_matching_threshold=2.3):

        self.bucket_marker_template = bucket_marker_template
        self.max_bucket_number = max_bucket_number

        width_from = int(bucket_marker_template.shape[1]*(0.5 - BucketMarkersDetector.always_seen_middle_part_rate/2))
        width_to = int(bucket_marker_template.shape[1]*(0.5 + BucketMarkersDetector.always_seen_middle_part_rate/2))
        self.always_seen_middle_template = bucket_marker_template[:, width_from:width_to, :]
        self.rgb_template_matcher = RGBTemplateMatcher(rgb_template=self.always_seen_middle_template,
                                                       threshold=expected_template_matching_threshold)
        self.bucket_number_identifier = BucketNumbersIdentifier()

    def bucket_numbers(self, image):
        bucket_numbers = []

        pool = Pool()
        bucket_markers = self.bucket_markers(image)
        results_left_buckets = pool.map(self.bucket_number_identifier.left_bucket_number, bucket_markers)
        results_right_buckets = pool.map(self.bucket_number_identifier.right_bucket_number, bucket_markers)

        for i in range(0, len(results_left_buckets)):
            bucket_numbers.append([results_left_buckets[i], results_right_buckets[i]])

        corrected_bucket_numbers = BucketNumbersCorrector(
                                        bucket_numbers=bucket_numbers,
                                        max_bucket_number=self.max_bucket_number).corrected_bucket_numbers

        return corrected_bucket_numbers

    def bucket_markers(self, image):
        template_height, template_width, _ = self.bucket_marker_template.shape

        bucket_markers = []

        for bucket_marker_top_left_corner in self.bucket_marker_top_left_corners(image):
            actual_bucket_marker = SnipFromImage(image=image,
                                                 x=bucket_marker_top_left_corner[0],
                                                 y=bucket_marker_top_left_corner[1],
                                                 w=template_width,
                                                 h=template_height).snipped_image

            bucket_markers.append(actual_bucket_marker)

        return bucket_markers

    def get_bucket_markers(self, image):
        bucket_markers = []

        for bounding_rectangle in self.get_bounding_rectangles(image):
            actual_bucket_marker = BucketMarker(image, bounding_rectangle)
            bucket_markers.append(actual_bucket_marker)

        return bucket_markers

    def get_bounding_rectangles(self, image):
        bounding_rectangles = []

        for bucket_marker_top_left_corner in self.bucket_marker_top_left_corners(image):
            actual_bounding_rectangle = Rectangle(top_left_x=bucket_marker_top_left_corner[0],
                                                  top_left_y=bucket_marker_top_left_corner[1],
                                                  width=self.bucket_marker_template.shape[1],
                                                  high=self.bucket_marker_template.shape[0])

            bounding_rectangles.append(actual_bounding_rectangle)

        return bounding_rectangles

    def bucket_marker_top_left_corners(self, image):
        always_seen_middle_template_half_width = int(self.always_seen_middle_template.shape[1] / 2)
        template_half_width = int(self.bucket_marker_template.shape[1] / 2)
        width_difference = template_half_width - always_seen_middle_template_half_width

        bucket_marker_top_left_corners = []

        for matching_middle_templates_position in self.matching_middle_templates_positions(image):
            bucket_marker_top_left_corners.append([matching_middle_templates_position[0] - width_difference,
                                                   matching_middle_templates_position[1]])

        return bucket_marker_top_left_corners

    def bucket_marker_middle_x_positions(self, image):
        always_seen_middle_template_half_width = int(self.always_seen_middle_template.shape[1] / 2)

        bucket_marker_middle_x_positions = []

        for matching_middle_templates_position in self.matching_middle_templates_positions(image):
            bucket_marker_middle_x_positions.append(matching_middle_templates_position[0]-always_seen_middle_template_half_width)

        return bucket_marker_middle_x_positions

    def matching_middle_templates_positions(self, image):
        return self.rgb_template_matcher.rectangle_top_left_vertices(image)
