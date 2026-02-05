## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2026-02-05 - Enter to Submit in Streamlit
**Learning:** Streamlit users expect "Enter" to trigger form submission, but default `text_input` + `button` requires a click. Using `st.form(border=False)` enables this native behavior without visual clutter.
**Action:** Wrap search/input groups in borderless forms to enable keyboard submission.
