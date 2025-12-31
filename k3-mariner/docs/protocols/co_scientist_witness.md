# The Witness Pattern: Empirical Evidence in Tournaments

The **Witness Pattern** is a critical refinement to the **Co-Scientist Three-Brain Tournament** protocol. It addresses the risk of "Reflective Hallucination," where an LLM-based Proposer or Judge evaluates success based on internal reasoning rather than external reality.

## 1. The Core Problem: The Self-Reporting Bias

In a standard tournament:

1. **Proposer** (Agent) implements a solution.
2. **Judge** (Verifier) reads the Proposer's output and issues a score.

**The Failure Mode**: If the Proposer *claims* to have passed a test in its STDOUT, the Judge may accept this claim at face value without verifying the underlying execution. This allows "faking" success via hallucinated logs.

## 2. The Solution: The "Witness" (Independent Test Driver)

To invalidate self-reported success, the protocol mandates a **Test Driver** (The Witness):

1. **Step 1 (Proposer)**: Implements the logic AND a discrete, independent test script (e.g., `refrag_test_driver.py`).
2. **Step 2 (Execution)**: The Test Driver executes the logic in a sandboxed environment.
3. **Step 3 (Artifact Generation)**: The Test Driver MUST output a machine-readable JSON file (e.g., `verdict.json`) containing raw scores.
4. **Step 4 (Judging)**: The **Tournament Judge** consumes the `verdict.json` file. It does NOT read the Proposer's logs or STDOUT for scoring.

## 3. Implementation Example: The ReFRAG Case

When validating the ReFRAG protocol (Jan 2026), the Witness pattern was used to achieve "Certified Success":

* **Logic**: `tools/refrag.py`
* **Witness**: `tools/refrag_test_driver.py`
* **Evidence**: `tools/refrag_verdict.json`
* **Judge Command**: `python tools/tournament_judge.py --goal "..." --scores tools/refrag_verdict.json`

## 4. Technical Constraints (The "STDOUT Pollution" Guard)

A common hurdle is **STDOUT Pollution**, where debug statements (e.g., "Pass/Fail" prints) mixed with JSON output cause the Judge to crash.

**Best Practice**:
* The Test Driver should write the JSON verdict to a **file** explicitly.
* Use `sys.stderr` for human-readable logging to keep the evidence channel clean.

## 5. Metadata

* **Protocol**: Co-Scientist v2.1
* **Status**: Mandated for all K3 technical foundations.
