from Bio import Entrez
from Bio import SeqIO

def genbank(*genbank_ids):
    """Fetches each genbank id and creates a file ready to upload in FASTA"""
    Entrez.email = "adelq@sas.upenn.edu"

    for i, genbank_id in enumerate(genbank_ids):
        handle = Entrez.efetch(db="nucleotide", id=genbank_id, rettype="fasta")
        fasta = handle.read()
        with open('NEED{0}.fasta'.format(i), 'w') as f:
            f.write(fasta)

if __name__ == '__main__':
    print genbank("JX569368.1", "JX469985.1")

##
#1)  Go to EMBOSS's Needle tool: http://www.ebi.ac.uk/Tools/psa/emboss_needle/nucleotide.html
#2)  MATRIX: "DNAfull"
#3)  GAP OPEN: 10
#4)  GAP EXTEND: 1.0
#5)  OUTPUT FORMAT: "pair"
#6)  END GAP PENALTY: true
#7)  END GAP OPEN: 10
#8)  END GAP EXTEND: 1.0
#9)  Click "Submit"
#10) Score is next to "Score:"
##