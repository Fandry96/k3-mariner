## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2025-05-27 - Streamlit Input Labels & Formatting
**Learning:** Technical identifiers (like model IDs) in dropdowns confuse users. Using `format_func` in `st.selectbox` allows presenting friendly names while keeping backend logic clean. Also, persistent captions with links below critical inputs (like API keys) reduce abandonment better than tooltips alone.
**Action:** Use `format_func` for technical enums and add `st.caption` with direct links below critical setup inputs.
