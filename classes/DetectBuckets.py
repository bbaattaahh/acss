import cv2

from ImageResizer import ImageResizer
from DetectBucketMarkers import DetectBucketMarkers
from Bucket import Bucket


class DetectBuckets:

    def __init__(self,
                 image,
                 bucket_marker_template,
                 bucket_marker_template_original_resolution,
                 template_matching_resolution):

        self.image = image
        self.bucket_marker_template = bucket_marker_template
        self.bucket_marker_template_original_resolution = bucket_marker_template_original_resolution
        self.template_matching_resolution = template_matching_resolution

    #todo
    # def buckets_on_smaller_image(self):
    #     buckets = []
    #
    #     detected_bucket_markers = DetectBucketMarkers(image=self.image_to_detect_bucket_markers,
    #                                                   bucket_marker_template=self.template_to_detect_bucket_markers)
    #
    #     bucket_x_borders = [0,
    #                         detected_bucket_markers.bucket_marker_middle_x_positions,
    #                         self.image_to_detect_bucket_markers.shape[1]]
    #
    #     bucket_numbers_to_for_for_loop = [[None, detected_bucket_markers.bucket_numbers[0][0]],
    #                                        detected_bucket_markers.bucket_numbers,
    #                                        detected_bucket_markers.bucket_numbers[-1][1], None]
    #
    #     for i in range(0, len(bucket_x_borders)-1):
    #         actual_bucket = Bucket(start=bucket_x_borders[i],
    #                                end=bucket_x_borders[i+1],
    #                                bucket_number=None)
    #
    #     return detected_bucket_markers

    @property
    def image_to_detect_bucket_markers(self):
        image_resizer = ImageResizer(image=self.image,
                                     target_resolution=self.template_matching_resolution)
        image_to_detect_bucket_markers = image_resizer.resized_image
        return image_to_detect_bucket_markers

    @property
    def template_to_detect_bucket_markers(self):
        image_resizer = ImageResizer(image=self.bucket_marker_template,
                                     target_resolution=self.template_matching_resolution,
                                     parent_image_resolution=self.bucket_marker_template_original_resolution)
        template_to_detect_bucket_markers = image_resizer.resized_image
        return template_to_detect_bucket_markers
