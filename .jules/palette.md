## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2024-05-23 - Mapping Technical IDs to User-Friendly Display Names
**Learning:** Users can be confused by technical IDs in selectboxes (e.g., "gemini/gemini-flash-latest"). Using the `format_func` parameter in Streamlit's `selectbox` widget maps technical identifiers to user-friendly display names without altering the underlying return values.
**Action:** Always use a mapping dictionary and `format_func` in `selectbox` for technical IDs to ensure clarity for users while maintaining backend functionality.

## 2024-07-30 - Form Submit Button Disabled State
**Learning:** In Streamlit, inputs inside `st.form` do not trigger reruns, making it impossible to dynamically disable the submit button based on them without permanently locking it. However, we can safely disable it based on required inputs located outside the form.
**Action:** Use `disabled` and `help` on `st.form_submit_button` for required fields outside the form to prevent invalid submissions, while retaining backend validation as a safeguard.
