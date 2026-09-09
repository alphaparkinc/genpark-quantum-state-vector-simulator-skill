import math

class StateVectorSimulator:
    """
    Qubit statevector simulation.
    State represented as complex list of length 2^n.
    Single-qubit gates (H, X, Z) and CNOT.
    """
    def __init__(self, num_qubits):
        self.n = num_qubits
        self.dim = 1 << num_qubits
        self.state = [0j] * self.dim
        self.state[0] = 1.0 + 0j

    def apply_h(self, target):
        inv_sqrt2 = 1.0 / math.sqrt(2)
        step = 1 << target
        for i in range(0, self.dim, step * 2):
            for j in range(step):
                i0 = i + j
                i1 = i + j + step
                v0 = self.state[i0]
                v1 = self.state[i1]
                self.state[i0] = (v0 + v1) * inv_sqrt2
                self.state[i1] = (v0 - v1) * inv_sqrt2

    def apply_x(self, target):
        step = 1 << target
        for i in range(0, self.dim, step * 2):
            for j in range(step):
                i0 = i + j
                i1 = i + j + step
                self.state[i0], self.state[i1] = self.state[i1], self.state[i0]

    def apply_cnot(self, control, target):
        for i in range(self.dim):
            if (i >> control) & 1:
                target_bit = (i >> target) & 1
                if target_bit == 0:
                    partner = i | (1 << target)
                    self.state[i], self.state[partner] = self.state[partner], self.state[i]

    def get_probabilities(self):
        return [abs(c)**2 for c in self.state]
