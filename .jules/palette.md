## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2024-05-23 - Mapping Technical IDs to User-Friendly Display Names
**Learning:** Users can be confused by technical IDs in selectboxes (e.g., "gemini/gemini-flash-latest"). Using the `format_func` parameter in Streamlit's `selectbox` widget maps technical identifiers to user-friendly display names without altering the underlying return values.
**Action:** Always use a mapping dictionary and `format_func` in `selectbox` for technical IDs to ensure clarity for users while maintaining backend functionality.
## 2025-03-05 - Dynamic Form Submission Prevention
**Learning:** Users can click the submit button on forms with missing required external inputs (like API keys), leading to error messages. Disabling the submit button dynamically prevents this.
**Action:** Use the `disabled` and `help` parameters on `st.form_submit_button` to dynamically disable the button based on required inputs outside the form, providing an explanatory tooltip.
