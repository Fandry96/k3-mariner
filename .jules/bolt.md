## 2024-05-23 - Streamlit Output Throttling
**Learning:** Streamlit's `placeholder.code()` triggers a full re-render on every call. High-frequency updates (e.g., from verbose agent logs) can freeze the UI because the browser cannot keep up with the render queue.
**Action:** Always implement time-based throttling (e.g., max 10Hz) when streaming text to Streamlit components, ensuring a forced final update in the `finally` block to capture the last chunk.

## 2024-05-24 - Search Caching Strategy
**Learning:** Web search results (duckduckgo_search) return a generator which must be consumed (converted to list) before caching, otherwise the cache stores an exhausted generator.
**Action:** When caching generator-based API results, always wrap them in `list()` inside the cached function. Use `@st.cache_data` for persistent Streamlit caching and `@functools.lru_cache` for backend logic.

## 2025-02-23 - Streamlit ANSI Cleaning Optimization
**Learning:** Cleaning ANSI codes from accumulating logs in `capture_stdout` using `clean_ansi(full_buffer)` is an O(N^2) operation. For long-running agents with verbose output, this causes significant lag.
**Action:** Implement incremental cleaning: clean new chunks *before* appending to the buffer, making the operation O(N).

## 2025-02-23 - Environment Loading Optimization
**Learning:** `load_dotenv` performs blocking disk I/O on every Streamlit rerun (~30ms), which adds up in interactive sessions. Caching it with `@st.cache_resource` eliminates this overhead but prevents hot-reloading of `.env` changes.
**Action:** Wrap `load_dotenv` in a `@st.cache_resource` function for production apps where config is static.

## 2025-02-23 - Warning Suppression Resilience
**Learning:** Libraries like `duckduckgo_search` may change their warning messages (e.g., from "duckduckgo_search" to "renamed to `ddgs`"). Hardcoded string filters can be brittle.
**Action:** Use broad yet specific filters in `logging.Filter` to catch variations (e.g., checking for both package name and specific deprecation messages) to ensure clean logs across library updates.
