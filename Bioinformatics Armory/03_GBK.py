from Bio import Entrez

Entrez.email = "edgano@gmail.com"

#genus, start, end = open('rosalind_gbk.txt').read().strip().split('\n')
genus="Villadia"
start="2006/12/26"
end="2010/03/05"

term = '%s[Organism] AND ("%s"[PDAT] : "%s"[PDAT])' % (genus, start, end)

handle = Entrez.esearch(db="nucleotide", term=term)
record = Entrez.read(handle)
print record["Count"]

