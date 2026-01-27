## 2024-05-23 - Streamlit Output Throttling
**Learning:** Streamlit's `placeholder.code()` triggers a full re-render on every call. High-frequency updates (e.g., from verbose agent logs) can freeze the UI because the browser cannot keep up with the render queue.
**Action:** Always implement time-based throttling (e.g., max 10Hz) when streaming text to Streamlit components, ensuring a forced final update in the `finally` block to capture the last chunk.

## 2024-05-24 - Agent Search Efficiency
**Learning:** Providing search snippets (body) to the agent significantly reduces the number of steps required to find information, effectively optimizing the "algorithm" of the agent loop.
**Action:** Always ensure search tools return snippets, not just titles and links, to avoid "flying blind" loops.
