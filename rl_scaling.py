import random
import numpy as np

class RLScaler:
    def __init__(self, epsilon=0.2):
        self.q = {}
        self.alpha = 0.1
        self.gamma = 0.9
        self.epsilon = epsilon

    def state(self, util, vms, predicted_load):
        u = 0 if util < 0.3 else 1 if util < 0.7 else 2
        p = 0 if predicted_load < 40 else 1 if predicted_load < 70 else 2
        return (u, vms, p)

    def act(self, s):
        self.q.setdefault(s, [0, 0, 0])
        if random.random() < self.epsilon:
            return random.choice([0, 1, 2])
        return np.argmax(self.q[s])

    def learn(self, s, a, r, s2):
        self.q.setdefault(s2, [0, 0, 0])
        self.q[s][a] += self.alpha * (
            r + self.gamma * max(self.q[s2]) - self.q[s][a]
        )
