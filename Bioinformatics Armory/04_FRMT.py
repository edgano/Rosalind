from Bio import Entrez
from Bio import SeqIO

Entrez.email = "edgano@gmail.com"

handle = Entrez.efetch(db="nucleotide", id=["JQ342169, JX308815, NM_001003102, JX308803, NM_001135551, NM_001185098, JX393321, JQ867090, NM_001246828"], rettype="fasta")
records = list (SeqIO.parse(handle, "fasta"))

minLenght =len(records[0].seq) 
minId = 0
for i in range (0,len(records)):
	if minLenght >= len(records[i].seq):
		minLenght = len(records[i].seq)
		minId = i
#return min

print ">",records[minId].description
print records[minId].seq