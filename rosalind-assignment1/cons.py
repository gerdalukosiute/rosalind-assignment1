sample_data = """"""#insert data

#func for data reading
def read_fasta(input_str):
    seq = {}
    current_label = ""
    current_seq = ""
    
    for line in input_str.split('\n'):
        if line.startswith('>'):
            if current_label: #if label not empty stores previous seq
                seq[current_label] = current_seq
            current_label = line[1:] #excludes >
            current_seq = "" #reset to store seq for new label
        else:
            current_seq += line
    
    if current_label: #checks if not empty
        seq[current_label] = current_seq
    
    return seq

values = list((read_fasta(sample_data)).values())

def profile_matrix(values):
    n = len(values[0])
    profile_matrix = {'A': [0] * n, 'C': [0] * n, 'G': [0] * n, 'T': [0] * n}

    for dna_str in values:
        for idx, nucleotide in enumerate(dna_str):
            profile_matrix[nucleotide][idx] += 1

    return profile_matrix

def consensus_string(profile):
    consensus = ''
    for idx in range(len(profile['A'])):
        counts = {key: profile[key][idx] for key in profile}
        consensus += max(counts, key=counts.get)

    return consensus

profile = profile_matrix(values)
consensus = consensus_string(profile)

print(consensus)
for nucleotide in profile:
    print(f"{nucleotide}: {' '.join(map(str, profile[nucleotide]))}")