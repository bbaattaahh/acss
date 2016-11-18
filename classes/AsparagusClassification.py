class AsparagusClassification:

    def __init__(self,
                 asparagus,
                 millimeter_pixel_ratio,
                 classification_specification):

        self.asparagus = asparagus
        self.millimeter_pixel_ratio = millimeter_pixel_ratio
        self.classification_specification = classification_specification
        self.classification_result = self.classify_asparagus()

    def classify_asparagus(self):
        for actual_class in self.classification_specification:
            if self.is_asparagus_fit_to_class(actual_class):
                return actual_class
        return "no class"

    def is_asparagus_fit_to_class(self, actual_class):
        for actual_condition_key in self.classification_specification[actual_class]:
            actual_condition = self.classification_specification[actual_class][actual_condition_key]
            if not self.is_condition_full(actual_condition_key, actual_condition):
                return False
        return True

    def is_condition_full(self, actual_condition_key, actual_condition):
        if actual_condition_key == "length":
            return self.is_length_appropriate(actual_condition)
        if actual_condition_key == "thickness":
            return self.is_thickness_appropriate(actual_condition)
        if actual_condition_key == "purple_head":
            return self.is_purple_head_appropriate(actual_condition)

    def is_length_appropriate(self, length_conditions):
        thickness_in_millimeter = self.asparagus.length * self.millimeter_pixel_ratio
        if thickness_in_millimeter < length_conditions["lower_limit"]:
            return False
        if thickness_in_millimeter >= length_conditions["upper_limit"]:
            return False
        return True

    def is_thickness_appropriate(self, thickness_conditions):
        thickness_in_millimeter = self.asparagus.thickness * self.millimeter_pixel_ratio

        if thickness_in_millimeter < thickness_conditions["lower_limit"]:
            return False

        if thickness_in_millimeter >= thickness_conditions["upper_limit"]:
            return False

        return True

    def is_purple_head_appropriate(self, expected_purple_head):
        return expected_purple_head == self.asparagus.purple_head
