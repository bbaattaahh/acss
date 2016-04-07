
class image_flow:
    def __init__(self, whole_images = []):
        self.whole_images = whole_images


    def add_whole_image(self, whole_image):
        self.whole_images.insert(0, whole_image)