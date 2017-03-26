class AsparagusClassifier:

    def __init__(self,
                 millimeter_pixel_ratio,
                 classification_specification):

        self.millimeter_pixel_ratio = millimeter_pixel_ratio
        self.classification_specification = classification_specification

    def classify(self, asparagus):
        for actual_class in self.classification_specification:
            if self.is_asparagus_fit_to_class(asparagus, actual_class):
                return actual_class
        return "no class"

    def is_asparagus_fit_to_class(self, asparagus, actual_class):
        for actual_condition_name, actual_condition in self.classification_specification[actual_class].items():
            if not self.is_condition_full(asparagus, actual_condition_name, actual_condition):
                return False
        return True

    def is_condition_full(self, asparagus, condition_name, condition):
        if condition_name == "length":
            return self.is_length_appropriate(asparagus, condition)
        if condition_name == "thickness":
            return self.is_thickness_appropriate(asparagus, condition)
        if condition_name == "white_head":
            return self.is_white_head_appropriate(asparagus, condition)
        if condition_name == "no_head":
            return self.is_white_head_appropriate(asparagus, condition)
        if condition_name == "purple_head":
            return self.is_purple_head_appropriate(asparagus, condition)
        if condition_name == "open_head":
            return self.is_open_head_appropriate(asparagus, condition)
        if condition_name == "piper":
            return self.is_piper_appropriate(asparagus, condition)

    def is_length_appropriate(self, asparagus, length_conditions):
        thickness_in_millimeter = asparagus.length * self.millimeter_pixel_ratio
        if thickness_in_millimeter <= length_conditions["lower_limit"]:
            return False
        if thickness_in_millimeter > length_conditions["upper_limit"]:
            return False
        return True

    def is_thickness_appropriate(self, asparagus, thickness_conditions):
        thickness_in_millimeter = asparagus.thickness * self.millimeter_pixel_ratio
        if thickness_in_millimeter <= thickness_conditions["lower_limit"]:
            return False
        if thickness_in_millimeter > thickness_conditions["upper_limit"]:
            return False
        return True

    @staticmethod
    def is_white_head_appropriate(asparagus, expected_head):
        return expected_head == asparagus.white_head

    @staticmethod
    def is_no_head_appropriate(asparagus, expected_head):
        return expected_head == asparagus.no_head

    @staticmethod
    def is_purple_head_appropriate(asparagus, expected_purple_head):
        return expected_purple_head == asparagus.purple_head

    @staticmethod
    def is_open_head_appropriate(asparagus, expected_open_head):
        return expected_open_head == asparagus.open_head

    @staticmethod
    def is_piper_appropriate(asparagus, expected_piper):
        return expected_piper == asparagus.piper
