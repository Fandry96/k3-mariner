## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2024-05-24 - Keyboard Submission
**Learning:** Streamlit's default `text_input` + `button` pattern breaks the "Enter to Submit" expectation. Wrapping them in `st.form` restores this native behavior.
**Action:** Use `st.form(border=False)` for primary search/chat inputs to enable keyboard submission without visual clutter.
