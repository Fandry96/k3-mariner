## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2026-03-04 - Enhanced API Key Onboarding
**Learning:** Relying solely on tooltips for critical setup inputs like API keys can lead to abandonment since the tooltip must be hovered over to be seen. A persistent caption alongside the tooltip increases visibility and click-through.
**Action:** Use both a `help` tooltip with a Markdown link and a persistent `st.caption` with a direct link for critical setup inputs.
