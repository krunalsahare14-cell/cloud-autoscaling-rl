import numpy as np
from collections import deque

history = deque(maxlen=5)

def generate_workload(t, mode="bursty"):
    if mode == "steady":
        load = 40
    elif mode == "periodic":
        load = 30 + 20 * ((t // 10) % 2)
    elif mode == "random":
        load = np.random.randint(10, 100)
    else:  # bursty
        if t < 30:
            load = np.random.randint(20, 40)
        elif t < 60:
            load = np.random.randint(60, 90)
        else:
            load = np.random.randint(30, 50)

    history.append(load)
    return load

def predict_workload():
    if len(history) == 0:
        return 40
    return sum(history) / len(history)
