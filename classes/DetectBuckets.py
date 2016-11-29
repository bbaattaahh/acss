import cv2
import pytesseract
from PIL import Image

from RGBTemplateMatching import RGBTemplateMatching


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

    @property
    def detected_bucket_markers(self):
        rgb_template_matching = RGBTemplateMatching(rgb_image=self.resized_image,
                                                    rgb_template=self.resized_bucket_marker_template,
                                                    threshold=2.3)

        back_scaled_rectangle_top_left_vertices = self.scale_bucket_marker_matches(
                                                            rgb_template_matching.rectangle_top_left_vertices)

        return back_scaled_rectangle_top_left_vertices

    def scale_bucket_marker_matches(self, rectangle_top_left_vertices):
        back_scaled_vertices = []
        image_scale_factor_y, image_scale_factor_x = self.image_scale_factors

        for rectangle_top_left_vertex in rectangle_top_left_vertices:
            actual_back_scaled_x = rectangle_top_left_vertex[0]/image_scale_factor_x
            actual_back_scaled_y = rectangle_top_left_vertex[1]/image_scale_factor_y
            back_scaled_vertices.append([actual_back_scaled_x, actual_back_scaled_y])

        return back_scaled_vertices


    @staticmethod
    def do_number_recognition(image):
        pil_image = Image.fromarray(image)
        recognized_numbers = pytesseract.image_to_string(pil_image, config='-psm 7')
        return recognized_numbers

    @property
    def resized_image(self):
        resize_image = cv2.resize(self.image,
                                  None,
                                  fx=self.image_scale_factors[1],
                                  fy=self.image_scale_factors[0],
                                  interpolation=cv2.INTER_CUBIC)
        return resize_image

    @property
    def image_scale_factors(self):
        target_height, target_width = self.template_matching_resolution
        height, width, _ = self.image.shape

        scale_factor_y = float(target_height) / height
        scale_factor_x = float(target_width) / width

        return scale_factor_y, scale_factor_x

    @property
    def resized_bucket_marker_template(self):
        resized_bucket_marker_template = cv2.resize(self.bucket_marker_template,
                                                    None,
                                                    fx=self.template_scale_factors[1],
                                                    fy=self.template_scale_factors[0],
                                                    interpolation=cv2.INTER_CUBIC)
        return resized_bucket_marker_template

    @property
    def template_scale_factors(self):
        original_height, original_width = self.bucket_marker_template_original_resolution
        template_matching_height, template_matching_width = self.template_matching_resolution
        bucket_marker_template_height, bucket_marker_template_width, _ = self.bucket_marker_template.shape

        target_height = bucket_marker_template_height * template_matching_height/original_height
        target_width = bucket_marker_template_width * template_matching_width/original_width

        scale_factor_x = float(target_width) / bucket_marker_template_width
        scale_factor_y = float(target_height) / bucket_marker_template_height

        return scale_factor_y, scale_factor_x
