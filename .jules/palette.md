## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2024-05-23 - Mapping Technical IDs to User-Friendly Display Names
**Learning:** Users can be confused by technical IDs in selectboxes (e.g., "gemini/gemini-flash-latest"). Using the `format_func` parameter in Streamlit's `selectbox` widget maps technical identifiers to user-friendly display names without altering the underlying return values.
**Action:** Always use a mapping dictionary and `format_func` in `selectbox` for technical IDs to ensure clarity for users while maintaining backend functionality.

## 2026-09-17 - Streamlit Tooltip Accessibility Pattern
**Learning:** In Streamlit applications, tooltips on elements like buttons are not stored in standard HTML title attributes but are rendered within a parent wrapper using `data-testid='stTooltipHoverTarget'`. This nested DOM structure requires specific scoping when locating tooltips to avoid strict mode violations during automated accessibility verification.
**Action:** When verifying tooltips on Streamlit buttons, always scope the locator to the specific parent component, such as `page.get_by_test_id("stFormSubmitButton").get_by_test_id("stTooltipHoverTarget")`.
