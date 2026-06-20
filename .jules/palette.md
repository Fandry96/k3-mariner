## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2024-05-23 - Mapping Technical IDs to User-Friendly Display Names
**Learning:** Users can be confused by technical IDs in selectboxes (e.g., "gemini/gemini-flash-latest"). Using the `format_func` parameter in Streamlit's `selectbox` widget maps technical identifiers to user-friendly display names without altering the underlying return values.
**Action:** Always use a mapping dictionary and `format_func` in `selectbox` for technical IDs to ensure clarity for users while maintaining backend functionality.
## 2026-06-20 - [Add tooltip and disabled state to submit button]
**Learning:** Disabling Streamlit submit buttons based on inputs *outside* the form prevents confusing error states and provides better immediate feedback. Using the `help` param adds contextual tooltips explaining the disabled state effectively.
**Action:** Always check if form dependencies are located outside the form block; if so, use them to reactively disable `st.form_submit_button` and provide a tooltip rather than relying entirely on post-submit backend validation errors.
