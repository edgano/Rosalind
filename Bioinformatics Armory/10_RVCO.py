###
#Problem
#
#Recall that in a DNA string s, 'A' and 'T' are complements of each other, as are 'C' and 'G'. Furthermore, the reverse complement of s is the string sc formed by reversing the symbols of s and then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").
#
#The Reverse Complement program from the SMS 2 package can be run online here.
#
#Given: A collection of n(n≤10) DNA strings.
#
#Return: The number of given strings that match their reverse complements.
###
import sys
from Bio import SeqIO

def read_file(input_file):
	record = SeqIO.parse(input_file, "fasta")
	return record

def rvco (raw_data):
	count=0
	for record in raw_data:
		if (record.seq == record.seq.reverse_complement()):
			count+=1
	return count

if __name__ == '__main__':
    raw_data=read_file(sys.argv[-1])
    print rvco(raw_data)