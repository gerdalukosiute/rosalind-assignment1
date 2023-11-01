def rna_to_protein(rna_string):
    rna_codon_dict = {
        "UUU": "F",      "CUU": "L",      "AUU": "I",      "GUU": "V",
        "UUC": "F",      "CUC": "L",      "AUC": "I",      "GUC": "V",
        "UUA": "L",      "CUA": "L",      "AUA": "I",      "GUA": "V",
        "UUG": "L",      "CUG": "L",      "AUG": "M",      "GUG": "V",
        "UCU": "S",      "CCU": "P",      "ACU": "T",      "GCU": "A",
        "UCC": "S",      "CCC": "P",      "ACC": "T",      "GCC": "A",
        "UCA": "S",      "CCA": "P",      "ACA": "T",      "GCA": "A",
        "UCG": "S",      "CCG": "P",      "ACG": "T",      "GCG": "A",
        "UAU": "Y",      "CAU": "H",      "AAU": "N",      "GAU": "D",
        "UAC": "Y",      "CAC": "H",      "AAC": "N",      "GAC": "D",
        "UAA": "Stop",   "CAA": "Q",      "AAA": "K",      "GAA": "E",
        "UAG": "Stop",   "CAG": "Q",      "AAG": "K",      "GAG": "E",
        "UGU": "C",      "CGU": "R",      "AGU": "S",      "GGU": "G",
        "UGC": "C" ,     "CGC": "R",      "AGC": "S",      "GGC": "G",
        "UGA": "Stop",   "CGA": "R",      "AGA": "R",      "GGA": "G",
        "UGG": "W",      "CGG": "R",      "AGG": "R",      "GGG": "G",
    } 

    a_a_seq = ""
    for i in range(0,len(rna_string),3):
        codon = rna_string[i:i+3] #extracting 3 nucleotides
        if codon in rna_codon_dict:
            a_a = rna_codon_dict[codon]
            if a_a == "Stop":
                break
            a_a_seq += a_a

    return a_a_seq

rna_string = ""# input rna string here
print(rna_to_protein(rna_string))

