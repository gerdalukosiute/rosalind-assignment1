sequence = ""#input sequence here

dict_conversion = {
    "A" : "T",
    "C" : "G",
    "T" : "A",
    "G" : "C"
}
new_sequence = ''
for pos in range(len(sequence) - 1, -1, -1):
 #-1 in middle because T at the end of sample sequence given on rosalind gets cut off
    new_sequence += dict_conversion[sequence[pos]]
print(new_sequence)