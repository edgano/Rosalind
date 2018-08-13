from __future__ import print_function
from Bio import SeqIO
import sys 

# grabbing the file and the name 
seq_file = sys.argv[1]
labels = seq_file.split(".")

# converting the file from fastq to fasta
SeqIO.convert(seq_file,"fastq",labels[0]+".fasta","fasta")


# taking the converted file and then changing the fasta header
for seq_record in SeqIO.parse(labels[0]+".fasta","fasta"):
    print(">",end='')
    print(seq_record.id)
    print(seq_record.seq)
