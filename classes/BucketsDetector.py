from BucketMarkersDetector import BucketMarkersDetector
from Bucket import Bucket
from BucketNumbersCorrector import BucketNumbersCorrector
from BucketNumbersIdentifier2 import BucketNumbersIdentifier2


class BucketsDetector:
    def __init__(self,
                 bucket_marker_template,
                 bucket_marker_template_original_resolution,
                 template_matching_resolution,
                 max_bucket_number,
                 expected_template_matching_threshold,
                 numbers_folder,
                 number_matching_resolution):

        self.max_bucket_number = max_bucket_number
        bucket_number_identifier = BucketNumbersIdentifier2(numbers_folder,
                                                            number_matching_resolution,
                                                            max_bucket_number)

        self.bucket_markers_detector = \
            BucketMarkersDetector(bucket_marker_template=bucket_marker_template,
                                  bucket_marker_template_original_resolution=bucket_marker_template_original_resolution,
                                  template_matching_resolution=template_matching_resolution,
                                  expected_template_matching_threshold=expected_template_matching_threshold,
                                  bucket_number_identifier=bucket_number_identifier)

    def buckets_on_image(self, image):

        bucket_markers = self.bucket_markers(image)
        if not bucket_markers:
            return []

        corrected_bucket_numbers = self.corrected_bucket_numbers(bucket_markers)
        unique_bucket_numbers = self.unique_bucket_numbers(corrected_bucket_numbers)
        bucket_borders = self.bucket_borders(bucket_markers, image)
        buckets_on_image = []

        for i in range(0, len(bucket_borders)-1):
            actual_bucket = Bucket(start=bucket_borders[i],
                                   end=bucket_borders[i+1],
                                   bucket_number=unique_bucket_numbers[i])

            buckets_on_image.append(actual_bucket)

        return buckets_on_image

    def bucket_markers(self, image):
        bucket_markers = self.bucket_markers_detector.get_bucket_markers(image)
        return bucket_markers

    def corrected_bucket_numbers(self, bucket_markers):
        bucket_numbers = []
        for bucket_marker in bucket_markers:
            bucket_numbers.append([bucket_marker.left_bucket_number,
                                   bucket_marker.right_bucket_number])

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

    @staticmethod
    def bucket_borders(bucket_markers, image):
        bucket_borders = [0, image.shape[1]]

        for bucket_marker in bucket_markers:
            bucket_borders.insert(-1, bucket_marker.middle_x)

        return bucket_borders
