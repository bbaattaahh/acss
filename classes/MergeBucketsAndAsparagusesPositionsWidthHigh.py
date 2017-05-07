# test are required


class MergeBucketsAndAsparagusPositionsWidthHigh:
    def __init__(self,
                 buckets,
                 one_asparagus_image_rectangles,
                 width_and_high):

        self.buckets = buckets
        self.one_asparagus_image_rectangles = one_asparagus_image_rectangles
        self.width_and_high = width_and_high

    @property
    def bucket_asparagus_pairs(self):
        bucket_asparagus_pairs = []

        for bucket in self.buckets:
            if bucket.bucket_number == "":
                return []
            for asparagus_image_middle in self.asparagus_image_middles:
                if bucket.start <= asparagus_image_middle <= bucket.end:
                    index = self.asparagus_image_middles.index(asparagus_image_middle)
                    bucket_asparagus_pairs.append([bucket.bucket_number, self.width_and_high[index]])

        return bucket_asparagus_pairs

    @property
    def asparagus_image_middles(self):
        asparagus_image_middles = list(map(self.horizontal_middle_of_opencv_rectangle,
                                           self.one_asparagus_image_rectangles))
        return asparagus_image_middles

    @staticmethod
    def horizontal_middle_of_opencv_rectangle(opencv_rectangle):
        middle = opencv_rectangle[0][0]
        return middle
