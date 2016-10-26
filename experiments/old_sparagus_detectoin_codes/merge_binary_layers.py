__author__ = '502444620'

import numpy as np


def merge_binary_layers(layer1, layer2, value_to_peserve, value_to_forget):
    bool_layer1 = layer1 == value_to_peserve
    bool_layer2 = layer2 == value_to_peserve

    bool_merged = bool_layer1 | bool_layer2
    inverse_of_bool_merge = np.logical_not(bool_merged)

    layer_to_preserve = bool_merged.astype(layer1.__class__)
    layer_to_preserve = layer_to_preserve * value_to_peserve

    layer_to_forget = inverse_of_bool_merge.astype(layer1.__class__)
    layer_to_forget = layer_to_forget * value_to_forget

    merged_layer = layer_to_preserve + layer_to_forget

    merged_layer.astype(layer1.__class__)

    return merged_layer