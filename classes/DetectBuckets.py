import cv2
import pytesseract
from PIL import Image


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

    @staticmethod
    def do_number_recognition(image):
        pil_image = Image.fromarray(image)
        recognized_numbers = pytesseract.image_to_string(pil_image, config='-psm 7')
        return recognized_numbers

    def resize_image(self):

        target_height, target_width = self.template_matching_resolution
        height, width, _ = self.image.shape

        scale_factor_x = float(target_width) / width
        scale_factor_y = float(target_height) / height

        resize_image = cv2.resize(self.image,
                                  None,
                                  fx=scale_factor_x,
                                  fy=scale_factor_y,
                                  interpolation=cv2.INTER_CUBIC)
        return resize_image

    def resize_bucket_marker_template(self):
        original_height, original_width = self.bucket_marker_template_original_resolution
        template_matching_height, template_matching_width = self.template_matching_resolution
        bucket_marker_template_height, bucket_marker_template_width, _ = self.bucket_marker_template.shape

        target_height = bucket_marker_template_height * template_matching_height/original_height
        target_width = bucket_marker_template_width * template_matching_width/original_width

        scale_factor_x = float(target_width) / bucket_marker_template_width
        scale_factor_y = float(target_height) / bucket_marker_template_height

        resized_bucket_marker_template = cv2.resize(self.bucket_marker_template,
                                                    None,
                                                    fx=scale_factor_x,
                                                    fy=scale_factor_y,
                                                    interpolation=cv2.INTER_CUBIC)
        return resized_bucket_marker_template
