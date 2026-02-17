## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2025-05-24 - Search Input Submission
**Learning:** Streamlit users expect "Enter" to submit search queries. Wrapping `st.text_input` and `st.form_submit_button` in `st.form(border=False)` enables this without visual changes.
**Action:** Use this pattern for all search-like inputs in Streamlit apps.
