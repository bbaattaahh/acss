__author__ = '502444620'

import cv2
import numpy as np
import matplotlib.pyplot as plt


def def_coin_diamaters():

    diamaters = np.array([21.2, 23.8, 24.8, 26.3, 27.4, 28.3])

    return diamaters


def get_radius(cycles):

    cycles = cycles[0]

    radiuses = []

    for i in range(0, len(cycles)):
        act_cycle = cycles[i]
        act_radius = act_cycle[2]
        radiuses.append(act_radius)

    return radiuses


def main_calculate_mm_pixel_ratio(calib_img):
    calib_img = cv2.medianBlur(calib_img,33)

    circles = cv2.HoughCircles(calib_img,
                               cv2.cv.CV_HOUGH_GRADIENT,
                               1,
                               20,
                               param1=80,
                               param2=20,
                               minRadius=40,
                               maxRadius=100)

    circles = np.uint16(np.around(circles))

    measured_rads = get_radius(circles)
    sorted_measured_rads = sorted(measured_rads)
    calib_diameters = def_coin_diamaters()
    calib_rads = calib_diameters / 2

    pixel_mm_ratios = calib_rads / sorted_measured_rads
    estimate_of_pixel_mm_ratio = np.mean(pixel_mm_ratios)

    return estimate_of_pixel_mm_ratio


img = cv2.imread("calib_coins2.jpg",0)
img = cv2.medianBlur(img,33)

circles = cv2.HoughCircles(img,cv2.cv.CV_HOUGH_GRADIENT,1,20,param1=80,param2=20,minRadius=40,maxRadius=100)
circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('detected circles',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print circles

rads = get_radius(circles)
rads = sorted(rads)
calib_diameters = def_coin_diamaters()
calib_rads = calib_diameters / 2

plt.plot(calib_rads, rads, 'ro')
plt.show()

print calib_rads / rads

pixel_mm_ratios = calib_rads / rads
estimate_of_pixel_mm_ratio = np.mean(pixel_mm_ratios)

print(estimate_of_pixel_mm_ratio)


img = cv2.imread("calib_coins2.jpg",0)

print(main_calculate_mm_pixel_ratio(img))