#!/usr/bin/python

import sys
from Bio.Seq import translate

def read_file(input_file):
    f = open(input_file)
    raw_input = f.readlines()
    f.close()
    return raw_input

def PTRA(DNA,protein):
    index = []
    ncbiTable = [1,2,3,4,5,6,9,10,11,12,13,14,15]
    for i in ncbiTable:
        p = translate(DNA, table=i, stop_symbol='*', to_stop=True)
        #print i
        #print p
        if p == protein:
            index.append(i)
    return index

if __name__ == '__main__':

    raw_data = read_file(sys.argv[-1])
    DNA, protein = [item.strip() for item in raw_data]
    #DNA = 'ATGGCCATGGCGCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA'
    #protein = 'MAMAPRTEINSTRING'
    print PTRA(DNA,protein)
