sequence = ""#insert sequence
dict_count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
for symbol in sequence:
    dict_count[symbol] = dict_count[symbol] + 1

print(dict_count['A'], dict_count['C'], dict_count['G'], dict_count['T'])
