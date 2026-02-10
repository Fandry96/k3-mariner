## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2024-05-24 - Streamlit Form Submission
**Learning:** Streamlit's default `text_input` + `button` pattern breaks the "Enter to Submit" expectation. Users find it jarring to have to click "Execute" after typing.
**Action:** Wrap single-input-action pairs in `st.form(clear_on_submit=False, border=False)` to enable keyboard submission without altering the UI.
