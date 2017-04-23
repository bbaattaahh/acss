from RGBTemplateMatcher import RGBTemplateMatcher
from BucketMarker import BucketMarker
from Rectangle import Rectangle
from ImageResizer import ImageResizer
from PositionConverter import PositionConverter


class BucketMarkersDetector:

    always_seen_middle_part_rate = 0.2

    def __init__(self,
                 bucket_marker_template,
                 bucket_marker_template_original_resolution,
                 template_matching_resolution,
                 expected_template_matching_threshold,
                 bucket_number_identifier):

        self.bucket_marker_template = bucket_marker_template
        self.bucket_marker_template_original_resolution = bucket_marker_template_original_resolution
        self.template_matching_resolution = template_matching_resolution

        image_resizer = ImageResizer(image=bucket_marker_template,
                                     target_resolution=template_matching_resolution,
                                     parent_image_resolution=bucket_marker_template_original_resolution)
        self.template_to_detect_bucket_markers = image_resizer.resized_snipped_image

        width_from = int(self.template_to_detect_bucket_markers.shape[1]*(0.5 - BucketMarkersDetector.always_seen_middle_part_rate/2))
        width_to = int(self.template_to_detect_bucket_markers.shape[1]*(0.5 + BucketMarkersDetector.always_seen_middle_part_rate/2))
        self.always_seen_middle_template = self.template_to_detect_bucket_markers[:, width_from:width_to, :]
        self.rgb_template_matcher = RGBTemplateMatcher(rgb_template=self.always_seen_middle_template,
                                                       threshold=expected_template_matching_threshold)
        self.bucket_number_identifier = bucket_number_identifier

    def get_bucket_markers(self, image):
        image_to_detection_on = self.image_to_detect_bucket_markers(image)

        matching_middle_templates_positions_on_smaller_image = \
            self.matching_middle_templates_positions(image_to_detection_on)

        bucket_marker_top_left_corners_on_smaller_image = \
            self.bucket_marker_top_left_corners(matching_middle_templates_positions_on_smaller_image)

        bucket_marker_top_left_corners_on_original_image = \
            self.convert_bucket_marker_top_left_corners_to_original_image(
                bucket_marker_top_left_corners_on_smaller_image,
                image_shape=image.shape[:2])

        bounding_rectangles = self.get_bounding_rectangles(bucket_marker_top_left_corners_on_original_image)

        bucket_markers = []

        for bounding_rectangle in bounding_rectangles:
            actual_bucket_marker = BucketMarker(image, bounding_rectangle, self.bucket_number_identifier)
            bucket_markers.append(actual_bucket_marker)

        return bucket_markers

    def image_to_detect_bucket_markers(self, image):
        image_resizer = ImageResizer(image=image,
                                     target_resolution=self.template_matching_resolution)
        image_to_detect_bucket_markers = image_resizer.resized_snipped_image
        return image_to_detect_bucket_markers

    def matching_middle_templates_positions(self, image):
        return self.rgb_template_matcher.rectangle_top_left_vertices(image)

    def bucket_marker_top_left_corners(self, matching_middle_templates_positions):
        always_seen_middle_template_half_width = int(self.always_seen_middle_template.shape[1] / 2)
        template_half_width = int(self.template_to_detect_bucket_markers.shape[1] / 2)
        width_difference = template_half_width - always_seen_middle_template_half_width

        bucket_marker_top_left_corners = []

        for matching_middle_templates_position in matching_middle_templates_positions:
            bucket_marker_top_left_corners.append([matching_middle_templates_position[0] - width_difference,
                                                   matching_middle_templates_position[1]])

        return bucket_marker_top_left_corners

    def convert_bucket_marker_top_left_corners_to_original_image(self, positions, image_shape):
        original_positions = []
        for position in positions:
            actual_original_position = PositionConverter(tuple(position),
                                                         original_resolution=self.template_matching_resolution,
                                                         target_resolution=image_shape).target_position
            actual_original_position = list(actual_original_position)
            original_positions.append(actual_original_position)

        return original_positions

    def get_bounding_rectangles(self, bucket_marker_top_left_corners):
        bounding_rectangles = []

        for bucket_marker_top_left_corner in bucket_marker_top_left_corners:
            actual_bounding_rectangle = Rectangle(top_left_x=bucket_marker_top_left_corner[0],
                                                  top_left_y=bucket_marker_top_left_corner[1],
                                                  width=self.bucket_marker_template.shape[1],
                                                  high=self.bucket_marker_template.shape[0])

            bounding_rectangles.append(actual_bounding_rectangle)

        return bounding_rectangles
