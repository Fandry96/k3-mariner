## 2024-05-23 - Streamlit Output Throttling
**Learning:** Streamlit's `placeholder.code()` triggers a full re-render on every call. High-frequency updates (e.g., from verbose agent logs) can freeze the UI because the browser cannot keep up with the render queue.
**Action:** Always implement time-based throttling (e.g., max 10Hz) when streaming text to Streamlit components, ensuring a forced final update in the `finally` block to capture the last chunk.

## 2024-05-24 - Regex Compilation Overhead
**Learning:** Even with Python's internal regex caching, compiling regex patterns inside a frequently called function (tight loop) can introduce significant overhead (~30% slowdown on short strings) due to cache lookup and function call costs.
**Action:** Always move `re.compile` to the module/global scope for patterns used in high-frequency loops or stream processing functions.
