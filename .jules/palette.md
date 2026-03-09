## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2025-03-09 - Persistent Setup Links & Friendly Names
**Learning:** The `help` tooltip alone can sometimes be missed or ignored during critical onboarding (like entering an API key). Using a persistent `st.caption` with a direct Markdown link ensures the fallback URL is always visible. Additionally, displaying raw technical identifiers (like 'gemini/gemini-flash-latest') in drop-downs causes cognitive load, while mapping them to user-friendly names improves clarity.
**Action:** For critical setup inputs, use both a `help` tooltip and a persistent `st.caption` with a direct link. Use the `format_func` parameter in `st.selectbox` to map technical identifiers to user-friendly display names without altering the underlying return values.
