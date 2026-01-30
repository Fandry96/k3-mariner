## 2024-05-23 - Streamlit Output Throttling
**Learning:** Streamlit's `placeholder.code()` triggers a full re-render on every call. High-frequency updates (e.g., from verbose agent logs) can freeze the UI because the browser cannot keep up with the render queue.
**Action:** Always implement time-based throttling (e.g., max 10Hz) when streaming text to Streamlit components, ensuring a forced final update in the `finally` block to capture the last chunk.

## 2026-01-30 - DuckDuckGo Search Warning Suppression
**Learning:** `duckduckgo_search.DDGS` calls `warnings.simplefilter('always')` during instantiation, overriding standard `warnings.filterwarnings` or `warnings.catch_warnings`. This forces the "package renamed" RuntimeWarning to print to stderr on every search, causing IO overhead and log pollution.
**Action:** Use `logging.captureWarnings(True)` and attach a `logging.Filter` to the `py.warnings` logger to programmatically filter out specific warning messages based on content.
