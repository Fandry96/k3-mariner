# Palette's UX Journal

## 2025-05-15 - Streamlit Keyboard Accessibility
**Learning:** Streamlit's `st.text_input` does not trigger actions on Enter by default. Users expect "Enter to Submit" for search bars.
**Action:** Always wrap single-input search/action fields in `st.form` with `border=False` to enable keyboard submission without altering the visual layout.
