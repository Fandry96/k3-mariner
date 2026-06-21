## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2024-05-23 - Mapping Technical IDs to User-Friendly Display Names
**Learning:** Users can be confused by technical IDs in selectboxes (e.g., "gemini/gemini-flash-latest"). Using the `format_func` parameter in Streamlit's `selectbox` widget maps technical identifiers to user-friendly display names without altering the underlying return values.
**Action:** Always use a mapping dictionary and `format_func` in `selectbox` for technical IDs to ensure clarity for users while maintaining backend functionality.
## 2025-06-21 - Disabled Submit Button with Tooltip
**Learning:** In Streamlit, disabling a form submit button dynamically must only depend on state outside the form (like the sidebar) to avoid permanently locking the form. Providing a tooltip on the disabled button significantly improves user understanding of the missing prerequisite.
**Action:** Always check if a prerequisite (like an API key) is outside the form and use it to disable the form submit button with an explanatory `help` parameter, instead of relying solely on post-submission errors.
