## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2026-02-07 - Enter to Submit
**Learning:** Streamlit inputs don't submit on Enter by default, which frustrates users expecting standard web form behavior.
**Action:** Always wrap primary action inputs in a `st.form` with `border=False` to enable Enter-to-submit without visual changes.
