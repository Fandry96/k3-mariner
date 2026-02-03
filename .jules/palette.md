## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2025-02-18 - Keyboard Accessibility in Search
**Learning:** In Streamlit, standard text inputs require a mouse click to submit unless wrapped in a form. This breaks the expected "Type -> Enter" flow for search interfaces.
**Action:** Always wrap primary search/input-action pairs in `st.form(..., border=False)` to enable "Enter to Submit" without altering the visual design.
