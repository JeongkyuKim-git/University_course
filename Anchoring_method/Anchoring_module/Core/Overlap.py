class Overlap(object):

    def __init__(self, length):
        self.length = length
        self.queryIndex = [None] * 2
        self.kMer = ''
        self.referenceIndex = [None] * 2
        self.anchorChild = False

    def setReferenceIndex(self, referenceIndex, position):
        self.referenceIndex[position] = referenceIndex

    def setQueryIndex(self, queryIndex, position):
        self.queryIndex[position] = queryIndex

    def setKMer(self, kMer):
        self.kMer = kMer

    def joinWith(self, overlap):
        self.queryIndex[1] = overlap.queryIndex[1]
        self.referenceIndex[1] = overlap.referenceIndex[1]
        self.kMer += overlap.kMer[2:]

    def setAsChild(self):
        self.anchorChild = True

    def isChild(self):
        return self.anchorChild

    def __repr__(self):
        # return 'KMer: ' + self.KMer + \
        #        ' Query: ' + str(self.queryIndex[0]) + ', ' + str(self.queryIndex[1]) + \
        #        ' Reference: ' + str(self.referenceIndex[0]) + ', ' + str(self.referenceIndex[1])
        return self.kMer
