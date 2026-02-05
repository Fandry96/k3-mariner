import sys
import time
import re
from io import StringIO
from contextlib import contextmanager

# Mock placeholder
class MockPlaceholder:
    def __init__(self):
        self.update_count = 0
        self.last_text = ""

    def code(self, text, language="text"):
        self.update_count += 1
        self.last_text = text

# Helper to clean ansi (copied from app.py)
def clean_ansi(text):
    ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")
    return ansi_escape.sub("", text)

# Unoptimized version (from app.py)
@contextmanager
def capture_stdout_unoptimized(placeholder):
    new_out = StringIO()
    old_out = sys.stdout

    def update():
        clean_text = clean_ansi(new_out.getvalue())
        placeholder.code(clean_text, language="text")

    class RealTimeStream:
        def write(self, s):
            new_out.write(s)
            if "\n" in s:
                update()

        def flush(self):
            old_out.flush()

    sys.stdout = RealTimeStream()
    try:
        yield
    finally:
        sys.stdout = old_out
        update()

# Optimized version
@contextmanager
def capture_stdout_optimized(placeholder):
    new_out = StringIO()
    old_out = sys.stdout

    # State for throttling
    last_update = 0.0
    THROTTLE_INTERVAL = 0.1  # 100ms

    def update():
        clean_text = clean_ansi(new_out.getvalue())
        placeholder.code(clean_text, language="text")

    class RealTimeStream:
        def write(self, s):
            nonlocal last_update
            new_out.write(s)

            current_time = time.time()
            # Update if newline AND sufficient time passed
            if "\n" in s and (current_time - last_update >= THROTTLE_INTERVAL):
                update()
                last_update = current_time

        def flush(self):
            old_out.flush()

    sys.stdout = RealTimeStream()
    try:
        yield
    finally:
        sys.stdout = old_out
        update()

def test_performance():
    print("Testing Unoptimized Performance...")
    p1 = MockPlaceholder()
    start_time = time.time()
    with capture_stdout_unoptimized(p1):
        for i in range(100):
            print(f"Log line {i}")
            # No sleep, simulating burst
    end_time = time.time()
    print(f"Unoptimized: {p1.update_count} updates in {end_time - start_time:.4f}s")

    # Expect 100 updates (one per line) + 1 final flush = 101 or similar
    assert p1.update_count >= 100, f"Expected >= 100 updates, got {p1.update_count}"


    print("\nTesting Optimized Performance...")
    p2 = MockPlaceholder()
    start_time = time.time()
    with capture_stdout_optimized(p2):
        for i in range(100):
            print(f"Log line {i}")
            # No sleep, simulating burst
    end_time = time.time()
    print(f"Optimized: {p2.update_count} updates in {end_time - start_time:.4f}s")

    # Expect significantly fewer updates.
    # Since it's a tight loop, it might only update 1 (first) + 1 (final) = 2, or a few more if it takes > 0.1s
    assert p2.update_count < 50, f"Expected < 50 updates, got {p2.update_count}"

    print("\nSUCCESS: Optimization verified.")

if __name__ == "__main__":
    test_performance()
