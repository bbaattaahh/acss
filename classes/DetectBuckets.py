import cv2
import pytesseract
from PIL import Image


class DetectBuckets:
    def __init__(self,
                 image,
                 bucket_marker_image,
                 bucket_marker_image_original_resolution,
                 bucket_marker_dimensions_in_millimeter,
                 pixel_millimeter_ratio):

        self.image = image
        self.bucket_marker_image = bucket_marker_image
        self.bucket_marker_image_original_resolution = bucket_marker_image_original_resolution
        self.bucket_marker_dimensions_in_millimeter = bucket_marker_dimensions_in_millimeter
        self.pixel_millimeter_ratio = pixel_millimeter_ratio

    @staticmethod
    def do_number_recognition(image):
        pil_image = Image.fromarray(image)
        recognized_numbers = pytesseract.image_to_string(pil_image, config='-psm 7')
        return recognized_numbers

    @staticmethod
    def resize_image(image, target_height, target_width):

        height, width, _ = image.shape

        scale_factor_x = float(target_width) / width
        scale_factor_y = float(target_height) / height

        resize_image = cv2.resize(image,
                                  None,
                                  fx=scale_factor_x,
                                  fy=scale_factor_y,
                                  interpolation=cv2.INTER_CUBIC)
        return resize_image
