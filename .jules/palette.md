## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2024-05-23 - Mapping Technical IDs to User-Friendly Display Names
**Learning:** Users can be confused by technical IDs in selectboxes (e.g., "gemini/gemini-flash-latest"). Using the `format_func` parameter in Streamlit's `selectbox` widget maps technical identifiers to user-friendly display names without altering the underlying return values.
**Action:** Always use a mapping dictionary and `format_func` in `selectbox` for technical IDs to ensure clarity for users while maintaining backend functionality.
## 2026-07-22 - Dynamic Form Submission Control
**Learning:** In Streamlit, elements inside an `st.form` do not trigger a rerun until submitted. However, because the `api_key` input is located outside the form, changes to it trigger a rerun, allowing us to dynamically disable the form's submit button based on its state.
**Action:** When preventing invalid form submissions, use `disabled` and `help` on `st.form_submit_button` based on the state of inputs outside the form. Omit layout-specific terms from help text. Leave original backend validation as a safeguard.
