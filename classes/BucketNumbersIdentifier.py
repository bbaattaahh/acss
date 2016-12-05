import pytesseract
import cv2
import numpy as np
from PIL import Image

from RGBImageSlicer import RGBImageSlicer


class BucketNumbersIdentifier:
    def __init__(self,
                 bucket_marker_image):

        self.rgb_image_slicer = RGBImageSlicer(image=bucket_marker_image)

    @property
    def left_bucket_number(self):

        return None

    @property
    def right_bucket_number(self):
        return None


    @staticmethod
    def process_image(image):
        return None

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
    def gray_image(image):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return gray_image


    @staticmethod
    def vanish_black_contours_beside_edges(image):
        black_frame_image = BucketNumbersIdentifier.set_img_frame_black(image)
        flood_filled_image = BucketNumbersIdentifier.flood_fill_with_white_for_top_left_corner(black_frame_image)
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

    @staticmethod
    def do_number_recognition(image):
        pil_image = Image.fromarray(image)
        recognized_numbers = pytesseract.image_to_string(pil_image, config='-psm 7 -outputbase digits')
        return recognized_numbers

