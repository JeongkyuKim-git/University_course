import sys
import time

from Core.DataProcess import DataProcess
from Core.SeqAligner import SeqAligner
from Core.OutputFile import OutputFile

if __name__ == "__main__":

    REFERENCE_FILE = str(sys.argv[1])
    QUERY_FILE = str(sys.argv[2])
    KMER_SIZE = int(sys.argv[3])
    OUTPUT_FILE = str(sys.argv[4])

    TIME_START = time.time()

    data = DataProcess(REFERENCE_FILE, QUERY_FILE)

    output = OutputFile('Final/' + OUTPUT_FILE + '.jres',
                        data.referenceSequence,
                        data.referenceHeader, kMerSize=KMER_SIZE)

    aligner = SeqAligner(kMerSize=KMER_SIZE)
    kMerRef = aligner.kMer([], data.referenceSequence, 0, seq='R')

    for q, query in enumerate(data.querySequences):
        kMerQuery = aligner.kMer([], query, 0, seq='Q')
        overlap = aligner.overlap(kMerRef['kMers'], kMerRef['index'], kMerQuery['kMers'], kMerQuery['index'])
        anchor = aligner.bestAnchor(overlap)

        output.writeFile(data.queryHeaders[q], len(data.querySequences[q]), anchor)
        aligner.clear()

    print('Total Execution Time: ' + str(time.time() - TIME_START) + ' sec.')
