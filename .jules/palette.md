## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2025-02-20 - Enter to Submit
**Learning:** `st.text_input` in Streamlit triggers a rerun on Enter but does not simulate a button click. Wrapping the input and button in `st.form(border=False)` aligns this behavior with user expectations (Enter = Submit) without altering the UI.
**Action:** Use `st.form` for primary search/action inputs to enable keyboard submission.
