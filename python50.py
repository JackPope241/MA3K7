import random, math
from math import comb, factorial

def simulate(n, m, trials):
    L_values = []   #holds all our results for number of loops
    Ak_total = [0] * (n + 2)
    length1_count = 0 #counter for havin exactly one loop
    mgf_sum = 0
    for _ in range(trials):
        group = list(range(n))   # each group is a string or loop. initially, we have n distinct strings so n groups
        ends = list(range(2 * n))   #labels the ends 0 to 2n-1
        length = [1] * n        #represents the lengths. we start with n strings of length 1

        loops = 0
        loop_lengths = []
        for _t in range(m):
            i = random.randrange(len(ends))  #choose a random end
            a = ends.pop(i)  #removes from list and returns list
            j = random.randrange(len(ends))   #choose a random other end to tie it to
            b = ends.pop(j) #removes this end and returns ends list
            ga, gb = group[a // 2], group[b // 2] #find the strings that the ends are from
            if ga == gb: # if the ends are from the same group then they are from the same string so a loop is formed
                loops += 1
                loop_lengths.append(length[ga])
            else: 
                length[gb] += length[ga]    #we make it so the group with string j in gets longer by adding the length of the other string
                for i in range(n):
                    if group[i]==ga: #and any string in the group i was originally in 
                        group[i] = gb  #is now in the group j was in
        L_values.append(loops)
        
        U = 1  # needed to choose a value of u for the MGF check
        mgf_sum += math.exp(U * loops) 
        
        if m == n:  #these are for the values I want when I do the process until the end
            if loops == 1:
                length1_count += 1  #counts if one big loop
            for L in loop_lengths:
                Ak_total[L] += 1  
    meannumloop = sum(L_values)/trials
    total = 0  #for calculating variance
    for x in L_values:
        total += (x - meannumloop) ** 2
    var = total / trials
    Ak = []
    for k in range(n+1):  
        Ak.append(Ak_total[k]/trials)
    return meannumloop, var, Ak, length1_count / trials, mgf_sum / trials

#formulae from my rubric
def E_Lnm(n, m):     
    result =0 
    for k in range(1, m + 1):
        result += 1/(2*n-2*k+1)
    return result
def Var_Lnm(n, m):   
    result =0
    for k in range(1, m + 1):
        result +=(2*n-2*k)/(2*n-2*k+1)**2
    return result
def MGF(n, m, u):
    product = 1
    for k in range(1, m + 1):
        product *= (2*n-2*k + math.exp(u))/(2*n-2*k+1)
    return product
def P_Ln1(n):
    product = 1
    for i in range(1, n):
        product *= (2*n-2*i)/(2*n-2*i+1)
    return product
def E_Ak(n, k):
    return comb(n, k)**2 * (2 ** (2 * k - 1)) * factorial(2*(n-k)) * factorial(k) * factorial(k-1)/factorial(2 * n)


trials = 10000000

for n, m in [(6, 6), (10, 10), (6, 3), (10, 5)]:
    mean, var, Ak, P1, mgf = simulate(n, m, trials)
    print(f"\nn={n}, m={m}")
    print("quantity, formula, simulation, difference")
    print(f"E[Lnm] {E_Lnm(n, m):.4f} {mean:.4f} {mean - E_Lnm(n, m):.4f}")
    print(f"Var(Lnm) {Var_Lnm(n, m):.4f} {var:.4f} {var - Var_Lnm(n, m):.4f}")
    print(f"MGF(1) {MGF(n, m, 1):.4f} {mgf:.4f} {mgf - MGF(n, m, 1):.4f}")
    if m == n:
        print(f"P(Ln=1) {P_Ln1(n):.4f} {P1:.4f} {P1 - P_Ln1(n):.4f}")
        for k in range(1, n + 1,2):
            print(f"E[A_{k}] {E_Ak(n, k):.4f} {Ak[k]:.4f} {Ak[k] - E_Ak(n, k):.4f}")