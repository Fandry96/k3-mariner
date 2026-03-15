## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2024-05-28 - Model Names Readability & Persistent Links
**Learning:** Raw technical IDs for models (like `gemini/gemini-flash-latest`) are confusing for non-technical users. Additionally, relying solely on tooltips for credential links leads to abandonment because users might not hover over the input.
**Action:** Use `format_func` in `st.selectbox` to map technical IDs to user-friendly display names without altering the underlying return values. For critical setup inputs (e.g., API keys), use both a `help` tooltip with a Markdown link and a persistent `st.caption` with a direct link to reduce abandonment.