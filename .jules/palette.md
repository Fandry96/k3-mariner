## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2024-05-23 - Mapping Technical IDs to User-Friendly Display Names
**Learning:** Users can be confused by technical IDs in selectboxes (e.g., "gemini/gemini-flash-latest"). Using the `format_func` parameter in Streamlit's `selectbox` widget maps technical identifiers to user-friendly display names without altering the underlying return values.
**Action:** Always use a mapping dictionary and `format_func` in `selectbox` for technical IDs to ensure clarity for users while maintaining backend functionality.

## 2024-10-24 - Dynamic Disabled States in Streamlit Forms
**Learning:** Streamlit form submit buttons cannot be dynamically disabled based on inputs *inside* the same form, because widgets inside an `st.form` do not trigger a rerun until submission.
**Action:** Only apply dynamic `disabled` states to form submit buttons based on the state of required inputs located *outside* the form.
