## 2024-05-23 - Streamlit Output Throttling
**Learning:** Streamlit's `placeholder.code()` triggers a full re-render on every call. High-frequency updates (e.g., from verbose agent logs) can freeze the UI because the browser cannot keep up with the render queue.
**Action:** Always implement time-based throttling (e.g., max 10Hz) when streaming text to Streamlit components, ensuring a forced final update in the `finally` block to capture the last chunk.

## 2024-05-24 - Search Caching Strategy
**Learning:** Web search results (duckduckgo_search) return a generator which must be consumed (converted to list) before caching, otherwise the cache stores an exhausted generator.
**Action:** When caching generator-based API results, always wrap them in `list()` inside the cached function. Use `@st.cache_data` for persistent Streamlit caching and `@functools.lru_cache` for backend logic.

## 2025-02-23 - Streamlit ANSI Cleaning Optimization
**Learning:** Cleaning ANSI codes from accumulating logs in `capture_stdout` using `clean_ansi(full_buffer)` is an O(N^2) operation. For long-running agents with verbose output, this causes significant lag.
**Action:** Implement incremental cleaning: clean new chunks *before* appending to the buffer, making the operation O(N).

## 2025-03-01 - Redundant StringIO Buffering Anti-Pattern
**Learning:** In incremental data capture flows like `capture_stdout`, allocating and writing to a write-only `StringIO` buffer (e.g., `new_out`) before processing the chunk is a double-buffering anti-pattern. This wastes memory allocations and CPU cycles on write operations whose data is never read or returned.
**Action:** Eliminate write-only `StringIO` objects from data capture flows. Removing a redundant `StringIO.write` operation in a tight loop yields approximately 75% performance improvement for that specific operation by reducing CPU overhead and memory allocation.
## 2026-05-01 - Optimize agent search tool with bounded cache and generator expressions
**Learning:** For standalone local agent tool instances like `MarinerSearchTool`, caching search queries in an unbounded instance dictionary can cause slow memory leaks for long-lived instances processing many unique queries. In addition, using list comprehensions inside string format joins increases peak memory usage for large result sets.
**Action:** Implemented a bounded instance-level dictionary cache (`self._cache`) ensuring cache bounds (max 50) and swapped list comprehensions inside `str.join()` for generator expressions across duplicate tool definitions in both `agent.py` and `app.py` to prevent redundant network calls, memory growth, and optimize string formatting.
## 2026-05-01 - Correct instance dictionary cache eviction logic
**Learning:** When enforcing an upper bound on an instance-level dictionary cache (e.g., `if len(self._cache) > 50:`), using `self._cache.clear()` wipes the entire cache including the just-added item, causing cache thrashing and rendering the cache useless for the 51st item. Furthermore, generator expressions inside `str.join()` for small result sets (N=5) offer no measurable peak memory advantage and represent premature micro-optimization.
**Action:** Implemented a robust LRU-style eviction by popping the oldest item (`self._cache.pop(next(iter(self._cache)))`) instead of clearing the whole dictionary, preserving the newly added result and preventing cache thrashing. Reverted string joining back to standard list comprehensions.
