RNA={"G":"C","C":"G","T":"A","A":"U"}

def to_rna(dna_strand):
    conv=""
    for nucleotide in range(len(dna_strand)):
        conv=conv+RNA[dna_strand[nucleotide]]

    return conv