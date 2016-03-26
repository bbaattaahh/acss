
class detect_background:
    def __init__(self, act_image, former_image = None, masks = [], actual_mask = None):
        self.act_image = act_image
        self.former_image = former_image
        self.masks = masks
        self.actual_mask = actual_mask

    def add_mask(self, mask):
        self.masks.append(mask)
