import more_itertools


class BucketNumbersCorrector:

    def __init__(self,
                 bucket_numbers,
                 max_bucket_number):

        self.bucket_numbers = bucket_numbers
        self.max_bucket_number = max_bucket_number

    @property
    def corrected_bucket_numbers(self):
        best_matching_bucket_numbers = self.best_matching_bucket_numbers
        corrected_bucket_numbers = self.convert_int_bucket_numbers_to_original_format(best_matching_bucket_numbers)
        return corrected_bucket_numbers

    @staticmethod
    def convert_int_bucket_numbers_to_original_format(int_bucket_numbers):
        str_bucket_numbers = []
        for i in range(0, len(int_bucket_numbers), 2):
            string_1 = BucketNumbersCorrector.number_to_3digit_string(int_bucket_numbers[i])
            string_2 = BucketNumbersCorrector.number_to_3digit_string(int_bucket_numbers[i+1])
            str_bucket_numbers.append([string_1, string_2])

        return str_bucket_numbers

    @property
    def best_matching_bucket_numbers(self):
        lowest_distance_so_far = 99999
        best_index_so_far = 0

        for index_to_keep in range(0, len(self.int_flatten_bucket_numbers)):
            if self.int_flatten_bucket_numbers[index_to_keep] is None:
                continue

            act_one_item_bucket_numbers = self.one_item_bucket_numbers(index_to_keep)
            act_fulfill_bucket_numbers = self.fulfill_bucket_numbers_which_has_one_item(act_one_item_bucket_numbers)
            act_distance = self.bucket_numbers_distance(self.int_flatten_bucket_numbers,
                                                        act_fulfill_bucket_numbers)

            if act_distance < lowest_distance_so_far:
                lowest_distance_so_far = act_distance
                best_index_so_far = index_to_keep

        best_one_item_bucket_numbers = self.one_item_bucket_numbers(best_index_so_far)
        best_fulfill_bucket_numbers = self.fulfill_bucket_numbers_which_has_one_item(best_one_item_bucket_numbers)
        return best_fulfill_bucket_numbers

    def one_item_bucket_numbers(self, index_to_keep):
        one_item_bucket_numbers = [None] * len(self.int_flatten_bucket_numbers)
        one_item_bucket_numbers[index_to_keep] = self.int_flatten_bucket_numbers[index_to_keep]
        return one_item_bucket_numbers

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
