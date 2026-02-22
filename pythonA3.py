import random
import matplotlib.pyplot as plt

def game():
    hat = list(range(1, 2027)) 

    while len(hat) > 1:
        a, b = random.sample(hat, 2)
        hat.remove(a)
        hat.remove(b)
        hat.append(abs(a - b))

    return(hat[0])

for i in range(50):
    print(game())

trials = 100000

results = [game() for _ in range(trials)]

# histogram
plt.figure()
plt.hist(results, bins=range(min(results), max(results) + 2))
plt.xlabel("Number final piece of paper")
plt.ylabel("Frequency")
plt.title(f"Final values over {trials} runs")
plt.show()


