## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2025-02-23 - Persistent Help Links
**Learning:** Tooltips (via `help` parameter) are often missed by users scanning for setup instructions. For critical blockers like API keys, a persistent text link (e.g., via `st.caption`) significantly reduces abandonment risk compared to hidden tooltips.
**Action:** Use both: `help` for context, and a persistent `st.caption` link for the primary "Get Key" call-to-action when the field is empty.
