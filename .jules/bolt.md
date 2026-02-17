## 2024-05-23 - Streamlit Output Throttling
**Learning:** Streamlit's `placeholder.code()` triggers a full re-render on every call. High-frequency updates (e.g., from verbose agent logs) can freeze the UI because the browser cannot keep up with the render queue.
**Action:** Always implement time-based throttling (e.g., max 10Hz) when streaming text to Streamlit components, ensuring a forced final update in the `finally` block to capture the last chunk.

## 2024-05-24 - Search Caching Strategy
**Learning:** Web search results (duckduckgo_search) return a generator which must be consumed (converted to list) before caching, otherwise the cache stores an exhausted generator.
**Action:** When caching generator-based API results, always wrap them in `list()` inside the cached function. Use `@st.cache_data` for persistent Streamlit caching and `@functools.lru_cache` for backend logic.

## 2024-05-25 - Incremental ANSI Cleaning
**Learning:** Cleaning ANSI codes from a growing log buffer using `re.sub` on the *entire* buffer every update creates an O(N^2) bottleneck, freezing the UI for large logs (e.g., 2.8s for 1000 lines). Incremental cleaning (O(N)) reduces this to ~9ms.
**Action:** When streaming text with potential ANSI codes, clean chunks incrementally before appending to the buffer, using a small pending buffer to handle split escape sequences.
