## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2024-05-23 - Mapping Technical IDs to User-Friendly Display Names
**Learning:** Users can be confused by technical IDs in selectboxes (e.g., "gemini/gemini-flash-latest"). Using the `format_func` parameter in Streamlit's `selectbox` widget maps technical identifiers to user-friendly display names without altering the underlying return values.
**Action:** Always use a mapping dictionary and `format_func` in `selectbox` for technical IDs to ensure clarity for users while maintaining backend functionality.

## 2024-04-29 - [Streamlit Selectbox Technical IDs UX Pattern]
**Learning:** Displaying raw technical IDs (like `gemini/gemini-flash-latest`) in `selectbox` widgets degrades the user experience for non-technical users, but directly modifying the options array breaks backend logic.
**Action:** Always use a mapping dictionary combined with the `format_func` parameter to render user-friendly display names while preserving the underlying technical IDs.
