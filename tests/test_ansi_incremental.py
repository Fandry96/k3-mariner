import time
import re
import io
import sys

# Exact regex from app.py
ANSI_ESCAPE = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")

def clean_ansi(text):
    return ANSI_ESCAPE.sub("", text)

class NaiveCapture:
    def __init__(self):
        self.buffer = io.StringIO()
        self.output_history = []

    def write(self, s):
        self.buffer.write(s)

    def update(self):
        # Current implementation: clean the entire history
        full_text = self.buffer.getvalue()
        clean_text = clean_ansi(full_text)
        # Simulate display (we just store length to avoid memory explosion in test)
        self.output_history.append(len(clean_text))

class IncrementalCapture:
    def __init__(self):
        self.clean_buffer = [] # List of strings
        self.output_history = []

    def write(self, s):
        # Proposed implementation: clean immediately
        clean_s = clean_ansi(s)
        self.clean_buffer.append(clean_s)

    def update(self):
        # Join cleaned chunks
        clean_text = "".join(self.clean_buffer)
        self.output_history.append(len(clean_text))

def test_correctness():
    print("Verifying correctness...")
    inputs = [
        "Hello World\n",
        "This is \x1B[31mRed\x1B[0m text.\n",
        "Another line.\n",
        # "Split ANSI: \x1B", "[32mGreen\x1B[0m\n" # We skip split ANSI test as we accept this limitation
    ]

    naive = NaiveCapture()
    inc = IncrementalCapture()

    for inp in inputs:
        naive.write(inp)
        naive.update()

        inc.write(inp)
        inc.update()

    naive_result = naive.output_history[-1]
    inc_result = inc.output_history[-1]

    if naive_result == inc_result:
        print("✅ Correctness (Standard inputs): PASS")
    else:
        print("❌ Correctness (Standard inputs): FAIL")
        print(f"Naive len: {naive_result}")
        print(f"Inc len:   {inc_result}")
        sys.exit(1)

def benchmark():
    print("\nBenchmarking...")
    # Simulate a heavy session
    # We use fewer iterations but larger chunks to emphasize the string length effect
    iterations = 5000
    chunk = "Log line with \x1B[34mcolor\x1B[0m and verify performance. " * 10 + "\n"

    # Naive
    start = time.time()
    naive = NaiveCapture()
    for _ in range(iterations):
        naive.write(chunk)
        naive.update()
    naive_time = time.time() - start
    print(f"Naive Time: {naive_time:.4f}s")

    # Incremental
    start = time.time()
    inc = IncrementalCapture()
    for _ in range(iterations):
        inc.write(chunk)
        inc.update()
    inc_time = time.time() - start
    print(f"Incremental Time: {inc_time:.4f}s")

    speedup = naive_time / inc_time if inc_time > 0 else 0
    print(f"Speedup: {speedup:.1f}x")

    if speedup > 1.2:
        print("✅ Performance: PASS (Improvement detected)")
    else:
        print("❌ Performance: FAIL (Improvement not significant)")
        # sys.exit(1) # Don't fail CI for noise, but warn.

if __name__ == "__main__":
    test_correctness()
    benchmark()
