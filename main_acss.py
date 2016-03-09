__author__ = 'Henrik'
import numpy as np
import cv2
from matplotlib import pyplot as plt


img = cv2.imread('images/test_img_1.jpg',0)


temp = np.zeros(2560L)

for x in range(0, 2560L):
    temp[x] = sum(img[:,x])

# plt.plot(temp)
# plt.show()

max_white = int(temp.argmax())

my_img = img[:, (max_white-200):(max_white+100)]

plt.imshow(my_img)

print 1
