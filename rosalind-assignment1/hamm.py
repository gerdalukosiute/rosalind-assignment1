s = ""#1st string
t = ""#2nd string

def hamming_distance(s,t):
    hamming_pos = []
    if len(s) == len(t):
        for idx in range(0, len(s)):
            if s[idx] != t[idx]:
                hamming_pos.append(idx)

    pos_counter = 0
    for num in range(0, len(hamming_pos)):
        pos_counter += len(hamming_pos)
        return pos_counter

print(hamming_distance(s,t))
    