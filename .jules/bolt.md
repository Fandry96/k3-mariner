## 2024-05-23 - Streamlit Output Throttling
**Learning:** Streamlit's `placeholder.code()` triggers a full re-render on every call. High-frequency updates (e.g., from verbose agent logs) can freeze the UI because the browser cannot keep up with the render queue.
**Action:** Always implement time-based throttling (e.g., max 10Hz) when streaming text to Streamlit components, ensuring a forced final update in the `finally` block to capture the last chunk.

## 2024-05-24 - Search Caching Strategy
**Learning:** Web search results (duckduckgo_search) return a generator which must be consumed (converted to list) before caching, otherwise the cache stores an exhausted generator.
**Action:** When caching generator-based API results, always wrap them in `list()` inside the cached function. Use `@st.cache_data` for persistent Streamlit caching and `@functools.lru_cache` for backend logic.

## 2025-02-23 - Streamlit ANSI Cleaning Optimization
**Learning:** Cleaning ANSI codes from accumulating logs in `capture_stdout` using `clean_ansi(full_buffer)` is an O(N^2) operation. For long-running agents with verbose output, this causes significant lag.
**Action:** Implement incremental cleaning: clean new chunks *before* appending to the buffer, making the operation O(N).

## 2026-02-23 - Streamlit Environment Loading Optimization
**Learning:** Streamlit re-executes the entire script on every user interaction. Calling blocking I/O functions like `load_dotenv` at the module level causes redundant file reads (~1-2ms) on every click, which adds up.
**Action:** Wrap environment loading and other static initialization in `@st.cache_resource` functions to ensure they only run once per session/server lifetime.

## 2026-02-23 - DuckDuckGo Search Client Reuse
**Learning:** Creating a new `DDGS()` instance for every search incurs significant overhead (~0.7ms vs ~0.04ms) due to session/SSL setup. Reusing a single `DDGS` instance via `@st.cache_resource` enables connection pooling (Keep-Alive) and dramatically speeds up search execution.
**Action:** Cache the `DDGS` client using `@st.cache_resource` and reuse it across search calls instead of instantiating it inside the function.
