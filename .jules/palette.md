## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2024-05-23 - Mapping Technical IDs to User-Friendly Display Names
**Learning:** Users can be confused by technical IDs in selectboxes (e.g., "gemini/gemini-flash-latest"). Using the `format_func` parameter in Streamlit's `selectbox` widget maps technical identifiers to user-friendly display names without altering the underlying return values.
**Action:** Always use a mapping dictionary and `format_func` in `selectbox` for technical IDs to ensure clarity for users while maintaining backend functionality.
## 2024-11-04 - Improve Model Dropdown Readability
**Learning:** Raw API identifiers like 'gemini/gemini-flash-latest' make poor UI text, but simple title-casing can result in clumsy redundancies (e.g. 'Gemini Gemini'). Custom formatting functions are needed to clean them up properly.
**Action:** Use `format_func` in `st.selectbox` to map raw backend IDs to clean, human-readable display names by removing repetitive prefixes and replacing hyphens with spaces.
