class DataProcess:

    def __init__(self, referenceFile, queryFile):
        self.referenceSequence = ''
        self.referenceHeader = ''
        self.querySequences = []
        self.queryHeaders = []

        self.referenceFile = open(referenceFile, 'r')
        self.readReference(self.referenceFile)

        self.queryFile = open(queryFile, 'r')
        self.readQueries(self.queryFile)

    def readReference(self, file):

        for r, line in enumerate(file):
            if r != 0:
                self.referenceSequence += line.rstrip()
            else:
                self.referenceHeader = line.rstrip()

    def readQueries(self, file):

        sequences = ''

        for q, line in enumerate(file):
            if line[0] != '>':
                sequences += line.rstrip()

            else:
                self.queryHeaders.append(line.rstrip())

                if sequences != '':
                    self.querySequences.append(sequences)
                    sequences = ''

        if sequences != '':
            self.querySequences.append(sequences)
