class Anchor(object):

    def __init__(self):
        self.overlaps = []
        self.counter = 0

    def append(self, overlap):
        self.overlaps.append(overlap)

    def __repr__(self):
        return str(self.overlaps)