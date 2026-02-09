import numpy as np
import matplotlib.pyplot as plt

trials = 50000
dims = np.arange(2,26)
proportions = []

for dim in dims:
    det_is_zero = 0
    n = dim*dim
    #equal number of 0s and 1s (one extra 1 if n is odd)
    ones = n // 2 + (n % 2)
    zeros = n - ones
    for _ in range(trials):
        entries = np.array([1] * ones + [0] * zeros)
        np.random.shuffle(entries)
        M = entries.reshape(dim, dim)

        det = round(np.linalg.det(M))
        if det == 0:
            det_is_zero += 1
    proportions.append(det_is_zero / trials)

plt.figure()
plt.plot(dims,proportions, marker= 'o')
plt.xlabel("Matrix dimension (n)")
plt.ylabel("Proportion with det = 0")
plt.title("Probability determinant is zero from random playing (extra 1)")
plt.xticks(dims)
plt.ylim(0, 1)
plt.show()
