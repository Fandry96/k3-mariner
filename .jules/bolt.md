## 2024-05-23 - Streamlit Output Throttling
**Learning:** Streamlit's `placeholder.code()` triggers a full re-render on every call. High-frequency updates (e.g., from verbose agent logs) can freeze the UI because the browser cannot keep up with the render queue.
**Action:** Always implement time-based throttling (e.g., max 10Hz) when streaming text to Streamlit components, ensuring a forced final update in the `finally` block to capture the last chunk.

## 2025-05-23 - DuckDuckGo Search Connection Reuse
**Learning:** Reusing the `duckduckgo_search.DDGS` instance (connection pooling) was consistently SLOWER (~0.85s vs ~0.18s) than creating a new instance for every request.
**Action:** Do NOT attempt to reuse `DDGS` instances for performance. Stick to the context manager pattern `with DDGS() as ddgs:`.
