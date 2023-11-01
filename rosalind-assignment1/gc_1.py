#sample input data
input_str = """"""

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

data = read_fasta(input_str)

#count gc %
def calc_gc_content(seq):
    gc_count = seq.count('G') + seq.count('C')
    return (gc_count / len(seq)) * 100

def find_highest_gc_content(data):
    max_gc_content = 0
    max_label = ""
    
    for label, seq in data.items():
        gc_content = calc_gc_content(seq)
        if gc_content > max_gc_content:
            max_gc_content = gc_content
            max_label = label
    
    return max_label, max_gc_content

#string with highest gc
result_label, result_gc_content = find_highest_gc_content(data)

#print(result_label)
#print(result_gc_content)

