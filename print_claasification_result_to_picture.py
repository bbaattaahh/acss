__author__ = 'Henrik'
import numpy as np
import cv2
from matplotlib import pyplot as plt

#TODO In case equal frequency of the classification result in one section, the last element will return


def print_classification_result_to_picture(image_flow,
                                           start_image_index,
                                           start_pixel,
                                           end_image_index,
                                           width_to_display,
                                           concatenated_image):

    ranges = []
    start_pixel_on_concateneted_image_next_image = 0

    for image_index in range(start_image_index, end_image_index+1):
        start_pixel_on_concateneted_image_act_image = start_pixel_on_concateneted_image_next_image
        if image_index == start_image_index :
            for act_asparagus in image_flow.whole_images[image_index].asparaguses:
                if act_asparagus.top_left_corner_x >= start_pixel:
                    start_pixel_on_concateneted_image = act_asparagus.top_left_corner_x - start_pixel
                    end_pixel_on_concateneted_image = start_pixel_on_concateneted_image + act_asparagus.sub_image.shape[1]
                    ranges.append([act_asparagus.classification,
                                   start_pixel_on_concateneted_image,
                                   end_pixel_on_concateneted_image])

            start_pixel_on_concateneted_image_next_image = image_flow.whole_images[start_image_index].original_picture_colourful.shape[1]\
                                                           - image_flow.whole_images[start_image_index].overlap_forward \
                                                           - start_pixel

        if image_index != start_image_index:
            for act_asparagus in image_flow.whole_images[image_index].asparaguses:
                start_pixel_on_concateneted_image = act_asparagus.top_left_corner_x + start_pixel_on_concateneted_image_act_image
                end_pixel_on_concateneted_image = start_pixel_on_concateneted_image + act_asparagus.sub_image.shape[1]
                ranges.append([act_asparagus.classification,
                               start_pixel_on_concateneted_image,
                               end_pixel_on_concateneted_image])

            start_pixel_on_concateneted_image_next_image = start_pixel_on_concateneted_image_next_image \
                                                           + image_flow.whole_images[image_index].original_picture_colourful.shape[1]\
                                                           - image_flow.whole_images[image_index].overlap_forward \

    merged_sections_with_multiple_classification_result = merge_sections(ranges)
    merged_sections_with_most_frequent_classification_result = get_most_common_classification_result_in_one_merged_section(merged_sections_with_multiple_classification_result)

    pic = put_text_to_image(concatenated_image, merged_sections_with_most_frequent_classification_result)

    # cv2.imshow('nossss',pic)


    return pic


def merge_sections(sections):
    merged_sections = []

    for section in sections:
        match_flag = False
        for merged_section in merged_sections:
            if (section[1] >= merged_section[1] and section[1] <= merged_section[2]):
                match_flag = True
                merged_section[2] = section[2]
                merged_section[0].append(section[0])

        if match_flag == False :
            extendedable_section = [[section[0]], section[1], section[2]]
            merged_sections.append(extendedable_section)

    return merged_sections


def get_most_common_classification_result_in_one_merged_section(merged_sections):
    merged_sectoins_with_the_frequent_classification_result = []
    for merged_section in merged_sections:
        most_frequent_classification_result = most_common(merged_section[0])
        merged_sectoins_with_the_frequent_classification_result.append([most_frequent_classification_result,
                                                                        merged_section[1],
                                                                        merged_section[2]])

    return merged_sectoins_with_the_frequent_classification_result

def most_common(lst):
    return max(set(lst), key=lst.count)


def put_text_to_image(image, calssification_results):
    for calssification_result in calssification_results:
        cv2.putText(image,
                    calssification_result[0],
                    (int(calssification_result[1]), image.shape[0]),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    5,
                    int(image.shape[0] * 0.05 * 8 / 6),
                    thickness = 20)


    return image