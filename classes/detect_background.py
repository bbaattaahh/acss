from datetime import datetime

class detect_background:
    def __init__(self,
                 act_image,
                 former_image = None,
                 masks = [],
                 actual_mask = None,
                 creation_time = datetime.now()):

        self.act_image = act_image
        self.former_image = former_image
        self.masks = masks
        self.actual_mask = actual_mask
        self.creation_time = creation_time

    def add_mask(self, mask):
        self.masks.append(mask)
