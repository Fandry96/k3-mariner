## 2024-05-23 - Streamlit Output Throttling
**Learning:** Streamlit's `placeholder.code()` triggers a full re-render on every call. High-frequency updates (e.g., from verbose agent logs) can freeze the UI because the browser cannot keep up with the render queue.
**Action:** Always implement time-based throttling (e.g., max 10Hz) when streaming text to Streamlit components, ensuring a forced final update in the `finally` block to capture the last chunk.

## 2024-05-24 - Search Caching Strategy
**Learning:** Web search results (duckduckgo_search) return a generator which must be consumed (converted to list) before caching, otherwise the cache stores an exhausted generator.
**Action:** When caching generator-based API results, always wrap them in `list()` inside the cached function. Use `@st.cache_data` for persistent Streamlit caching and `@functools.lru_cache` for backend logic.

## 2024-05-25 - Incremental ANSI Cleaning
**Learning:** Re-cleaning the entire log buffer with regex (`clean_ansi(full_text)`) on every UI update is an O(N^2) operation that dominates CPU usage for long-running processes. Incremental cleaning (O(N)) combined with split-ANSI detection is ~100x faster.
**Action:** When streaming text with ANSI codes, maintain a buffer of cleaned chunks and a `pending_ansi` string. Use `split_incomplete_ansi` to handle escape sequences split across chunk boundaries. Avoid `StringIO.getvalue()` if possible to eliminate O(N) copies.
