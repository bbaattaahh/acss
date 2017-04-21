import pytesseract
import cv2
import re
import numpy as np
from PIL import Image

from RGBImageSlicer import RGBImageSlicer
from KeepNLargestAreaContours import KeepNLargestAreaContours


class BucketNumbersIdentifier2:

    def left_bucket_number(self, bucket_marker_image):
        rgb_image_slicer = RGBImageSlicer(bucket_marker_image)

        upper_number_image = rgb_image_slicer.first_quarter
        identified_upper_numbers = self.number_identification(upper_number_image)

        lower_number_image = rgb_image_slicer.third_quarter
        identified_lower_numbers = self.number_identification(lower_number_image)

        evaluated_identifications = self.evaluate_identifications(identified_upper_numbers,
                                                                  identified_lower_numbers)

        return evaluated_identifications

    def right_bucket_number(self, bucket_marker_image):
        rgb_image_slicer = RGBImageSlicer(bucket_marker_image)

        upper_number_image = rgb_image_slicer.second_quarter
        identified_upper_numbers = self.number_identification(upper_number_image)

        lower_number_image = rgb_image_slicer.fourth_quarter
        identified_lower_numbers = self.number_identification(lower_number_image)

        evaluated_identifications = self.evaluate_identifications(identified_upper_numbers,
                                                                  identified_lower_numbers)

        return evaluated_identifications

    @staticmethod
    def number_identification(image):
        processed_image = BucketNumbersIdentifier2.process_image(image)
        detected_numbers = BucketNumbersIdentifier2.do_number_recognition(processed_image)
        filtered_numbers = BucketNumbersIdentifier2.filter_out_not_digit_characters(detected_numbers)
        return filtered_numbers

    @staticmethod
    def evaluate_identifications(identification_1, identification_2):
        if len(identification_1) == 3 and len(identification_2) == 3 and identification_1 == identification_2:
            return identification_1

        if len(identification_1) == 3 and len(identification_2) != 3:
            return identification_1

        if len(identification_2) == 3 and len(identification_1) != 3:
            return identification_2

        return ""

    @staticmethod
    def process_image(image):
        gray_image = BucketNumbersIdentifier2.gray_image(image)
        narrowed_image = BucketNumbersIdentifier2.delete_top_and_lower_20_percent_of_image(gray_image)
        image_150_pixel_height = BucketNumbersIdentifier2.image_150_pixel_height(narrowed_image)
        blured_image = BucketNumbersIdentifier2.blur_image(image_150_pixel_height)
        thresholded_and_binarized_image = BucketNumbersIdentifier2.threshold_and_binarize_image(blured_image)
        closed_image = BucketNumbersIdentifier2.closed_image(thresholded_and_binarized_image)
        vanish_black_contours_beside_edges_image =\
            BucketNumbersIdentifier2.vanish_black_contours_beside_edges(closed_image)
        final_image = KeepNLargestAreaContours(image=vanish_black_contours_beside_edges_image,
                                               kept_contour_number=3,
                                               invert_flag=True).kept_n_largest_area_contours_image
        return final_image

    @staticmethod
    def do_number_recognition(image):
        pil_image = Image.fromarray(image)
        recognized_numbers = pytesseract.image_to_string(pil_image, config='-psm 7 -outputbase digits')
        # recognized_numbers = ""
        return recognized_numbers

    @staticmethod
    def filter_out_not_digit_characters(identified_numbers):
        filtered_numbers = re.sub("[^0-9]", "", identified_numbers)
        return filtered_numbers

    @staticmethod
    def gray_image(image):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return gray_image

    @staticmethod
    def delete_top_and_lower_20_percent_of_image(image):
        height, _ = image.shape
        narrowed_image = image[int(height * 0.2):int(height * 0.8), :]
        return narrowed_image

    @staticmethod
    def image_150_pixel_height(image):

        original_height, _ = image.shape

        target_height = 150.0
        scale_factor = target_height / original_height

        image_150_pixel_height = cv2.resize(image,
                                            None,
                                            fx=scale_factor,
                                            fy=scale_factor,
                                            interpolation=cv2.INTER_CUBIC)
        return image_150_pixel_height

    @staticmethod
    def blur_image(image):
        blured_image = cv2.GaussianBlur(image, (5, 5), 0)
        return blured_image

    @staticmethod
    def threshold_and_binarize_image(image):
        thresholded_and_binarized_image = cv2.adaptiveThreshold(image,
                                                                255,
                                                                cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                                                cv2.THRESH_BINARY,
                                                                37,
                                                                2)
        return thresholded_and_binarized_image

    @staticmethod
    def closed_image(image):
        kernel = np.ones((5, 5), np.uint8)
        closed_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
        return closed_image

    @staticmethod
    def vanish_black_contours_beside_edges(image):
        black_frame_image = BucketNumbersIdentifier2.set_img_frame_black(image)
        flood_filled_image = BucketNumbersIdentifier2.flood_fill_with_white_for_top_left_corner(black_frame_image)
        return flood_filled_image

    @staticmethod
    def set_img_frame_black(image):
        height, width = image.shape

        image[:, 0] = 0
        image[:, width - 1] = 0
        image[0, :] = 0
        image[height - 1, :] = 0

        return image

    @staticmethod
    def flood_fill_with_white_for_top_left_corner(image):
        height, width = image.shape
        mask = np.zeros((height + 2, width + 2), np.uint8)
        cv2.floodFill(image, mask, (0, 0), 255)
        return image
