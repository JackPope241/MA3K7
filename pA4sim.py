import random

trials = 10000000
hits = 0

for _ in range(trials):
    position = 1

    while position < 25:
        position += random.choice([1, 2])  

    if position == 25:
        hits += 1
#
print("Estimated probability =", hits / trials)