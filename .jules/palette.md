## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2024-05-23 - Mapping Technical IDs to User-Friendly Display Names
**Learning:** Users can be confused by technical IDs in selectboxes (e.g., "gemini/gemini-flash-latest"). Using the `format_func` parameter in Streamlit's `selectbox` widget maps technical identifiers to user-friendly display names without altering the underlying return values.
**Action:** Always use a mapping dictionary and `format_func` in `selectbox` for technical IDs to ensure clarity for users while maintaining backend functionality.
## 2024-07-26 - Dynamically Disabling Form Buttons
**Learning:** In Streamlit, elements inside an `st.form` do not trigger a rerun until submission. To reliably disable an `st.form_submit_button` based on a required input, that input must be located *outside* the form. Disabling the button based on an input *inside* the form will permanently lock it.
**Action:** Always ensure that any state driving a disabled `st.form_submit_button` originates from inputs outside the `st.form` context, and use `help` to explain why the button is disabled.
