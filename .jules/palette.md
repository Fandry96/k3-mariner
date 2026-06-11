## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2024-05-23 - Mapping Technical IDs to User-Friendly Display Names
**Learning:** Users can be confused by technical IDs in selectboxes (e.g., "gemini/gemini-flash-latest"). Using the `format_func` parameter in Streamlit's `selectbox` widget maps technical identifiers to user-friendly display names without altering the underlying return values.
**Action:** Always use a mapping dictionary and `format_func` in `selectbox` for technical IDs to ensure clarity for users while maintaining backend functionality.

## 2025-03-02 - Disabling Submit Button for Missing API Keys
**Learning:** Users experience frustration when they fill out a form, click submit, and then get an error that a required field from elsewhere (like an API key in the sidebar) is missing.
**Action:** Use the `disabled` and `help` parameters on `st.form_submit_button` to prevent submission and provide immediate inline feedback when required inputs are missing, leaving backend validation as a fallback.
