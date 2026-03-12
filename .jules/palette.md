## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link, and a persistent caption ensures visibility even before interaction.
**Action:** Always include a `help` parameter with a Markdown URL for any external service credential input. Include a persistent `st.caption` below the input if the value is missing.

## 2024-05-23 - Selectbox Model Names
**Learning:** Displaying technical IDs (like "gemini/gemini-flash-latest") in selectboxes degrades UX by exposing implementation details. The `format_func` parameter in `st.selectbox` efficiently maps these internal values to user-friendly labels without breaking backend expectations.
**Action:** Use `format_func` to display user-friendly names for model selection or similar technical identifiers.
