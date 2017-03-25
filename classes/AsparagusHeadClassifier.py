import numpy as np
from keras.models import model_from_json
from keras import backend as K

from AsparagusHeadImage import AsparagusHeadImage


class AsparagusHeadClassifier:

    def __init__(self,
                 neural_network_hierarchy_file,
                 neural_network_weights_file,
                 classification_labels,
                 top_part_to_keep_ratio,
                 head_classification_resolution):

        json_file = open(neural_network_hierarchy_file, 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        self.model = model_from_json(loaded_model_json)
        self.model.load_weights(neural_network_weights_file)
        self.classification_labels = classification_labels
        self.top_part_to_keep_ratio = top_part_to_keep_ratio
        self.head_classification_resolution = head_classification_resolution

    def predict(self, image):
        asparagus_head_image = AsparagusHeadImage(image,
                                                  self.top_part_to_keep_ratio,
                                                  self.head_classification_resolution).resized_top_part

        processed_image = self.process_image(asparagus_head_image)
        image_with_extra_dimension = np.array([processed_image])
        model_result_weights = self.model.predict(image_with_extra_dimension)
        label = self.classification_labels[np.argmax(model_result_weights)]
        return label

    @staticmethod
    def process_image(image):
        K.set_image_dim_ordering('th')
        float_image = image.astype('float32')
        normalized_image = float_image / 255.0
        return normalized_image
