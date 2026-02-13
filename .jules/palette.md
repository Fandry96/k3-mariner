## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2024-05-23 - Search Input Submission
**Learning:** Users expect search inputs to submit on "Enter". Wrapping `st.text_input` and `st.form_submit_button` in `st.form(border=False)` provides this behavior without the visual clutter of a default form border.
**Action:** Always wrap primary search/input fields in a borderless form for keyboard accessibility.
