class BucketNumbersCorrector:

    def __init__(self,
                 bucket_numbers,
                 max_bucket_number):

        self.bucket_numbers = bucket_numbers
        self.max_bucket_number = max_bucket_number

    @property
    def int_bucket_numbers(self):
        int_bucket_numbers = []
        for number_pair in self.bucket_numbers:
            if number_pair[0] != "":
                number_1 = int(number_pair[0])
            else:
                number_1 = None

            if number_pair[1] != "":
                number_2 = int(number_pair[1])
            else:
                number_2 = None

            int_number_pair = [number_1, number_2]
            int_bucket_numbers.append(int_number_pair)

        return int_bucket_numbers

    def eliminate_empty_strings(self):
        for i in range(0, len(self.bucket_numbers)):
            if self.bucket_numbers[i][0] == "" and i <> 0:
                self.bucket_numbers[i][0] = self.bucket_numbers[i-1][1]

            if self.bucket_numbers[i][1] == "" and i <> len(self.bucket_numbers)-1:
                self.bucket_numbers[i][1] = self.bucket_numbers[i+1][0]

        return self.bucket_numbers

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
