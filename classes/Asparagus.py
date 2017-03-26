class Asparagus:
    def __init__(self,
                 length,
                 thickness,
                 white_head=True,
                 no_head=False,
                 purple_head=False,
                 open_head=False,
                 piper=False):

        self.length = length
        self.thickness = thickness
        self.white_head = white_head
        self.no_head=no_head
        self.purple_head = purple_head
        self.open_head = open_head
        self.piper = piper

    def __eq__(self, other):
        return self.__dict__ == other.__dict__