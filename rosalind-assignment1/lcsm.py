input_str = """"""#insert huge dataset here

def read_fasta(input_str):
    sequences = []
    current_seq = ""
    
    for line in input_str.split('\n'):
        if line.startswith('>'):
            if current_seq:
                sequences.append(current_seq)
            current_seq = ""
        else:
            current_seq += line
    
    if current_seq: #check last
        sequences.append(current_seq)
    
    return sequences

def find_longest_common_substring(strings):
    def is_common_substring(substring, strings):
        return all(substring in s for s in strings)
    
    strings.sort(key=len)  #sort the strings by length
    shortest = strings[0]
    max_length = len(shortest)
    longest_common_substring = ""
    
    for length in range(max_length, 0, -1):
        for start in range(max_length - length + 1):
            substring = shortest[start:start + length]
            if is_common_substring(substring, strings):
                longest_common_substring = substring
                break
        if longest_common_substring:
            break
    
    return longest_common_substring

sequences = read_fasta(input_str)
result = find_longest_common_substring(sequences)

print(result)