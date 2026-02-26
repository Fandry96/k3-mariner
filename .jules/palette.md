## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2024-05-25 - Visible Links for Critical Actions
**Learning:** Tooltips are great for context, but critical onboarding actions (like getting an API key) benefit from a persistent, visible link (`st.caption`) to reduce friction.
**Action:** Use `st.caption` with a direct link for mandatory setup steps, in addition to or instead of tooltips.
