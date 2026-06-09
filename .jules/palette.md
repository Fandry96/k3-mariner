## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2024-05-23 - Mapping Technical IDs to User-Friendly Display Names
**Learning:** Users can be confused by technical IDs in selectboxes (e.g., "gemini/gemini-flash-latest"). Using the `format_func` parameter in Streamlit's `selectbox` widget maps technical identifiers to user-friendly display names without altering the underlying return values.
**Action:** Always use a mapping dictionary and `format_func` in `selectbox` for technical IDs to ensure clarity for users while maintaining backend functionality.
## 2024-05-24 - Disable form submit button on missing API Key
**Learning:** Streamlit forms can natively disable their submit buttons and provide tooltips via the `disabled` and `help` parameters, which is much better UX than letting the user submit and then showing an error message.
**Action:** Always use `disabled` and `help` parameters on `st.form_submit_button` to prevent invalid form submissions and explain why the button is disabled.
