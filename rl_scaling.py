import random
import numpy as np

class RLScaler:
    def __init__(self):
        self.q_table = {}
        self.alpha = 0.1      # learning rate
        self.gamma = 0.9      # discount factor
        self.epsilon = 0.2    # exploration rate

    def get_state(self, utilization, vms):
        if utilization < 0.3:
            util_state = 0
        elif utilization < 0.7:
            util_state = 1
        else:
            util_state = 2
        return (util_state, vms)

    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.choice([0, 1, 2])
        return np.argmax(self.q_table.get(state, [0, 0, 0]))

    def update(self, state, action, reward, next_state):
        self.q_table.setdefault(state, [0, 0, 0])
        self.q_table.setdefault(next_state, [0, 0, 0])

        best_next = max(self.q_table[next_state])
        self.q_table[state][action] += self.alpha * (
            reward + self.gamma * best_next - self.q_table[state][action]
        )
