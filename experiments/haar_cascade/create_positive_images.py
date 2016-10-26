from moviepy.editor import *
import cv2
import numpy as np
import os

clip = VideoFileClip('live_test_2.avi')

t = np.arange(32,55,0.1)

i = 1

for x in t:
    act_str = '00:00:' + str(x)
    act_frame_brg = clip.get_frame(act_str)
    act_frame_rgb = cv2.cvtColor(act_frame_brg, cv2.COLOR_BGR2RGB)
    act_frame_gray = cv2.cvtColor(act_frame_brg, cv2.COLOR_RGB2GRAY)
    act_frame_gray_blur = cv2.blur(act_frame_gray, (10, 10))


    cv2.imshow('happy?', act_frame_rgb)
    filename =  "pos/" + str(i) + ".jpg"
    cv2.imwrite(filename, act_frame_rgb)
    i += 1
    #cv2.imshow('happy?', maf1.masked_image)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()