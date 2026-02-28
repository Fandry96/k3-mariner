## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2025-02-28 - Explicit Setup Links
**Learning:** While tooltips are good for minor hints, critical setup links (like generating an API key) get missed when placed inside a hover tooltip.
**Action:** Always provide a persistent inline link (e.g., via `st.caption`) for external dependencies to reduce onboarding friction.
