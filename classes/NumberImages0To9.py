import cv2


class NumberImages0To9:
    def __init__(self,
                 folder_path):

        self.folder_path = folder_path
        self.number_0 = self.get_image("0.jpg")
        self.number_1 = self.get_image("1.jpg")
        self.number_2 = self.get_image("2.jpg")
        self.number_3 = self.get_image("3.jpg")
        self.number_4 = self.get_image("4.jpg")
        self.number_5 = self.get_image("5.jpg")
        self.number_6 = self.get_image("6.jpg")
        self.number_7 = self.get_image("7.jpg")
        self.number_8 = self.get_image("8.jpg")
        self.number_9 = self.get_image("9.jpg")

    def get_image(self, image_name):
        image = cv2.imread(self.folder_path + "/" + image_name,
                           flags=cv2.IMREAD_GRAYSCALE)
        return image