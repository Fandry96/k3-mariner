## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2024-10-26 - Persistent Help Links
**Learning:** Tooltips are great for context, but hidden by default. For critical blockers (like API keys), a persistent `st.caption` with a direct link reduces abandonment more effectively than a tooltip alone.
**Action:** Use both `help` (for detail) and `st.caption` (for action) on critical setup inputs.
