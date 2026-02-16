## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2024-05-24 - Enter to Submit Pattern
**Learning:** Streamlit inputs don't submit on Enter by default, causing friction. Wrapping single inputs in `st.form(border=False)` enables this native behavior without visual clutter.
**Action:** Always wrap primary search/input fields in a borderless form.
