import cv2
import pytesseract
from PIL import Image


class DetectBuckets:
    def __init__(self,
                 image,
                 bucket_marker_image,
                 bucket_marker_dimensions_in_millimeter,
                 pixel_millimeter_ratio):

        self.image = image
        self.bucket_marker_image = bucket_marker_image
        self.bucket_marker_dimensions_in_millimeter = bucket_marker_dimensions_in_millimeter
        self.pixel_millimeter_ratio = pixel_millimeter_ratio

    @staticmethod
    def do_number_recognition(image):
        pil_image = Image.fromarray(image)
        recognized_numbers = pytesseract.image_to_string(pil_image, config='-psm 7')
        return recognized_numbers

    def get_bucket_marker_image_center(self):
        height, width, _ = self.bucket_marker_image.shape
        center_x = width/2
        center_y = height/2

        lower_x = int(center_x - width*0.05)
        upper_x = int(center_x + width*0.05)
        lower_y = int(center_y - height*0.05)
        upper_y = int(center_y + height*0.05)

        center_image = self.bucket_marker_image[lower_y:upper_y, lower_x:upper_x, :]

        return center_image
