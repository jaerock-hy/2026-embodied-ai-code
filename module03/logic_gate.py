import numpy as np

class LogicGate:
    def __init__(self):
        pass

    def and_gate(self, x):
        w = np.array([0.09, 0.05])
        th = 0.1
        return 1 if np.sum(w * x) >= th else 0
    
        w1, w2, th = 0.09, 0.05, 0.1  

if __name__ == "__main__":
    print("AND Gate Truth Table:")
    gate = LogicGate()
    print(gate.and_gate([0, 0]))  # Output: 0
    print(gate.and_gate([0, 1]))  # Output: 0
    print(gate.and_gate([1, 0]))  # Output: 0
    print(gate.and_gate([1, 1]))  # Output: 1