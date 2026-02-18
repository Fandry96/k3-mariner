## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2024-05-24 - Search Form Submission
**Learning:** Streamlit's `st.text_input` doesn't support "Enter to submit" by default unless wrapped in a `st.form`. This is a critical pattern for search-heavy interfaces.
**Action:** Always wrap primary search/input fields in `st.form(border=False)` to enable keyboard submission.
