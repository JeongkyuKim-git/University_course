import sys
import math

if __name__ == '__main__':

    print('Reading Sequence File...')
    referenceSequence = ''
    referenceFile = open(sys.argv[1], 'r')
    referenceHeader = ''
    for r, line in enumerate(referenceFile):
        if r != 0:
            referenceSequence += line.rstrip()
        else:
            referenceHeader = line.rstrip()

    print('Splitting Sequence...')
    kFold = int(sys.argv[2])
    splitSequences = [''] * kFold

    end = math.floor(len(referenceSequence) / kFold)
    start = 0
    for i, sequence in enumerate(splitSequences):
        splitSequences[i] = referenceSequence[start:end]

        if i == kFold - 1:
            splitSequences[i] = referenceSequence[start:]

        start = end
        end = end + math.floor(len(referenceSequence) / kFold)

        # print(splitSequences[i])

    print('Writing to File...')
    for x in range(len(splitSequences)):
        output = open('split-' + str(x) + '.fasta', 'w')
        output.write(referenceHeader + '\n')
        output.write(splitSequences[x])

    print('Done')
