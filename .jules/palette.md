## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2024-10-24 - Verifying Streamlit Tooltips
**Learning:** Streamlit renders `help` parameters as elements with `data-testid="stTooltipIcon"`. This allows for reliable automated verification of help text presence using Playwright.
**Action:** Use `page.locator("[data-testid='stTooltipIcon']").count()` to verify accessible help text coverage in future Streamlit apps.
