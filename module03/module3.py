from logic_gate import LogicGate

gate = LogicGate()
print("AND Gate Truth Table:")
print(gate.and_gate([0, 0]))  # Output: 0
print(gate.and_gate([0, 1]))  # Output: 0
print(gate.and_gate([1, 0]))  # Output: 0
print(gate.and_gate([1, 1]))  # Output: 1
