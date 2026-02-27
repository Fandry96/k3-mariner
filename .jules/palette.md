## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2024-05-23 - Human-Readable Model Names
**Learning:** Exposing raw model IDs (e.g., `gemini/gemini-flash-latest`) confuses non-technical users. Using a dictionary map and `format_func` in selection widgets keeps the backend precise while making the frontend friendly.
**Action:** Always map technical identifiers to user-friendly labels in `selectbox` or `radio` inputs.
