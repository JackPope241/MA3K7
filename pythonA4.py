#
import numpy as np
n = 25
A = np.zeros((n,n))
b = np.zeros(n)

for i in range(23):
    A[i, i]= 1
    A[i, i+1]= -0.5
    A[i, i+2]= -0.5
    b[i] = 0
A[23, 23]= 1
A[24, 24]= 1
b[23]=0.5
b[24]=1

P = np.linalg.solve(A, b)

print("Fair coin:")
print("P_1 =", P[0])

#Extension section, unbiased coins
for x in range(1,11):
    x = x/10
    p1= (1-(x-1)**25)/(2-x)
    print(f"For x={x}, P_1 = {p1}")

#

