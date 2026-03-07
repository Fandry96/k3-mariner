## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2024-05-24 - Technical Jargon in UI & Persistent Onboarding
**Learning:** Exposing technical model IDs (e.g., `gemini/gemini-flash-latest`) is confusing to non-technical users. Additionally, users often miss tooltips (like the `help` icon), making critical onboarding links (like API keys) hard to find, leading to abandonment.
**Action:** Use `format_func` in Streamlit selectboxes to map technical IDs to user-friendly names without changing the underlying value. Use persistent UI elements (like `st.caption` with Markdown links) near critical empty inputs to ensure visibility, rather than relying solely on tooltips.
