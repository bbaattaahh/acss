from RGBTemplateMatching import RGBTemplateMatching
from SnipFromImage import SnipFromImage
from BucketNumbersIdentifier import BucketNumbersIdentifier


class DetectBucketMarkers:

    always_seen_middle_part_rate = 0.2

    def __init__(self,
                 image,
                 bucket_marker_template):

        self.image = image
        self.bucket_marker_template = bucket_marker_template

    @property
    def bucket_numbers(self):
        bucket_numbers = []

        for bucket_marker in self.bucket_markers:
            bucket_number_identifier = BucketNumbersIdentifier(bucket_marker)
            bucket_numbers.append([bucket_number_identifier.left_bucket_number,
                                   bucket_number_identifier.right_bucket_number])

        return bucket_numbers

    @property
    def bucket_markers(self):
        template_height, template_width, _ = self.bucket_marker_template.shape

        bucket_markers = []

        for bucket_marker_top_left_corner in self.bucket_marker_top_left_corners:
            actual_bucket_marker = SnipFromImage(image=self.image,
                                                 x=bucket_marker_top_left_corner[0],
                                                 y=bucket_marker_top_left_corner[1],
                                                 w=template_width,
                                                 h=template_height).snipped_image

            bucket_markers.append(actual_bucket_marker)

        return bucket_markers

    @property
    def bucket_marker_top_left_corners(self):
        always_seen_middle_template_half_width = int(self.always_seen_middle_template.shape[1] / 2)
        template_half_width = int(self.bucket_marker_template.shape[1] / 2)
        width_difference = template_half_width - always_seen_middle_template_half_width

        bucket_marker_top_left_corners = []

        for matching_middle_templates_position in self.matching_middle_templates_positions:
            bucket_marker_top_left_corners.append([matching_middle_templates_position[0] - width_difference,
                                                   matching_middle_templates_position[1]])

        return bucket_marker_top_left_corners

    @property
    def matching_middle_templates_positions(self):
        rgb_template_matching = RGBTemplateMatching(rgb_image=self.image,
                                                    rgb_template=self.always_seen_middle_template,
                                                    threshold=2.3)
        return rgb_template_matching.rectangle_top_left_vertices

    @property
    def always_seen_middle_template(self):
        width_from = int(self.bucket_marker_template.shape[1]*(0.5-DetectBucketMarkers.always_seen_middle_part_rate/2))
        width_to = int(self.bucket_marker_template.shape[1]*(0.5+DetectBucketMarkers.always_seen_middle_part_rate/2))
        always_seen_middle_template = self.bucket_marker_template[:, width_from:width_to, :]
        return always_seen_middle_template
