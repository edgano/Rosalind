from Bio import SeqIO
from math import *

import sys
import StringIO

def phre():
    with open("fastq.txt") as f:
        th = int(f.readline())
        fastq = f.read()

    with open("foo.fastq", 'w') as f:
        f.write(fastq)

    records = SeqIO.parse("foo.fastq", "fastq")

    num_rec = 0 # num records whose avg quality is below threshold
    for rec in records:
        qs = rec.letter_annotations['phred_quality']
        if float(sum(qs)) / len(qs) < th:
            num_rec += 1

    print num_rec

if __name__ == '__main__':
    phre()