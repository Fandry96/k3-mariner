## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2024-05-24 - Streamlit Form Interaction
**Learning:** Users expect "Enter" to submit text inputs, but Streamlit requires wrapping inputs in `st.form` to enable this without explicit button clicks. Using `border=False` preserves the original visual layout.
**Action:** Wrap primary search/input fields and their submit buttons in `st.form(key="...", border=False)` to support keyboard-first workflows.

(Note: PR #3941519556 was closed as a duplicate.)
