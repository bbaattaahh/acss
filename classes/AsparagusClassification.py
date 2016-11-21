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
        for actual_condition_name, actual_condition in self.classification_specification[actual_class].iteritems():
            if not self.is_condition_full(actual_condition_name, actual_condition):
                return False
        return True

    def is_condition_full(self, condition_name, condition):
        if condition_name == "length":
            return self.is_length_appropriate(condition)
        if condition_name == "thickness":
            return self.is_thickness_appropriate(condition)
        if condition_name == "head":
            return self.is_head_appropriate(condition)
        if condition_name == "purple_head":
            return self.is_purple_head_appropriate(condition)
        if condition_name == "open_head":
            return self.is_open_head_appropriate(condition)
        if condition_name == "piper":
            return self.is_piper_appropriate(condition)

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

    def is_head_appropriate(self, expected_head):
        return expected_head == self.asparagus.head

    def is_purple_head_appropriate(self, expected_purple_head):
        return expected_purple_head == self.asparagus.purple_head

    def is_open_head_appropriate(self, expected_open_head):
        return expected_open_head == self.asparagus.open_head

    def is_piper_appropriate(self, expected_piper):
        return expected_piper == self.asparagus.piper
