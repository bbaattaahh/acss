import cv2

from time import gmtime, strftime
from BucketsDetector import BucketsDetector
from BucketMarkersDetector import BucketMarkersDetector

template = cv2.imread("template.jpg")
bucket_marker_template_original_resolution = 960, 1280
template_matching_resolution = 480, 640
max_bucket_number = 100

buckets_detector = BucketsDetector(template,
                                   bucket_marker_template_original_resolution,
                                   template_matching_resolution,
                                   max_bucket_number)

bucket_markers_detector = BucketMarkersDetector(bucket_marker_template=template,
                                                max_bucket_number=110,
                                                expected_template_matching_threshold=1.5)

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    _, frame = cap.read()

    buckets = buckets_detector.buckets_on_image(frame)

    if len(buckets) > 0:
        frame[:, buckets[0].end, :] = 0
        print(buckets[0].bucket_number)

    bucket_markers = bucket_markers_detector.get_bucket_markers(frame)

    if len(bucket_markers) > 0:
        rectangle = bucket_markers[0].bounding_rectangle
        top_left_corner = rectangle.top_left_x, rectangle.top_left_y
        button_right_corner = rectangle.top_left_x + rectangle.width, rectangle.top_left_y + rectangle.high
        cv2.rectangle(frame, top_left_corner, button_right_corner, (255, 0, 0), 2)
        #print(bucket_markers[0].left_bucket_number)
        #print(bucket_markers[0].right_bucket_number)



    cv2.imshow('frame', frame)
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
