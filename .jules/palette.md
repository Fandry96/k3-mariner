## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2024-05-23 - Mapping Technical IDs to User-Friendly Display Names
**Learning:** Users can be confused by technical IDs in selectboxes (e.g., "gemini/gemini-flash-latest"). Using the `format_func` parameter in Streamlit's `selectbox` widget maps technical identifiers to user-friendly display names without altering the underlying return values.
**Action:** Always use a mapping dictionary and `format_func` in `selectbox` for technical IDs to ensure clarity for users while maintaining backend functionality.
## 2026-09-01 - Dynamic disabled state for form submit button
**Learning:** Users can click the submit button on forms only to see an error that an API key is required. Disabling the button dynamically and providing a tooltip explaining why prevents this frustrating interaction.
**Action:** Use `disabled` and `help` on form submit buttons to lock them and explain why when external state (like a required API key) is missing.
