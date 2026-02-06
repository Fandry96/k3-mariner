## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2024-05-23 - Enter to Submit
**Learning:** Users expect 'Enter' to submit search queries. Wrapping Streamlit inputs in `st.form(border=False)` enables this behavior without altering visual layout.
**Action:** Apply this pattern to all primary search/input interfaces.
