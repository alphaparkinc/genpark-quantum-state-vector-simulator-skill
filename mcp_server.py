import sys
import json
from client import StateVectorSimulator

def handle_call(name, arguments):
    if name == "simulate_bell":
        sim = StateVectorSimulator(2)
        sim.apply_h(0)
        sim.apply_cnot(0, 1)
        return {"probabilities": sim.get_probabilities()}
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_call(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"id": req.get("id"), "result": res}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
