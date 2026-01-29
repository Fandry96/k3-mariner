## 2024-05-23 - Streamlit Output Throttling
**Learning:** Streamlit's `placeholder.code()` triggers a full re-render on every call. High-frequency updates (e.g., from verbose agent logs) can freeze the UI because the browser cannot keep up with the render queue.
**Action:** Always implement time-based throttling (e.g., max 10Hz) when streaming text to Streamlit components, ensuring a forced final update in the `finally` block to capture the last chunk.

## 2025-02-19 - DuckDuckGo Search Caching
**Learning:** `duckduckgo_search` operations are network-bound and take ~150-300ms per call. Reusing `DDGS` instances doesn't help performance, but the results are highly cacheable for repeated queries.
**Action:** Use `@st.cache_data` (Streamlit) or `@functools.lru_cache` (Python) to cache search results, converting the generator to a list to avoid exhaustion.
