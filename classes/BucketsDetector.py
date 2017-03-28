from ImageResizer import ImageResizer
from BucketMarkersDetector import BucketMarkersDetector
from Bucket import Bucket
from PositionConverter import PositionConverter


class BucketsDetector:
    def __init__(self,
                 bucket_marker_template,
                 bucket_marker_template_original_resolution,
                 template_matching_resolution,
                 max_bucket_number):

        self.bucket_marker_template = bucket_marker_template
        self.bucket_marker_template_original_resolution = bucket_marker_template_original_resolution
        self.template_matching_resolution = template_matching_resolution
        self.max_bucket_number = max_bucket_number

        image_resizer = ImageResizer(image=bucket_marker_template,
                                     target_resolution=template_matching_resolution,
                                     parent_image_resolution=bucket_marker_template_original_resolution)
        self.template_to_detect_bucket_markers = image_resizer.resized_snipped_image

    def buckets_on_image(self, image):

        buckets_on_image = []

        for bucket_on_smaller_image in self.buckets_on_smaller_image(image):
            start_on_image = PositionConverter(
                original_position=[bucket_on_smaller_image.start, 0],
                original_resolution=self.image_to_detect_bucket_markers(image).shape[0:2],
                target_resolution=image.shape[0:2]).target_position[0]

            end_on_image = PositionConverter(original_position=[bucket_on_smaller_image.end, 0],
                                             original_resolution=self.image_to_detect_bucket_markers(image).shape[0:2],
                                             target_resolution=image.shape[0:2]).target_position[0]

            actual_bucket = Bucket(start=start_on_image,
                                   end=end_on_image,
                                   bucket_number=bucket_on_smaller_image.bucket_number)

            buckets_on_image.append(actual_bucket)

        return buckets_on_image

    def buckets_on_smaller_image(self, image):
        buckets = []

        detected_bucket_markers = BucketMarkersDetector(bucket_marker_template=self.template_to_detect_bucket_markers,
                                                        max_bucket_number=self.max_bucket_number)

        if len(detected_bucket_markers.bucket_marker_middle_x_positions(self.image_to_detect_bucket_markers(image))) == 0:
            return []

        bucket_x_borders = [0] + \
                           detected_bucket_markers.bucket_marker_middle_x_positions(self.image_to_detect_bucket_markers(image)) + \
                           [self.image_to_detect_bucket_markers(image).shape[1]]

        bucket_numbers_to_feed_for_loop = [[None, detected_bucket_markers.bucket_numbers(self.image_to_detect_bucket_markers(image))[0][0]]] + \
                                          detected_bucket_markers.bucket_numbers(self.image_to_detect_bucket_markers(image)) + \
                                          [[detected_bucket_markers.bucket_numbers(self.image_to_detect_bucket_markers(image))[-1][1], None]]

        for i in range(0, len(bucket_x_borders) - 1):
            actual_bucket = Bucket(start=bucket_x_borders[i],
                                   end=bucket_x_borders[i + 1],
                                   bucket_number=bucket_numbers_to_feed_for_loop[i][1])
            buckets.append(actual_bucket)

        return buckets

    def image_to_detect_bucket_markers(self, image):
        image_resizer = ImageResizer(image=image,
                                     target_resolution=self.template_matching_resolution)
        image_to_detect_bucket_markers = image_resizer.resized_snipped_image
        return image_to_detect_bucket_markers
