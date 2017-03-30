import cv2

from BucketMarkersDetector import BucketMarkersDetector

template = cv2.imread("template.jpg")

bucket_markers_detector = BucketMarkersDetector(bucket_marker_template=template,
                                                max_bucket_number=110,
                                                expected_template_matching_threshold=2)


cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    _, frame = cap.read()

    bucket_markers = bucket_markers_detector.get_bucket_markers(frame)

    if len(bucket_markers) > 0:
        rectangle = bucket_markers[0].bounding_rectangle
        top_left_corner = rectangle.top_left_x, rectangle.top_left_y
        botton_right_corner = rectangle.top_left_x + rectangle.width, rectangle.top_left_y+rectangle.high
        cv2.rectangle(frame, top_left_corner, botton_right_corner, (255, 0, 0), 2)
        print(bucket_markers[0].left_bucket_number)
        print(bucket_markers[0].right_bucket_number)

    cv2.imshow('frame', frame)



    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
