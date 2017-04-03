from ImageResizer import ImageResizer
from RectangleResizer import RectangleResizer
from BucketMarkersDetector import BucketMarkersDetector
from Bucket import Bucket
from BucketNumbersCorrector import BucketNumbersCorrector


class BucketsDetector:
    def __init__(self,
                 bucket_marker_template,
                 bucket_marker_template_original_resolution,
                 template_matching_resolution,
                 max_bucket_number,
                 expected_template_matching_threshold=2.3):

        self.bucket_marker_template = bucket_marker_template
        self.bucket_marker_template_original_resolution = bucket_marker_template_original_resolution
        self.template_matching_resolution = template_matching_resolution
        self.max_bucket_number = max_bucket_number

        image_resizer = ImageResizer(image=bucket_marker_template,
                                     target_resolution=template_matching_resolution,
                                     parent_image_resolution=bucket_marker_template_original_resolution)
        self.template_to_detect_bucket_markers = image_resizer.resized_snipped_image
        self.bucket_markers_detector = \
            BucketMarkersDetector(bucket_marker_template=self.template_to_detect_bucket_markers,
                                  max_bucket_number=self.max_bucket_number,
                                  expected_template_matching_threshold=expected_template_matching_threshold)

    def buckets_on_image(self, image):

        bucket_markers_on_smaller_image = self.bucket_markers_on_smaller_image(image)
        if not bucket_markers_on_smaller_image:
            return []

        corrected_bucket_numbers = self.corrected_bucket_numbers(bucket_markers_on_smaller_image)
        unique_bucket_numbers = self.unique_bucket_numbers(corrected_bucket_numbers)
        bucket_borders = self.bucket_borders(bucket_markers_on_smaller_image, image)
        buckets_on_image = []

        for i in range(0, len(bucket_borders)-1):
            actual_bucket = Bucket(start=bucket_borders[i],
                                   end=bucket_borders[i+1],
                                   bucket_number=unique_bucket_numbers[i])

            buckets_on_image.append(actual_bucket)

        return buckets_on_image

    def bucket_markers_on_smaller_image(self, image):
        bucket_markers_on_smaller_image = self.bucket_markers_detector.get_bucket_markers(
                                                                            self.image_to_detect_bucket_markers(image))
        return bucket_markers_on_smaller_image

    def image_to_detect_bucket_markers(self, image):
        image_resizer = ImageResizer(image=image,
                                     target_resolution=self.template_matching_resolution)
        image_to_detect_bucket_markers = image_resizer.resized_snipped_image
        return image_to_detect_bucket_markers

    def corrected_bucket_numbers(self, bucket_markers_on_smaller_image):
        bucket_numbers = []
        for bucket_marker_on_smaller in bucket_markers_on_smaller_image:
            bucket_numbers.append([bucket_marker_on_smaller.left_bucket_number,
                                   bucket_marker_on_smaller.right_bucket_number])

        corrected_bucket_number = \
            BucketNumbersCorrector(bucket_numbers, self.max_bucket_number).corrected_bucket_numbers

        return corrected_bucket_number

    @staticmethod
    def unique_bucket_numbers(corrected_bucket_numbers):
        if corrected_bucket_numbers[0] == ["", ""]:
            no_valid_bucket_number_detected = [""] * (len(corrected_bucket_numbers) + 1)
            return no_valid_bucket_number_detected

        unique_bucket_numbers = []
        for bucket_number_pair in corrected_bucket_numbers:
            if bucket_number_pair[0] not in unique_bucket_numbers:
                unique_bucket_numbers.append(bucket_number_pair[0])
            if bucket_number_pair[1] not in unique_bucket_numbers:
                unique_bucket_numbers.append(bucket_number_pair[1])

        return unique_bucket_numbers

    def bucket_borders(self, bucket_markers_on_smaller_image, image):
        bucket_borders = [0, image.shape[1]]

        bucket_marker_bounding_rectangles_on_image = \
            self.bucket_marker_bounding_rectangles_on_original_image(bucket_markers_on_smaller_image, image)

        for rectangle in bucket_marker_bounding_rectangles_on_image:
            bucket_borders.insert(-1, rectangle.middle_x)

        return bucket_borders

    def bucket_marker_bounding_rectangles_on_original_image(self, bucket_markers_on_smaller_image, image):
        bucket_marker_bounding_rectangles_on_image = []
        rectangle_resizer = RectangleResizer(original_resolution=self.template_matching_resolution,
                                             target_resolution=image.shape[:2])

        for bucket_marker_on_smaller_image in bucket_markers_on_smaller_image:
            bucket_bounding_rectangle_on_smaller_image = bucket_marker_on_smaller_image.bounding_rectangle
            bucket_marker_bounding_rectangle_on_image = \
                rectangle_resizer.resize(bucket_bounding_rectangle_on_smaller_image)
            bucket_marker_bounding_rectangles_on_image.append(bucket_marker_bounding_rectangle_on_image)

        return bucket_marker_bounding_rectangles_on_image
