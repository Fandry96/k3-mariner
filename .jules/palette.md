## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2024-05-24 - Streamlit Form Submission
**Learning:** By default, Streamlit `text_input` widgets do not submit on "Enter". Users expect this behavior in search interfaces. Wrapping inputs and the submit button in `st.form(border=False)` enables this without altering the visual layout.
**Action:** Always wrap primary search/input groups in a borderless `st.form` to support "Enter" key submission.
