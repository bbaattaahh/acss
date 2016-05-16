import numpy as np

def preprocess_input_image(image):

    image = np.rot90(image)

    return image