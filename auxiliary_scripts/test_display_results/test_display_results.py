from DisplayClassification import DisplayClassification
import time

display_classification = DisplayClassification(image_size=(480, 640), letter_pixel_high=30)

for i in range(1,100):
    display_classification.add_new_result(i, "Jani a kompon")
    time.sleep(2)
    display_classification.display_actual()

display_classification.kill()