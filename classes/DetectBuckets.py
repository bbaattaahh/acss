import cv2


class DetectBuckets:
    def __init__(self,
                 image,
                 number_images_0_to_9):

        self.image = image
        self.number_images_0_to_9 = number_images_0_to_9

    @staticmethod
    def template_match(image, template):
        return None



    def prepare_image(self):
        gray_image = self.get_gray_image(self.image)
        resized_image = self.resize_image(gray_image)
        return resized_image

    def prepare_number_images(self):
        prepared_number_images_0_to_9 = self.number_images_0_to_9.copy()

        for index in range(len(prepared_number_images_0_to_9.numbers)):
            prepared_number_images_0_to_9.numbers[index] = \
                                    self.get_gray_image(prepared_number_images_0_to_9.numbers[index])

        return prepared_number_images_0_to_9

    @staticmethod
    def get_gray_image(image):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return gray_image

    def resize_image(self, image):
        parent_image_shape = self.number_images_0_to_9.parent_image_resolution
        image_shape = image.shape

        scale_factor_y = float(parent_image_shape[0]) / float(image_shape[0])
        scale_factor_x = float(parent_image_shape[1]) / float(image_shape[1])

        resized_image = cv2.resize(image,
                                   None,
                                   fx=scale_factor_x,
                                   fy=scale_factor_y,
                                   interpolation=cv2.INTER_CUBIC)

        return resized_image
