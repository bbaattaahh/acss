__author__ = '502444620'

import cv2
import numpy as np

def hole_filler(img):

    # Copy the thresholded image.
    im_floodfill = img.copy()

    # Mask used to flood filling.
    # Notice the size needs to be 2 pixels than the image.
    h, w = img.shape[:2]
    mask = np.zeros((h+2, w+2), np.uint8)


    # Floodfill from point (0, 0)
    cv2.floodFill(im_floodfill, mask, (0,0), 255);

    # Invert floodfilled image
    im_floodfill_inv = cv2.bitwise_not(im_floodfill)

    # Combine the two images to get the foreground.
    im_out = img | im_floodfill_inv

    return im_out