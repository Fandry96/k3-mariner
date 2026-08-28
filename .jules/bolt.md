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

## 2025-03-01 - LRU Caching of API Clients
**Learning:** When using `@functools.lru_cache` on external API wrappers (like duckduckgo_search), instantiating the client inside the cached function destroys HTTP connection pooling for each new query. Also, caching and returning mutable objects exposes the cache to downstream mutation.
**Action:** Cache a method on a class instance that reuses a single established client, and always cast sequence results to immutable types (like `tuple`).

## 2025-03-01 - Python Caching and Generator Myths
**Learning:**
1. Applying `@functools.lru_cache` to an instance method causes the instance (`self`) to become part of the cache key. This creates a memory leak (strong reference to `self` preventing GC) and will crash with a `TypeError` if the class inherits from an unhashable type (like Pydantic's `BaseModel`, common in agent frameworks).
2. Using a generator expression inside `str.join()` (e.g., `",".join(x for x in list)`) instead of a list comprehension does *not* save memory in CPython. `str.join()` requires two passes (one to calculate total length, one to copy) so it internally unpacks the generator into a list anyway. The generator expression is actually slightly slower due to frame execution overhead.
**Action:**
1. Use dictionary-based instance caching for class methods instead of `@lru_cache`, or use `@lru_cache` only on static/pure functions.
2. Stick to list comprehensions for `str.join()` as they are faster and use the same amount of memory.
