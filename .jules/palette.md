## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.
## 2024-05-23 - Model Selectbox Display Names\n**Learning:** Streamlit selectboxes can display user-friendly names while returning technical IDs using `format_func`.\n**Action:** Use `format_func` in `st.selectbox` for mapping model IDs to readable names.
