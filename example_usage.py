from client import StateVectorSimulator

def main():
    print("=== Testing Quantum Statevector Simulator ===")
    sim = StateVectorSimulator(2)
    sim.apply_h(0)
    sim.apply_cnot(0, 1)

    probs = sim.get_probabilities()
    print("Measurement probabilities for Bell State (|00> + |11>)/sqrt(2):")
    for idx, p in enumerate(probs):
        print(f"  |{bin(idx)[2:].zfill(2)}>: {round(p, 4)}")

    assert abs(probs[0] - 0.5) < 1e-5
    assert abs(probs[3] - 0.5) < 1e-5
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
