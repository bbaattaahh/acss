import cv2

from ImageResizer import ImageResizer
from DetectBucketMarkers import DetectBucketMarkers
from BucketNumbersIdentifier import BucketNumbersIdentifier


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

    def bucket_markers(self):
        detected_bucket_markers = DetectBucketMarkers(image=self.image_to_detect_bucket_markers,
                                                      bucket_marker_template=self.template_to_detect_bucket_markers)
        return detected_bucket_markers

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
