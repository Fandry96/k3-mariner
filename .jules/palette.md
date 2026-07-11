## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2024-05-23 - Mapping Technical IDs to User-Friendly Display Names
**Learning:** Users can be confused by technical IDs in selectboxes (e.g., "gemini/gemini-flash-latest"). Using the `format_func` parameter in Streamlit's `selectbox` widget maps technical identifiers to user-friendly display names without altering the underlying return values.
**Action:** Always use a mapping dictionary and `format_func` in `selectbox` for technical IDs to ensure clarity for users while maintaining backend functionality.
## 2024-07-11 - Disabling form submit button with missing global state
**Learning:** Preventing invalid form submissions early by dynamically disabling the submit button improves user experience. Since inputs within a Streamlit form don't trigger reruns until submission, you can safely disable the submit button based on inputs *outside* the form (like API key in the sidebar). Using the `disabled` and `help` parameters simultaneously explains *why* the button is disabled.
**Action:** Always dynamically disable form submit buttons based on missing external required state and pair it with a helpful tooltip.
