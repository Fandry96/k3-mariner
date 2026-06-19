## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2024-05-23 - Mapping Technical IDs to User-Friendly Display Names
**Learning:** Users can be confused by technical IDs in selectboxes (e.g., "gemini/gemini-flash-latest"). Using the `format_func` parameter in Streamlit's `selectbox` widget maps technical identifiers to user-friendly display names without altering the underlying return values.
**Action:** Always use a mapping dictionary and `format_func` in `selectbox` for technical IDs to ensure clarity for users while maintaining backend functionality.
## 2024-06-19 - Streamlit Form Button Disablement Constraint
**Learning:** Streamlit forms (`st.form`) do not trigger a script rerun until submitted, which means dynamically disabling `st.form_submit_button` based on inputs *inside* the form will permanently lock the button. However, it can be safely disabled based on inputs *outside* the form.
**Action:** Always validate form inputs internally but safely disable form submit buttons using state from inputs located outside the form (like sidebar settings).
