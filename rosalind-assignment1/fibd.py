#any n,m values
n = 93
m = 17

def mortal_rabbit_pairs(n,m):
    age = [1] + [0] * (m-1)
    for i in range(n-1):
        new_age = sum(age[1:])
        age = [new_age] + age[:-1]

    total_pairs = sum(age)
    return total_pairs

print(mortal_rabbit_pairs(n,m))
