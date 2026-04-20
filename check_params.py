import inspect
import streamlit as st

sig = inspect.signature(st.form_submit_button)
print(sig.parameters)
