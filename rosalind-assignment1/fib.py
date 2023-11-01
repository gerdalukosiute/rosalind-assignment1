#recursive way
def rec_rabbit_pairs(n,k):
    if n == 1 or n == 2:
        return 1
    if n == 3:
        return k + 1
    
    first_gen = rec_rabbit_pairs(n-1,k)
    second_gen = rec_rabbit_pairs(n-2,k)

    if n >= 3:
        return first_gen + (second_gen * k)

#print(rec_rabbit_pairs(24,3))

#other way 
def iter_rabbit_pairs(n,k):
    if n == 1 or n == 2:
        return 1
    if n == 3:
        return k + 1
    if n >= 3:
        second_gen = 1
        third_gen = k + second_gen
        for month in range(4,n+1):
            new_gen = (second_gen * k) + third_gen
            second_gen = third_gen
            third_gen = new_gen

    return new_gen
#print(iter_rabbit_pairs(24,3)) 



