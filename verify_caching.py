import time
import pickle

dicts = [{"title": f"Title {i}", "href": f"http://example.com/link{i}", "body": f"This is the snippet body for result {i} "*10} for i in range(5)]
string_val = "\n".join([f"- [Title]: {r.get('title', 'N/A')}\n  [Link]: {r.get('href', 'N/A')}\n  [Snippet]: {r.get('body', 'N/A')}" for r in dicts])

print(f"List of dicts pickle size: {len(pickle.dumps(dicts))} bytes")
print(f"String pickle size: {len(pickle.dumps(string_val))} bytes")

t0 = time.time()
for _ in range(100000):
    pickle.dumps(dicts)
print(f"Dict dump time: {time.time() - t0:.4f}s")

t0 = time.time()
for _ in range(100000):
    pickle.dumps(string_val)
print(f"String dump time: {time.time() - t0:.4f}s")
