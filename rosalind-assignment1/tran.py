input_str = """"""#fasta input here

def fasta_transition_transversion_ratio(input_str):
    seq = {}
    current_label = ""
    current_seq = ""
    
    for line in input_str.split('\n'):
        if line.startswith('>'):
            if current_label: #if label not empty stores previous 
                seq[current_label] = current_seq
            current_label = line[1:] #excludes >
            current_seq = "" #reset to store seq for new label
        else:
            current_seq += line
    
    if current_label: #checks if not empty (for last)
        seq[current_label] = current_seq
    
    values = list(seq.values())

    s1 = values[0]
    s2 = values[1]

    transitions = 0
    transversions = 0

    for base1, base2 in zip(s1, s2):
        if base1 != base2:
            if (base1 == 'A' and base2 == 'G') or (base1 == 'G' and base2 == 'A') or (base1 == 'C' and base2 == 'T') or (base1 == 'T' and base2 == 'C'):
                transitions += 1
            else:
                transversions += 1

    return transitions / transversions

ratio = fasta_transition_transversion_ratio(input_str)
print(f"{ratio:.11f}")