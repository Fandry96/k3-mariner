## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2024-05-23 - Mapping Technical IDs to User-Friendly Display Names
**Learning:** Users can be confused by technical IDs in selectboxes (e.g., "gemini/gemini-flash-latest"). Using the `format_func` parameter in Streamlit's `selectbox` widget maps technical identifiers to user-friendly display names without altering the underlying return values.
**Action:** Always use a mapping dictionary and `format_func` in `selectbox` for technical IDs to ensure clarity for users while maintaining backend functionality.

## 2024-06-14 - Prevent Invalid Form Submissions
**Learning:** Users can be frustrated by clicking a submit button only to receive a validation error after the fact, especially in forms with prerequisite credentials.
**Action:** Dynamically disable form submit buttons using the `disabled` parameter and provide an explanatory `help` tooltip when required fields (like API keys) are missing to proactively guide users.
