__author__ = '502444620'

import cv2
import imutils
import numpy as np


def calcualte_overlap2(image_flow, upper_narrow_limit, lower_narrow_limit):

    imageA = image_flow.whole_images[0].original_picture_colourful
    imageB = image_flow.whole_images[1].original_picture_colourful


    imageA = narrow_horizontally_examined_part(imageA,
                                               upper_narrow_limit,
                                               lower_narrow_limit)

    imageB = narrow_horizontally_examined_part(imageB,
                                               upper_narrow_limit,
                                               lower_narrow_limit)



    stitcher = calculate_overlap_dummy()
    x_difference_in_picture = stitcher.stitch([imageA, imageB])
    overlap = imageA.shape[1] + x_difference_in_picture

    image_flow.whole_images[0].overlap_forward = overlap
    image_flow.whole_images[1].overlap_backward = overlap

    return None


def dummy_sticher(kpsA, kpsB, matches, status):

    diffs = []

    for match_index in range(0, len(matches)):
        if status[match_index] == 0:
            continue

        actual_good_match = matches[match_index]
        print actual_good_match
        left_image_keypoint = kpsA[actual_good_match[1]]
        right_image_keypoint = kpsB[actual_good_match[0]]

        x_diff = right_image_keypoint[0] - left_image_keypoint[0]
        diffs.append(x_diff)


    avg_x_diff = np.average(diffs)

    avg_x_diff_rounded = int(avg_x_diff)

    return avg_x_diff_rounded


class calculate_overlap_dummy:
    def __init__(self):
        # determine if we are using OpenCV v3.X
        self.isv3 = imutils.is_cv3()

    def stitch(self, images, ratio=0.75, reprojThresh=4.0):
        # unpack the images, then detect keypoints and extract
        # local invariant descriptors from them
        (imageB, imageA) = images
        (kpsA, featuresA) = self.detectAndDescribe(imageA)
        (kpsB, featuresB) = self.detectAndDescribe(imageB)

        #print kpsA
        #print kpsB

        # match features between the two images
        M = self.matchKeypoints(kpsA, kpsB,
            featuresA, featuresB, ratio, reprojThresh)

        #print M

        # if the match is None, then there aren't enough matched
        # keypoints to create a panorama
        if M is None:
            return None

        # otherwise, apply a perspective warp to stitch the images
        # together
        (matches, H, status) = M

        return dummy_sticher(kpsA, kpsB, matches, status)


    def detectAndDescribe(self, image):
        # convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # check to see if we are using OpenCV 3.X
        if self.isv3:
            # detect and extract features from the image
            descriptor = cv2.xfeatures2d.SIFT_create()
            (kps, features) = descriptor.detectAndCompute(image, None)

        # otherwise, we are using OpenCV 2.4.X
        else:
            # detect keypoints in the image
            detector = cv2.FeatureDetector_create("SIFT")
            kps = detector.detect(gray)

            # extract features from the image
            extractor = cv2.DescriptorExtractor_create("SIFT")
            (kps, features) = extractor.compute(gray, kps)

        # convert the keypoints from KeyPoint objects to NumPy
        # arrays
        kps = np.float32([kp.pt for kp in kps])

        # return a tuple of keypoints and features
        return (kps, features)

    def matchKeypoints(self, kpsA, kpsB, featuresA, featuresB,
        ratio, reprojThresh):
        # compute the raw matches and initialize the list of actual
        # matches
        matcher = cv2.DescriptorMatcher_create("BruteForce")
        rawMatches = matcher.knnMatch(featuresA, featuresB, 2)
        matches = []

        # loop over the raw matches
        for m in rawMatches:
            # ensure the distance is within a certain ratio of each
            # other (i.e. Lowe's ratio test)
            if len(m) == 2 and m[0].distance < m[1].distance * ratio:
                matches.append((m[0].trainIdx, m[0].queryIdx))

        # computing a homography requires at least 4 matches
        if len(matches) > 4:
            # construct the two sets of points
            ptsA = np.float32([kpsA[i] for (_, i) in matches])
            ptsB = np.float32([kpsB[i] for (i, _) in matches])

            # compute the homography between the two sets of points
            (H, status) = cv2.findHomography(ptsA, ptsB, cv2.RANSAC,
                reprojThresh)

            # return the matches along with the homograpy matrix
            # and status of each matched point
            return (matches, H, status)

        # otherwise, no homograpy could be computed
        return None


def narrow_horizontally_examined_part(image, upper_limit, lower_limit):
    return image[upper_limit:lower_limit, :, :]

