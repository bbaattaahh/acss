import more_itertools


class BucketNumbersCorrector:

    def __init__(self,
                 bucket_numbers,
                 max_bucket_number):

        self.bucket_numbers = bucket_numbers
        self.max_bucket_number = max_bucket_number

    @property
    def int_flatten_bucket_numbers(self):
        flatten_bucket_numbers = list(more_itertools.flatten(self.bucket_numbers))
        int_flatten_bucket_numbers = []

        for flatten_bucket_number in flatten_bucket_numbers:
            if flatten_bucket_number == "":
                int_flatten_bucket_numbers.append(None)
                continue

            int_flatten_bucket_numbers.append(int(flatten_bucket_number))

        return int_flatten_bucket_numbers

    def eliminate_empty_strings(self):
        for i in range(0, len(self.bucket_numbers)):
            if self.bucket_numbers[i][0] == "" and i <> 0:
                self.bucket_numbers[i][0] = self.bucket_numbers[i-1][1]

            if self.bucket_numbers[i][1] == "" and i <> len(self.bucket_numbers)-1:
                self.bucket_numbers[i][1] = self.bucket_numbers[i+1][0]

        return self.bucket_numbers

    def fulfill_bucket_numbers_which_has_one_item(self, bucket_numbers):
        for i in range(0, len(bucket_numbers)-1):
            if bucket_numbers[i] is None:
                continue
            if i % 2 == 0:
                bucket_numbers[i+1] = self.next_number(bucket_numbers[i])
            if i % 2 == 1:
                bucket_numbers[i+1] = bucket_numbers[i]

        for i in range(len(bucket_numbers)-1, 0, -1):
            if bucket_numbers[i-1] is not None:
                continue
            if i % 2 == 1:
                bucket_numbers[i-1] = self.previous_number(bucket_numbers[i])
            if i % 2 == 0:
                bucket_numbers[i-1] = bucket_numbers[i]

        return bucket_numbers

    @staticmethod
    def number_to_3digit_string(number):
        str_number = str(number)
        if len(str_number) == 1:
            return "00" + str_number

        if len(str_number) == 2:
            return "0" + str_number

        return str_number

    def next_number(self, number):
        if number+1 > self.max_bucket_number:
            return 1

        return number+1

    def previous_number(self, number):
        if number-1 < 1:
            return self.max_bucket_number

        return number-1

    @staticmethod
    def bucket_numbers_distance(bucket_numbers_1, bucket_numbers_2):
        distance = 0
        for i in range(0, len(bucket_numbers_1)):
            if bucket_numbers_1[i] is None or bucket_numbers_2[i] is None:
                continue

            if bucket_numbers_1[i] != bucket_numbers_2[i]:
                distance += 1

        return distance
