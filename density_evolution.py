import matplotlib.pyplot as plt

"""
REGULAR LDPC CODES 
i.e. all check nodes have same degree, d_c, and all variable nodes have same degree, d_v
"""
d_c, d_v = 6, 3                     # degree of check nodes and degree of variable nodes

epsilons = [0.4, 0.41, 0.425, 0.43]        # epsilon (probaility of erasure)
for e in epsilons:
    p_ts, steps = [], []    # list to hold the fraction of erasures at each step t

    p_t = e              # at step t = 0, fraction of erasures is epsilon
    for i in range(50):   
        p_ts.append(p_t)
        steps.append(i)
        
        p_t = e*(1-(1-p_t)**(d_c-1))**(d_v-1)
    
    plt.plot(steps, p_ts, label=e)

plt.title(f'Regular LDPC Code with d_v={d_v} and d_c={d_c}')
plt.xlabel('Number of steps, t')
plt.ylabel('Fraction of erasures remaining, p_t')
plt.legend()
plt.show()



"""
IRREGULAR LDPC CODES 
i.e. check nodes have different degrees and variable nodes have different degrees
lamda is the degree distribution polynomial of the variable node degrees from the edge perspective
row is the degree distribution of the check node degrees from the edge perpective
"""

def lambda_(x):
    return (25/41)*x + (10/41)*x**2 + (6/41)*x**3

def row_(x):
    return x**5

epsilons = [0.325, 0.327, 0.328, 0.33]  
for e in epsilons:
    p_ts, steps = [], []    # list to hold the fraction of erasures at each step t

    p_t = e              # at step t = 0, fraction of erasures is epsilon
    for i in range(1000):   
        p_ts.append(p_t)
        steps.append(i)
        
        p_t = e*lambda_(1-row_(1-p_t))
    
    plt.plot(steps, p_ts, label=e)

plt.title('Irregular LDPC Code')
plt.xlabel('Number of steps, t')
plt.ylabel('Fraction of erasures remaining, p_t')
plt.legend()
plt.show()
