import numpy as np
import random

def run_simulation(max_steps):
    state = 1
    history = [state]

    for step in range(max_steps):
        if state == 9:
            print("Reached state 9. Process ends.")
            break
        p_forward = 1 / state
        r = random.random()
        if r < p_forward:
            state = min(state + 1, 9)
        else:
            state = max(state - 1, 1)
        history.append(state)
    return history
for i in range(10):
    print("Visited states:")
    print(run_simulation(100))