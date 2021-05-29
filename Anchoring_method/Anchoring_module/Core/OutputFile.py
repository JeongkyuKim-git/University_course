from Core.Anchor import Anchor


class OutputFile:

    def __init__(self, fileName, referenceSequence, referenceHeader, kMerSize):
        self.fileName = fileName
        self.referenceSequence = referenceSequence
        self.referenceHeader = referenceHeader
        self.kMerSize = kMerSize
        self.index = 0

        self.file = open(fileName, 'w')

    def writeFile(self, queryHeader, querySequenceLength, anchor: Anchor):
        self.file.write('Query: ' + repr(self.index) + '\n')
        self.file.write('Reference: ' + repr(self.referenceHeader) + '\n')
        self.file.write('Query:     ' + repr(queryHeader) + '\n')
        self.file.write('\n')
        self.file.write(self.referenceSequence)
        self.file.write('\n')

        anchorWithMismatch = ['-'] * (len(self.referenceSequence))
        symbols = [' '] * (len(self.referenceSequence))

        matchedFirst = -1
        matchedLast = 0
        if anchor is not None:
            for overlap in anchor.overlaps:

                matchedLast = overlap.referenceIndex[0] + len(overlap.kMer)
                if matchedFirst == -1:
                    matchedFirst = overlap.referenceIndex[0]

                symbols[overlap.referenceIndex[0]:overlap.referenceIndex[0] + len(overlap.kMer) + 1] \
                    = ['|'] * (overlap.referenceIndex[1] - overlap.referenceIndex[0] + self.kMerSize)
                anchorWithMismatch[overlap.referenceIndex[0]:overlap.referenceIndex[0] + len(overlap.kMer) + 1] \
                    = overlap.kMer[:]

                if matchedFirst != -1:
                    anchorWithMismatch[:matchedFirst] = [' '] * matchedFirst

                anchorWithMismatch[matchedLast:] = [' '] * (querySequenceLength - (querySequenceLength - matchedLast))

        for symbol in symbols:
            self.file.write(symbol)
        self.file.write('\n')

        match = 0
        for element in anchorWithMismatch:
            if element == '-' or element == ' ':
                continue
            match += 1

        mismatch = querySequenceLength - match
        aligned = round((match / (mismatch + match)) * 100, 2)

        for char in anchorWithMismatch:
            self.file.write(char)

        self.file.write('\n')
        self.file.write('\n')

        if anchor is not None:
            for ove in anchor.overlaps:
                self.file.write('Reference: [' + repr(ove.referenceIndex[0]) + ', ' + repr(
                    ove.referenceIndex[1] + self.kMerSize - 1) + '] and Query: [' + repr(
                    ove.queryIndex[0]) + ', ' + repr(ove.queryIndex[1] + self.kMerSize - 1) + ']\n')
        self.file.write('\n')
        self.file.write('Match: ' + repr(match) + ' | ' + 'Mismatch: ' + repr(mismatch) + '\n')
        self.file.write('Aligned: ' + repr(aligned) + '(%)' + '\n')
        self.file.write('\n')
        self.file.write('\n')
        self.index += 1
