## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2026-03-03 - Technical IDs vs Display Names in Selectboxes
**Learning:** Exposing technical identifiers (e.g., 'gemini/gemini-flash-latest') in UI select menus can confuse users and look unpolished. Streamlit's `format_func` parameter enables mapping these IDs to user-friendly labels (like 'Gemini Flash (Fast)') while retaining the underlying technical value for backend operations.
**Action:** Use `format_func` in `st.selectbox` (or similar selection widgets) whenever presenting technical model IDs, system strings, or raw identifiers to end users.
