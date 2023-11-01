#insert any k,N values
k = 7 
N = 38 

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
       
    return result

def prob_mendel(k, N):
    prob = 0
    twopwrk = 2**k
    for idx in range(N,twopwrk + 1):
        prob += (factorial(twopwrk)/(factorial(idx) * factorial(twopwrk - idx))) * (0.25**idx) * (0.75**(twopwrk-idx))
          
    return prob

result = prob_mendel(k, N)
print(round(result,3))



