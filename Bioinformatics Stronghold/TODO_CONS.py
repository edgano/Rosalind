def profile(matrix):
    strings = matrix.split()

    default = [0] * len(strings[0])
    results = {
        'A': default[:],
        'C': default[:],
        'G': default[:],
        'T': default[:],
    }

    for s in strings:
        for i, c in enumerate(s):
            results[c][i] += 1

    return results


def consensus(profile):
    result = []

    keys = profile.keys()

    for i in range(len(profile[keys[0]])):
        max_v = 0
        max_k = None
        for k in keys:
            v = profile[k][i]
            if v > max_v:
                max_v = v
                max_k = k
        result.append(max_k)

    return ''.join(result)
    
small_dataset = """
>Rosalind_3569
TCGATGAACTTACCAACCTCAGGCGGTTTTCCGTATCTTGGGATCAAAAGGGAGGTCTCC
ATTGACTCCCCCACTGAGGATCTACAGCTAAACGGCCGATGGGCGCTCTTGTATGAAAGG
AAATGTATTCGAGTTGATGAGCGTCCTACACATCAGACTGCACCAGTAGCGTCCTTCAAC
GACAAGACTACGACCCCCAGGCGGAGGTAAACGCCATCCGTCATGGGGTGATGTGGTGGC
GGTTCTTTACGGGGTGGGTCAAGCATGCCTGTGTATTGCTAGGCTTTCTCTTGACTCGGC
TGATTTGCATTATCTAGAGCAATAAATGCCTGCGGTAGCCGTGTCTATTCTCAGAGAGAT
CCACGTAGCCTCACCGCGACTCTCCTCACTAAGCTCGTACGCGGGTGTTATTGTGTTCGG
ATTCAGTCGCGGTAGAACGAAACGAAACGCAATCAATTTCAAGGGCTACAACCTGCTCAT
CGGGCGTAGCAAAACAGATATTGTATGGTCAAGGCTCTTCCTTATCAGTGGCAATCGACT
ATGGTCTGTCGGGCTTCACCATACGGTGCTGATTCGGATCCTCCAGCCTAGACAAAAATT
AGTCTGGGCAAATAGTATGGACGAACGGCAATTCATCGCAAACCCCAGAAGCGGCCGGGC
TGTTTGTTCGCAAGCGACCCCTCCTAAGCCCGTGCTCGCGTACGGGCCCCAGACAATCTT
CGCGGGGTCTGGATTTTGTAGCCGAACGAGGCATAGGGCTTTTAACTTAAAGAATACGGA
CACTGGAGCCCGAGATAAGCACCCTGCTACCTAAGAATCATCAAAGCGCGTTTAACGTCT
CACCAACACAGCGACTGTATCGTGGCCAGGGAGCCAGTACTCCTCCTTAAAACATTCGAT
GTCACGTGGTCCACTTGAAATGTACGCGATAGACCTAATGAGGTGGCGTTGTGCTATGAC
CT
>Rosalind_1489
AGCGCAGGCTCCAGAGCAAGTTGTGTGCTGTCAGGCTCTCCCGACGTCGGACAGCCTAAT
AGTGGAAATTCGGCGCTACTGGGCTGACCGTCGCCGAAGTTTTAAAATACTAAGTATCTT
TTACACGTTAATCATTGGAATACATGCGGGATAAGATACCCCTCCCAGTCTCGGGAAATG
ATTTTTGGTCTATATGTTATTAATAGGATACGAGAACGTTAGGGGCATTGCTCTTCCTCT
GGTTACTCACAGGCAAAACTAAAGGGTGTGCTCCTCTACACCGTGCATTGGCTCATCAAT
ACAGGTGGTGCCTCAAGACCAGAATCCTCCCGGTTTTTTCGCACCAGGGTGTTGCCTGAC
GATGGGCCACAGGCTGGGGCGCTTCTTACTCACGGGACGTACAGGAGAGCCGGCTAGGCG
ATGCGGATAATCCTTCATAGGGCCGTCGGGAGTGACCACTTCGGATTTCTTACTGGGATT
ATATCCAGTCGATAACCTGACGAAACTACATGGTGTTACTAGCGAGGACATAATTCTTCT
TCGGTGCGATGCGAGGGCTTACTCGGATTTTAATCATTGCAGACGCCGGAGGTTACGTTT
CGACGTCGTTGAAGATCACGGTATGTCCCAACCATCCCTATAATGCTAAGCGACTATAAC
TAGCAAATCGGTGCCACTCCTACTACGTACTGCAAGCTAGAGTCGAGCCTGCGGGCATCA
AGTAGCGTTGATTGGTTAGTCGCGGCAGGGAGAAAACTCTAACGACGTAAACTTATCGCG
GGGGCGCATGGCTAGTCCGGGAGCTTCCCCCGTCAATCGTTTCGCTTGCTAATTTCCTAG
AGGGTATGCATTGCATTAAGTGCACTCCCGTACGCCTCGGTCTAAGCATTCTAACCGAGG
AACGGCGGACGCCATATTCGAGACGCGGCTCGTCCGCATCGGACAGAGCATCTAGCGTGT
GT
>Rosalind_4072
CCGATAGTGTGATTTTGCCTAACAGTACATGCTATGTAGGCAACAGACATTACGTGTAAG
TAGAACTGGGTACAGACGGCACATGCTAGTCGGTTAATTATAGCGATCTTACTCTATGCG
TATGCTATATACTGATTCGCCGCGTCCGCAATGATTATTTAGCCGGTCCTCTTTGCACAA
TCTGCTATGTCCAGATAGTTTTCGCTACTGTGGAGAGTACAGTAAATTAACACCTATGAA
GAGGCTCGTTTACAACGCGTTCCCCCTCTTCTGATGATGTCAACTGACCAATCAGAGCTG
TAAGCACGATGAATATGTCTGGGTAGCCGCCATCGGGGGCCAAGTTGACTCGAACGCATA
GTCACGAAGTAGACGGTGGCCAGGGGGATTATAAGGAGCGCGATAGGCGATCACGATGTG
CAGGGCGCAATTTACTAATGACAAAAGCAGGGGGGTCAGGTGTCATAGTTAAGCCTGTCC
GAAGTGTTAGTAGCGCGCACAACTTCTAAGGGAGGTACCCGCGAAACACAGTACACGCGA
CTCATGCAGAGTAGGGTGACCTCATATATCAAAAACTCATCGATTCCCAGCCCCCAGAAT
ACTTTGCCCTCCATGCGTCCTTCAGGACCCCACATGGTTATAAGGGTGCTGAGACCACCA
GCGGTCCCCCCCATTGACGGGAAATATCTGCCCATGAGCAACCACTTCTTATTGGACATT
ACTCGGGAGGCCCGACAAATGGCCAGATTGACGGTCAATTTCTGAGGATCGGCGACCGGA
TCCCTGCGAAGATCTTAAGCTCGGAAGGTCTAGCGCACCCATTCCGGACTAACTTAGCCT
CAGCAGGAGAAAATAAGTGAGGACTGTTGGGGTTACGATGCCGCTCGCCACCTGCACGCA
GGTATCCTGTTAACCCGCGGCTTATTAATTAACTACTCTAAACATATATCTCTCTGCTGA
GG
>Rosalind_3442
TCGAGTAGGTACTAAGCGGCGGCACAGTGCGATAGATCGCTAACGCCCTAAGTGCATAGC
CCTCGAATGGGTGAACACGAGCATGTTGCCTGCTATTCTAGTTTATTTGGGCATCTGCCT
TAACCGATCTGAGAGACTACGCAATGCCATAAACGGGCACGGATAGGTGAATTACCAGAA
CGTGGCAGCACCAGGTGGTGGATGCGGTTAACTGAATATCCAGGAAGAAGTGCCCTGAGT
TCTTTAATGCGCCTCCGCACAGCCTTTTCGCTGCTTGAAACGTATAGAACTGGGGAGCTT
ATAGAACCGCCATGTTAATGACGGGTTCGCGATCTCCGCCATGGTGACGCAGTCATGATG
CGTTGTCTAGTAGAGGTTACTACTACCCGGCTTATCTTGGAATTAACGTAGCACCCTTCA
TTGGGGGGATGGATCTCCCGCCCACGAGGGGATCACACGGAATAAGCTCGCAAAGAGGCA
GGCCCCGTGTGGAATTTTGCACGATCAGGGCTATTCAATACTCCGGATGTTAGCTCAATC
AATAGTACAAGGGCGTCGGTAAGGATCTGAAGAGTTTGCGCTGGGTCTCGTAACCGTGCC
TCATACCACAAATAGCGGCAAGCACGTACGAGGCAGCTGGGTGGCCACAATCAATCGAGT
TCACCCACCCATGGTATGTTTGTTAGCGTCCGACATCCTCCAACTAGAAACGAAAGGACC
CGCGGAGTAAGGATCGTTTTTCTCGGGCTAGGACTGATATGAGTTGTGACTTGACGTAGG
GTAACTCTCCCGCAGCTTCTCTTATCCACTACACCAACAAAGAGTAGGTCACGCGACGAA
TCGCTAATGTGACGGAACCTAACGTGCTGGGCTCTAACACAACGCGGATAAGAAAAGAGC
CATGCACGTCGTTAATGCATATCAATAGGAAGACAAGGCAGCATCACTATAGCTGGTTAA
GC
>Rosalind_8036
CGCGTGTCTCAGTGTTTATTAACCTACGACTTGATGACTTCGCAACACTTCGTGTCCTTT
AACGCCATCAAATTCGACATACGACAGCCCTCCCGAGTTCTGATCTTCATCGGACTTCTC
AACTTCTGTCCTAGACCCACCTGTGCACGTTATCAATGCCATGCCCAAAAGGCCTCCGTC
TAATGACCCCTGCCTCCCGCCAACGATTAGTTTGATTTATCCGCCCTGTCACAACGTACT
CCCCTTTGAAGAGGGCAAGCGGTGCGTTCATCCTACACACGAATTCTCCGCTTTCTGACT
GTTCTCTGGGGTCTTTTTGATTGCCCTAATTCATTGGTCCTTCTATACCGAGGAGATGGC
TATTACTATCGCGCTCATGTGCAACTTTTGACTCGTTTAGCGCTTCGGCAACGCCCGGGG
CGTGGGATAAAGCTTCTAATTAGTCTTTACTCTTACCTATTTCCGAGATTAGGAACCCAT
TCTGCGCCACGCGTAGGAGACAGTCTCGTAGGTTACAGTACCTGGTTCTTCCATATTAAG
CAGACAGCCGATACATGGACATTCAACCGCGCCTCCCTACGCCGCAGGGAACGATTAGGA
CCGTTCGAACGTTGTTGAGTCTATCCCATGCCTATATATTACGAACCTACGAGAGTTGAA
TTCTGGGGCAGATTTTATCAGGAGTGTGTTCCGGCACGGGAAGGTCGCTAATAAGAACTT
CTCACCGGGTGGAGGTAGGACAATGTGAGAGAGCCGTTGCAATCATCGTCCTTTGCTGGG
TACTTGAACAACGGTCTATTACAACGCAGTTAGAGCAGGCAACTTTGTTGCCGCCGTAGA
CGTCGAGCATCGACAGTTAATCTCGTAACCAAACCTATGTCTAGCGGTTATCCAGATTTT
CACCGTCCGGAAGTACTAATTGGTTCAGGGGCTATTCCTACCGTATCCATCCCCGAGGGG
AA
>Rosalind_2556
GCGTAACCCTTACTCCTAGCAACATGGCACTAGCGCGCCATGTGTGCGTGATGTTAGCCA
GGCGTATGAAAGATACGAGGGGAACCTTACATCAGTCCGCGTGAGTAGAGCGGGGTGTCC
TTTCGCTTCTCCACATAGATGTGGGTGTGCTTGTCGCGTGACAACATAGTGCCCGAAACT
AACGAATTTACCCAACATTGTGGGGCTATATGGTAGGGTTGTGCGGTCCAGTTTACTTCA
CGTTTACGTCCTCTCAGCGGCCGGCCCGTCTACTTGATCCGGAACGTCATCGGCCAGTAT
GGCCGTTCTAACACTGGACTATCTTCCGGATTGGTAAGAGTGCCTGTCAAGCAATCCCAG
AGTACCCTAGAGCGTTCATACCTTCCGAAATTTGAAACCAATTTCTAAATCCTGCGAAAG
GTATTGTCGTACTAATACTCCGCTGGATTGGGGGGTGCAGTGCGGATCGATGGTTATCAC
GGATTCGTTACGGCGCTATGACTCCTCTAAGCATTGGACTTAGGACCTGCTTCCATAGCA
GGGGCCAGGTTACTACAAGCCCAGGACTACGTACATTTTGGGCTACCCCAATATTTGTCT
AAAGAATCAGGGCGGGAAGCACCTAGTAAAGCGGAAGAATCATGTCGGTGTCCTCTAAAC
ACACAAGTAAGATCCAGCGTGCAAGCGGTTTCGGGCTACCCCTCCGTGGATGCACTGTCG
CCAAGCGGTGTAAAGCTGCAGTCCCACCGGGTTTGGCTCCAGCGATCAGACGGGTACCTC
TTCTGACCTGTGGCGTCTTGTAGCTAATTTAGGAAACGCCTTTCCTCCACCAGATGACAG
TGCTCCGGTATTTCGACTGAGCATGGAGACGGATAGTTCAGATCCGATGTAGATGAACAA
AGCGCGGTTTCGGAGTTCAATTCTATCCGCCAAAAGTCTTGTAATTATTATAGTCATAAG
AG
>Rosalind_2983
TGTGACTTCAATGACTTAAGCAGCGACGGGGCTACTGAGTGAATAATCAGTTGGACTTTC
CTTGTGTATAAGGGCGGACGCGGTGGTTCCACTACTCGCCACGGTTCATTGTATCTGCGG
CCTCCTCCCGAGAGGTGTCCACTCTTCGTAAGATGTCGTTTCTCGGCGCTTAAGAAGCAT
CAGTACGACAACGCTGATACGATTTTCCTAAGGTCATGGATACTTGCAGGTTGGACTGTC
AGCCGTGCCTTGCAATAGGGGTCCTCTCTCGCCTGACAATTATGGTCAAAATACACGTCC
AGGACAGATAAGCAGCCCCTCCACGCGATTACGGCAGCGATACCCTCAAGTCGCTAGTCA
AAGTTAAGACTCCAGGCCAACAAGAACGTACGTCCTCAGCCTGGGTATGGGCTTATGTCC
TAGTACACGGCCTTCTGCATAGTAGTTAAACTTCGGGGGTAAAAACGTTGGAGATGCCCA
GACTGGTTAGGTAGAGGGAGAAGATTGCTGCTAAACAACAATTCCTGCCCCTCCTTGAGT
GGAGCGCTAGCGGGGAGTTCAGAGTCTGCCGGTGCTATTTCCGTGGCAGGGAGGTAGCAG
ACGACTTCAATAATGAAGGTACAATAGTCTTAAGTGGTGCCAGTCGTATACGTGCACGTG
GGATGCGGATGCGCCTGCAAAGAAGAGTACCACGCCGACTAAGCGGCGAAGGTGTGCCAC
TGGTTTGTTATATATTCTGCATGTTATCCGGTAGAGGTCGAAACCGTCACGTCTTTAATG
ATAAATCACTGCTAACCCCATGATAACCGCCTGGCGGCCTAAGAATCATAGAGTGAATTT
AAGTTTATGAATTAAGGACATCTGTTGCTTGAACGCAATTGCGTTGAGGGGAACTAATGT
CCATCAAGATCCTAAAATGACGCGGCCATCATATACTCTCGGTTGCCCCAGTTGCGCGTT
AA
>Rosalind_1113
GACTGAAGGGATGCTGGGTACAGCCTCCATGGTCTGTCGATTGGGGGTATGAGGTCGAAC
CCGAACCGTCTAAGTACGAGAGCGGGGGACATTAACCGGATAGGGAAGGCAAGTGGAGAG
CCGGTGAACGAATGAGAAGAAGACGGTCGTCGCATTTAATATGCAATTGTCCGAGTATCA
AAGACACGGATTAGGGAAGCGAGATGTTCCCTCCCACTTACAGGTTACGGCTGGGTAAGG
ACGTTCGCTAAAGGGGATGCTCGGTGGTCAGGGCATCTACTTCTGTGTAATGCGTGCCAG
TCTGTCTCTGTGGGCGGCAACATCTGGAGCTTAGAGAATCTGGAATGTTGTAGGAATATA
GTTCGTAGAATAGTTGGTCACCCTGTGTGTCCACGAGCCGTCAGGCGCCATAGTTCGTAT
AGAACCCCGTTACCGTGGTTCATTAGCGGGTCGTTTGGGGATCTTCAATCCTCGTAGTGA
GCGATTTCGGTGTTCCGATATTAGCGTGACGAGCGGTGACGAACCCGCACAGTGGGTCGT
TTCACAACTGACCTAGTTACATCTAGCGCGTTGATACCTTGATAGCTAAAAGAATTGACC
GTGTGCACAGTTCTCGCCATGCACGCGGGTTTATTGTGCCGGTGTATCTTACGGGCTAGG
TACGCTTATCGGCTATTTTACCTCATTAAGCTGCCGTCTTGAGATGTGTGGTGAACGGCC
TTCCTCTCTATGGGAGGTGACAGGTGATAGGTCACCACGAACTGGCTCGTATGTCAGTTA
AGCGGAATGTGCAGAAAATTGTCAATACATATTAACTTATAGAGACGACTATTATTTGGT
TAGCGGCGAATGACCAAGATGTAGCAAAAGCGGAAGGCAATGGTACCTAGTTAGATTGAT
ACCTGGCTCATAGAAGACGTCTATATTCCCCCTTTTGGGGGTGCTTTTCCATTAATCCCC
GG
>Rosalind_6517
CCAATTGGGCAGTCACTAGAAGAACTCATTAGTACTATTCTCTCGTCCGCGAAGTTCTGT
AAGCCGGGGGCCCAAATATATGGTGCCGGCCCTTCAACCGCCTAGAGCGTTATTGTTTTT
TCATTAGTGGAATAAACCGATCTGAGCTTCTATTAGTCGGTTCAACGGTATCGATCTCGG
CAAGCCTACATACTGGCAATTAGGCCCTACGATGTGGGATCTCACCATCTGCAAACTGAT
GAAAACGCTTTCGGTATTTACTTGAGGGATTACAAATAAATTCTTCATCCCGCTTTTGAG
ATCACTTTAACGGCTGTAGGCAAGCAAATGAATAATATCCGATGTATGGCATTATAAGAA
ACTGTCATTTTATCCAAACCTTAATAGATACCATGTATCTATTCTATTTGAGAACGGCCA
GTGCTCATGGTCAGGCACGCGTGCGAGAAACTCCGGGTCCCACCAGTGAGACCGCAGACT
AAGAAATGAATCAATTATTAGGGTGTAAATTACTGTGGGGTACCTATCCCGCCGGGCAAC
GCATCCCTGTGCTCTCCCATCAATATTCAAGGGTCGACACACCCACGAGTGGTTACCTCA
CAGTTCCGACAGTTTGAGCTAACAAGTCGTATGCGTTCCAAAGCCGATAGGTGGATTTTT
GTGTGCGTCTAACTTTCTATGTTCAGCATGGACGGCGTCGGTACATGGCCCCACCCGATT
TTTCCCGCTCCTTCGTCGCTCGCTCTCCCAAACATTCAAATTTAACGGACCGTAATGCTT
CCACGGTGTGTAAGAATTGAATGGCTCAAGCCGTTTTTACTGGATTCGCTCTACTTTGCG
CTTAACCGCAACGACCAGTATCACCTTTCCTGCTTGACGCACAAATATTCTTTGTGCTCC
AGTGTGCCAAGGAGAGCTCTTCACCAGATGAAATGAGGTACTACTATACTGGCAGTCCAA
GT
>Rosalind_4666
TTCCCGCACTCTCGTTTTCTATTCATTTACAAGCGGACCGACCCCGACTCGTAATCCGTG
GGTACCATGAAACTATAGATTATAGCATCCGGTGGGGAGCGGGCTGGTCTCATGTCTCTC
GAGGTCTCGGCTTCGAGGGTCTAGGCGAAAGCGTTTGCAACCGCCTTCAACGGGCAAATC
TGGATGGTAAACGTAAAACACGACGACATCAGATTCCAATCTGGTGCTTATATACTAGGA
TTCCGATTAGTTACGGCGCTGAGAGTAGCGATTAGCTCGCGGTGGATGAACACCTGTTAA
GGAGGTCACTCGTAGAGCCACTCCCCAACTTTCGGCGTTTTACATCCTATAACAAGACGA
AATATTAGAAGATAATTCAATGTCCGTTCGCGAATCCCGAACAGTTGTCGTTTGTATTAC
CTTGGAGTTCGCTGGCCTTGGTTGATTTGGCATCCAGGCTGGACTCATCTGAGTTACGAT
TGGTACCCTGATCTCCGGTACGTTTGGTGTAATCCTTTGACGTCCCCCCGGCGCTATCCC
CAGTCTGCATCAAACAACTCAACCTATGGTATGATTGTCCGTGATTGATGTGTCTCCACT
TAACGGTGAGGGGATAATACTGCCGGGGACTATGCGGTGAATTTATGACTTGGTGCGACG
TGAACAGGGCACGGCTACCTCACTTTTGCTACGCCATAGTCTTGGAGCCGGGCCGCAAAC
GATCAGTTGTCGACACCGTCGGTGACCTAGGCGTCCGGTCCATGTCGAATTACCCAATGT
AGTTCTGTCTGTATGAGTTCGGAATCGGCCGAGGCGACACGTCCTGAGTTTCACAATCCA
TGAAATTGATTTCGTGGAGCGAGAACTAAGTCTCGCGAAGAACTAGGTTCTTGTCACCGA
AATGCCTGCGCGCACGCATAGCACATTATCTTCGCGCGCATAGAAGGCCTCGCGAGTTGG
CA
    """

p = profile(small_dataset)
c = consensus(p)

print c
for k in sorted(p.iterkeys()):
	print "%s: %s" % (k, ' '.join(map(str, p[k])))