__author__ = 'Henrik'

def classify_the_asparaguses(my_whole_image):
    for act_asparagus in my_whole_image.asparaguses:
        classify_the_asparagus(act_asparagus)


def classify_the_asparagus(asparagus):

    if asparagus.width_millimeter < 10:
        asparagus.classification = "Leves"

    if asparagus.width_millimeter >= 10 and asparagus.width_millimeter < 13:
        asparagus.classification = "Solo II"

    if asparagus.width_millimeter >= 13 and asparagus.width_millimeter < 16:
        asparagus.classification = "Solo I"

    if asparagus.width_millimeter >= 16:
        asparagus.classification = "EXTRA"

    return None