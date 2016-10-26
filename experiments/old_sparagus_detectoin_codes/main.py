__author__ = '502444620'

import numpy as np
import cv2

from hole_filler import hole_filler

from decide_about_contours_it_could_be_an_asparagus import decide_about_conturs

from delete_incorrect_contours import delete_incorrect_contours

from set_img_frame import set_img_frame

from merge_binary_layers import merge_binary_layers


cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    # lower_blue = np.array([ 240, 240, 240])
    # upper_blue = np.array([255,255,255])

    # It should be adaptive
    # Threshold the HSV image to get only blue colors
    # HVS
    # mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # RGB
    #mask = cv2.inRange(frame, lower_blue, upper_blue)
    #
    #blur = cv2.GaussianBlur(frame[:,:,1],(5,5),0)
    #ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    block_size = 123

    # frame[:,:,0] = cv2.GaussianBlur(frame[:,:,0],(3,3),0)
    # frame[:,:,1] = cv2.GaussianBlur(frame[:,:,1],(3,3),0)
    # frame[:,:,2] = cv2.GaussianBlur(frame[:,:,2],(3,3),0)




    #mask0 = cv2.adaptiveThreshold(frame[:,:,0],255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
    #        cv2.THRESH_BINARY, block_size, 2)

    #mask0 =  np.invert(mask0)

    # mask1 = cv2.adaptiveThreshold(frame[:,:,1],255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
    #        cv2.THRESH_BINARY, block_size, 2)

    #mask1 =  np.invert(mask1)

    #mask2 = cv2.adaptiveThreshold(frame[:,:,2],255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
    #        cv2.THRESH_BINARY, block_size, 2)

    #mask2 =  np.invert(mask2)

    #frame = cv2.COLOR_BGR2GRAY(frame)
    mask3 = cv2.Canny(frame,140,90)
    # mask3 =  np.invert(mask3)

    #laplacian = merge_binary_layers(laplacian, mask3, 0, 255)

    # mask = mask0 + mask1 + mask2 #+ mask3

    # mask = merge_binary_layers(mask0, mask1, 0, 255)
    # mask = merge_binary_layers(mask, mask2, 0, 255)
    # mask = merge_binary_layers(mask, mask3, 0, 255)


    # mask = mask.astype(np.uint8)
    # laplacian = laplacian.astype(np.uint8)
    # cv2.imshow('mask_felut', laplacian)


    # mask = set_img_frame(mask, 0, 10)
    # mask = np.invert(mask)


    # erode/dilate
    kernel = np.ones((4,4),np.uint8)
    mask3 = cv2.dilate(mask3, kernel, iterations = 1)
    #hole_filler
    # mask3 = hole_filler(mask3)

    # copy_of_mask = mask3.copy()
    # copy_of_mask = np.invert(copy_of_mask)
    contours, hierarchy = cv2.findContours(mask3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    correct_conturs = decide_about_conturs(contours, 500, 5)

    if correct_conturs != [] :
        for i in range(0, len(correct_conturs)):
            x,y,w,h = cv2.boundingRect(correct_conturs[i])
            valami = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            crop_img = frame[y:y+h, x:x+w]
            # rect = cv2.minAreaRect(correct_conturs[i])
            # box = cv2.boxPoints(rect)
            # box = np.int0(box)
            # im = cv2.drawContours(frame,[box],0,(0,0,255),2)
            # cv2.imshow('valami',crop_img)
    # mask3 = delete_incorrect_contours(mask3, contours, 0, 200, 5)


    # Bitwise-AND mask and original image
    # res = cv2.bitwise_and(frame, frame, mask = mask3)

    cv2.imshow('frame',frame)
    # cv2.imshow('mask',mask3)
    #cv2.imshow('res',res)
    #cv2.imshow('laplacian',laplacian)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()