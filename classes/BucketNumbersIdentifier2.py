import cv2
import numpy as np
import glob

from RGBImageSlicer import RGBImageSlicer
from KeepNLargestAreaContours import KeepNLargestAreaContours
from SnipNLargestAreaContours import SnipNLargestAreaContours
from ImageResizer import ImageResizer


class BucketNumbersIdentifier2:
    def __init__(self,
                 numbers_folder,
                 number_matching_resolution=(50, 25),
                 max_bucket_number=110):

        self.number_matching_resolution = number_matching_resolution
        self.number_templates = self.get_number_templates(numbers_folder)
        self.max_bucket_number = max_bucket_number

    def get_number_templates(self, numbers_folder):
        number_images_file_names = glob.glob(numbers_folder + "/*")

        number_templates = []

        for number_images_file_name in number_images_file_names:
            actual_number_image = cv2.imread(number_images_file_name, flags=cv2.IMREAD_GRAYSCALE)
            actual_number_template = self.process_number(actual_number_image)
            number_templates.append(actual_number_template)

        return number_templates

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

    def number_identification(self, image):
        processed_image = self.process_image(image)
        # cv2.imwrite("processed_image.png", processed_image)
        number_images = SnipNLargestAreaContours(image=processed_image,
                                                 n=3,
                                                 invert_flag=True).n_largest_area_contours_images

        # cv2.imwrite("0.png", number_images[0])
        # cv2.imwrite("1.png", number_images[1])
        # cv2.imwrite("2.png", number_images[2])

        identified_number = ""
        for number_image in number_images:
            detected_number = self.do_number_recognition(number_image)
            # cv2.imwrite("actual.png", number_image)
            identified_number = identified_number + detected_number

        return identified_number

    def evaluate_identifications(self, identification_1, identification_2):
        if int(identification_1) > self.max_bucket_number:
            identification_1 = ""

        if int(identification_2) > self.max_bucket_number:
            identification_2 = ""

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

    def do_number_recognition(self, number_image):
        processed_number_image = self.process_number(number_image)
        max_same_pixel_number = 0
        max_same_pixel = 0
        for number in range(0, len(self.number_templates)):
            actual_same_pixel = sum(sum(self.number_templates[number] == processed_number_image))

            if actual_same_pixel > max_same_pixel:
                max_same_pixel = actual_same_pixel
                max_same_pixel_number = number

        str_max_same_pixel_number = str(max_same_pixel_number)

        return str_max_same_pixel_number

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

    def process_number(self, number_image):
        resized_image = ImageResizer(number_image,
                                     target_resolution=self.number_matching_resolution).resized_snipped_image
        return resized_image
