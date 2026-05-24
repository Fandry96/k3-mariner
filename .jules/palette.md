## 2024-05-24 - Form UX polish
**Learning:** Using `format_func` in Streamlit's `selectbox` is an excellent way to maintain technical identifiers while presenting a user-friendly interface. Additionally, relying on backend errors for empty queries is a poor UX pattern in Streamlit; inline `st.warning` checks provide much faster, clearer feedback.
**Action:** Always map technical IDs to human-readable strings using `format_func` in selectboxes, and proactively validate text inputs before passing them to expensive agent runs.
