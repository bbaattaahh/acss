class Bucket:
    def __init__(self,
                 start="Unknown",
                 end="Unknown",
                 bucket_number="Unknown"):

        self.start = start
        self.end = end
        self.bucket_number = bucket_number

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
