__author__ = 'Henrik'

def classify_the_asparagus(asparagus):

    if asparagus.width < 10:
        asparagus.classification = "Leves"

    if asparagus.width >= 10 and asparagus.width < 13:
        asparagus.classification = "Solo II"

    if asparagus.width >= 13 and asparagus.width < 16:
        asparagus.classification = "Solo I"

    if asparagus.width >= 16:
        asparagus.classification = "EXTRA"

    return None