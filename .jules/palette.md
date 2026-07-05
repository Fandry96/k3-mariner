## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2024-05-23 - Mapping Technical IDs to User-Friendly Display Names
**Learning:** Users can be confused by technical IDs in selectboxes (e.g., "gemini/gemini-flash-latest"). Using the `format_func` parameter in Streamlit's `selectbox` widget maps technical identifiers to user-friendly display names without altering the underlying return values.
**Action:** Always use a mapping dictionary and `format_func` in `selectbox` for technical IDs to ensure clarity for users while maintaining backend functionality.

## 2024-05-24 - Dynamic Form Submit Disabling
**Learning:** In Streamlit, disabling a form submit button based on inputs inside the form locks it permanently because internal widgets don't trigger reruns until submission. However, it is safe and highly effective UX to disable it dynamically based on required inputs located *outside* the form (like API keys in the sidebar).
**Action:** Use `disabled` and `help` parameters on `st.form_submit_button` to prevent invalid states when dependent variables are outside the form.
