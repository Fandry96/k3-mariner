## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2024-05-23 - Mapping Technical IDs to User-Friendly Display Names
**Learning:** Users can be confused by technical IDs in selectboxes (e.g., "gemini/gemini-flash-latest"). Using the `format_func` parameter in Streamlit's `selectbox` widget maps technical identifiers to user-friendly display names without altering the underlying return values.
**Action:** Always use a mapping dictionary and `format_func` in `selectbox` for technical IDs to ensure clarity for users while maintaining backend functionality.

## 2024-05-24 - Prevent Invalid Form Submissions
**Learning:** Showing an error message after a user clicks submit on a form with missing required fields (like API keys) is a frustrating experience. Disabling the submit button and providing a helpful tooltip is a much better pattern.
**Action:** Use `disabled` and `help` parameters on `st.form_submit_button` to prevent invalid states proactively.
