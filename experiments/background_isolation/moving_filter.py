# try built in openCV functions OpenCV, (MOG, MOG2, GMG algorithm)

class moving_filter:
    masks = []
    masked_image = None

    def __init__(self, leg, difference_limit, first_frame):
        self.leg = leg
        self.difference_limit = difference_limit
        self.frames = [first_frame]

    def add_frame(self, frame):

        def get_mask(difference_limit, frame_t1, frame_t2):
            difference_image = abs(frame_t1 - frame_t2)
            mask = cv2.inRange(difference_image, difference_limit, 255)
            return mask

        self.frames.append(frame)

        if len(self.frames) > self.leg:
            del self.frames[0]

        if len(self.frames) > 1:
            mask = get_mask(self.difference_limit,
                            self.frames[-2],
                            self.frames[-1])

            moving_filter.masks.append(mask)

            if len(moving_filter.masks) > self.leg - 1:
                del moving_filter.masks[0]

            commulatied_mask = moving_filter.masks[0]

            for mask in moving_filter.masks:
                commulatied_mask = cv2.bitwise_or(commulatied_mask, mask)

            moving_filter.masked_image = cv2.bitwise_and(self.frames[-1],
                                                         self.frames[-1],
                                                         mask=commulatied_mask)


from moviepy.editor import *
import cv2
import numpy as np

clip = VideoFileClip('live_test_2.avi')

t =  np.arange(20,60,0.01)

act_frame_brg = clip.get_frame("00:00:00")
act_frame_rgb = cv2.cvtColor(act_frame_brg, cv2.COLOR_BGR2RGB)
act_frame_gray = cv2.cvtColor(act_frame_brg, cv2.COLOR_RGB2GRAY)
act_frame_gray_blur = cv2.blur(act_frame_gray,(10,10))

fgbg = cv2.BackgroundSubtractorMOG(history=1000, nmixtures = 5, backgroundRatio = 0.55, noiseSigma = 0)
# fgbg = cv2.BackgroundSubtractorMOG2(history=100, varThreshold=16, bShadowDetection=False)
fgmask = fgbg.apply(act_frame_gray_blur)

maf1 = moving_filter(20, 200, act_frame_gray)

for x in t:
    act_str = '00:00:' + str(x)
    act_frame_brg = clip.get_frame(act_str)
    act_frame_rgb = cv2.cvtColor(act_frame_brg, cv2.COLOR_BGR2RGB)
    act_frame_gray = cv2.cvtColor(act_frame_brg, cv2.COLOR_RGB2GRAY)
    act_frame_gray_blur = cv2.blur(act_frame_gray, (10, 10))

    fgmask = fgbg.apply(act_frame_gray_blur)

    maf1.add_frame(act_frame_gray_blur)

    cv2.imshow('happy?', fgmask)
    #cv2.imshow('happy?', maf1.masked_image)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()