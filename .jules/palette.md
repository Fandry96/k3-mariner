## 2024-05-23 - API Key Onboarding
**Learning:** Users often stall at the "API Key" input if they don't know where to get one. Streamlit's `help` tooltip is a low-intrusiveness way to provide this link.
**Action:** Always include a `help` parameter with a direct URL for any external service credential input.

## 2025-02-18 - Enter-to-Submit with Invisible Forms
**Learning:** Streamlit users expect "Enter" to submit text inputs. `st.form(border=False)` combined with `st.form_submit_button` enables this without altering the visual layout.
**Action:** Always wrap single-input search/action patterns in a borderless form.
