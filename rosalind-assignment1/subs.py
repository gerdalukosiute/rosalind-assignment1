s = ""#string here
t = ""#substring here

def substr_counter(s,t):
    pos = []
    for i in range(len(s)-len(t)+1): #impossible for t to be sub if len(t)>s
        if s[i:i+len(t)] == t:
            pos.append(i+1) #idx from 1
    return pos

print(substr_counter(s,t))

