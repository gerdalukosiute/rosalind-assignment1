sequence = ""#sample sequence here

new_sequence = ''
for symbol in sequence:
    if symbol == 'T':
        new_sequence += 'U'
    else:
        new_sequence += symbol

print(new_sequence)