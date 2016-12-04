import pytesseract
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
    def do_number_recognition(image):
        pil_image = Image.fromarray(image)
        recognized_numbers = pytesseract.image_to_string(pil_image, config='-psm 7 -outputbase digits')
        return recognized_numbers