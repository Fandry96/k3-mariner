## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2026-02-21 - Invisible Form for "Enter to Submit"
**Learning:** Streamlit users often expect pressing "Enter" in a single text input to submit the form, but by default, it only triggers a rerun without button context. Wrapping the input and button in `st.form(border=False)` (available since v1.33.0) enables this behavior seamlessly without altering the visual design.
**Action:** Always check for single-input "search-like" interfaces and wrap them in borderless forms to improve keyboard accessibility and user expectation.
