## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2024-05-24 - Model Name Display
**Learning:** Exposing raw model IDs in UI dropdowns confuses non-technical users. Streamlit's `format_func` allows displaying user-friendly names while retaining technical IDs as the underlying value.
**Action:** Use `format_func` in `st.selectbox` for model selection to map technical IDs to descriptive names.
