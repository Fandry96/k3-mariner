## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2024-05-24 - Streamlit Form Submission
**Learning:** Streamlit text inputs do not natively support "Enter to submit" without being wrapped in a form, causing user friction in search-heavy interfaces.
**Action:** Wrap search/input groups in `st.form(border=False)` and use `st.form_submit_button` to enable keyboard submission while maintaining visual layout.
