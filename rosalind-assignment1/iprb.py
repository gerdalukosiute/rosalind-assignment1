#insert any k,m,n values
k = 28
m = 20
n = 24
#total organisms
tot = k + m + n
#k_branch probability
k_prob = (k/tot)*(((k-1) + m + n)/(tot-1))
#m_branch probability
m_prob = ((m/tot)*(k/(tot-1))) + ((3/4)*(m/tot)*((m-1)/(tot-1))) + ((1/2)*(m/tot)*(n/(tot-1)))
#n_branch probability
n_prob = ((n/tot)*(k/(tot-1))) + ((1/2)*(n/tot)*(m/(tot-1)))
#total probability
prob = k_prob + m_prob + n_prob

print(prob)

