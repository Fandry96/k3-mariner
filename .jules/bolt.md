## 2024-05-23 - Streamlit Placeholder Performance
**Learning:** `placeholder.code()` in Streamlit triggers a full frontend re-render of the component. Calling it on every newline from a fast-producing stream (like an LLM thinking process) causes massive UI lag and CPU usage.
**Action:** Always throttle real-time stream updates to the UI (e.g., max 10Hz) to balance responsiveness with performance.
