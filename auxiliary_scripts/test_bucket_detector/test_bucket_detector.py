import cv2
import numpy as np

from BucketsDetector import BucketsDetector

template = cv2.imread("template.jpg")
bucket_detector = BucketsDetector(bucket_marker_template=template,
                                  bucket_marker_template_original_resolution=(960, 1280),
                                  template_matching_resolution=(240, 320),
                                  max_bucket_number=110)

cap = cv2.VideoCapture(0)
cap.set(3, 480)
cap.set(4, 320)

while True:
    _, frame = cap.read()

    cv2.imshow('frame', frame)

    if bucket_detector.buckets_on_image(frame) != []:
        print("Meg van marker")
        print(bucket_detector.buckets_on_image(frame)[0].bucket_number)

        frame[:, bucket_detector.buckets_on_image(frame)[0].end, :] = 0

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
