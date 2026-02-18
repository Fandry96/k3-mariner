## 2024-05-23 - Streamlit Output Throttling
**Learning:** Streamlit's `placeholder.code()` triggers a full re-render on every call. High-frequency updates (e.g., from verbose agent logs) can freeze the UI because the browser cannot keep up with the render queue.
**Action:** Always implement time-based throttling (e.g., max 10Hz) when streaming text to Streamlit components, ensuring a forced final update in the `finally` block to capture the last chunk.

## 2024-05-24 - Search Caching Strategy
**Learning:** Web search results (duckduckgo_search) return a generator which must be consumed (converted to list) before caching, otherwise the cache stores an exhausted generator.
**Action:** When caching generator-based API results, always wrap them in `list()` inside the cached function. Use `@st.cache_data` for persistent Streamlit caching and `@functools.lru_cache` for backend logic.

## 2024-05-25 - Incremental ANSI Cleaning
**Learning:** Cleaning ANSI codes from the entire log buffer on every update ($O(N^2)$) freezes the UI for long-running agents.
**Action:** Implement incremental cleaning: clean only the new chunk ($O(M)$), append to a list, and join ($O(N)$) for display. This reduces processing time by ~50x-400x for large logs.
