import cv2
import numpy as np


class DisplayClassification:
    def __init__(self,
                 image_size=(480, 640),
                 letter_pixel_high=30):
        self.image_size = image_size
        self.letter_pixel_high = letter_pixel_high
        self.results = []

    def add_new_result(self, bucket_number, classification_result):
        new_result = str(bucket_number) + " : " + classification_result
        self.results = [new_result] + self.results

        if len(self.results) * self.letter_pixel_high > self.image_size[0]:
            del self.results[-1]

    def display_actual(self):
        cv2.imshow('img', self.actual_image)
        k = cv2.waitKey(30) & 0xff

    @property
    def actual_image(self):
        pos_x = 10
        pos_y = 30
        font = cv2.FONT_HERSHEY_SIMPLEX
        image = np.zeros((self.image_size[0], self.image_size[1], 3), np.uint8)
        for result in self.results:

            image = cv2.putText(image, result, (pos_x, pos_y), font, 1, (255,255,255), 2, cv2.LINE_AA)
            pos_y += self.letter_pixel_high

        return image

    @staticmethod
    def kill():
        cv2.destroyAllWindows()
