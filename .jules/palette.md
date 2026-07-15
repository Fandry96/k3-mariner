## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2024-05-23 - Mapping Technical IDs to User-Friendly Display Names
**Learning:** Users can be confused by technical IDs in selectboxes (e.g., "gemini/gemini-flash-latest"). Using the `format_func` parameter in Streamlit's `selectbox` widget maps technical identifiers to user-friendly display names without altering the underlying return values.
**Action:** Always use a mapping dictionary and `format_func` in `selectbox` for technical IDs to ensure clarity for users while maintaining backend functionality.
## 2024-07-15 - Disabled States on Streamlit Form Buttons
**Learning:** Streamlit form widgets do not trigger reruns until submitted. Disabling a form submit button based on inputs *inside* the form permanently locks it. However, it is safe to dynamically disable a form submit button based on state changes from inputs located *outside* the form (e.g., in `st.sidebar`), as those changes trigger an immediate app rerun and properly re-evaluate the button's `disabled` state.
**Action:** Always verify the location of inputs (inside vs outside `st.form`) before using them to compute dynamic `disabled` states for `st.form_submit_button` to prevent locking users out.
