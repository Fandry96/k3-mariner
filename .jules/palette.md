## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2025-02-12 - Enter-to-Submit via Forms
**Learning:** Streamlit's `st.text_input` does not trigger submission on Enter by default, frustrating users who expect search-like behavior.
**Action:** Wrap search inputs in `st.form` with `border=False` to enable Enter-key submission without visual disruption.
