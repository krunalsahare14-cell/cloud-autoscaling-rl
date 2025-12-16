import numpy as np

def generate_workload(t):
    """
    Simulates dynamic workload.
    """
    if t < 30:
        return np.random.randint(20, 40)
    elif t < 60:
        return np.random.randint(60, 90)  # burst
    else:
        return np.random.randint(30, 50)
