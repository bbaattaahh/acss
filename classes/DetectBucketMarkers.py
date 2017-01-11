import cv2


class DetectBucketMarkers:

    always_seen_middle_part_rate = 0.2

    def __init__(self,
                 image,
                 bucket_marker_template):

        self.image = image
        self.bucket_marker_template = bucket_marker_template

    @property
    def always_seen_middle_template(self):
        width_from = int(self.bucket_marker_template.shape[1]*(0.5 - DetectBucketMarkers.always_seen_middle_part_rate/2))
        width_to = int(self.bucket_marker_template.shape[1]*(0.5 + DetectBucketMarkers.always_seen_middle_part_rate/2))
        always_seen_middle_template = self.bucket_marker_template[:, width_from:width_to,:]
        return always_seen_middle_template
