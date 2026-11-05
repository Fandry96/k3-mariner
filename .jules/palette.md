## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2024-05-23 - Mapping Technical IDs to User-Friendly Display Names
**Learning:** Users can be confused by technical IDs in selectboxes (e.g., "gemini/gemini-flash-latest"). Using the `format_func` parameter in Streamlit's `selectbox` widget maps technical identifiers to user-friendly display names without altering the underlying return values.
**Action:** Always use a mapping dictionary and `format_func` in `selectbox` for technical IDs to ensure clarity for users while maintaining backend functionality.

## 2024-11-05 - Model Name Deduplication
**Learning:** Naively capitalizing model IDs like `gemini/gemini-flash-latest` can result in clumsy UI text like "Gemini Gemini Flash Latest".
**Action:** Use a specific string replacement (e.g., replacing the entire `gemini/gemini-` prefix) in the `format_func` to ensure a clean, redundant-free display name.
