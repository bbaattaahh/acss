import cv2


class NumberImages0To9:
    def __init__(self,
                 folder_path,
                 parent_image_resolution):

        self.folder_path = folder_path
        self.parent_image_resolution = parent_image_resolution
        self.numbers = [self.get_image("0.jpg"),
                        self.get_image("1.jpg"),
                        self.get_image("2.jpg"),
                        self.get_image("3.jpg"),
                        self.get_image("4.jpg"),
                        self.get_image("5.jpg"),
                        self.get_image("6.jpg"),
                        self.get_image("7.jpg"),
                        self.get_image("8.jpg"),
                        self.get_image("9.jpg")]

    def get_image(self, image_name):
        image = cv2.imread(self.folder_path + "/" + image_name)
        return image
