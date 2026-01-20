import sys
import os
import re
from unittest.mock import MagicMock

# Add parent directory to path so we can import app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Mock streamlit before importing app, because app.py has side effects (st.set_page_config)
sys.modules["streamlit"] = MagicMock()
sys.modules["smolagents"] = MagicMock()
sys.modules["duckduckgo_search"] = MagicMock()
sys.modules["litellm"] = MagicMock()

# Now we can import the function we want to test
from app import clean_ansi

def test_clean_ansi_simple():
    text = "Hello \x1b[31mWorld\x1b[0m"
    cleaned = clean_ansi(text)
    assert cleaned == "Hello World"

def test_clean_ansi_complex():
    text = "\x1b[1m\x1b[31mError:\x1b[0m Something went wrong"
    cleaned = clean_ansi(text)
    assert cleaned == "Error: Something went wrong"

def test_clean_ansi_no_ansi():
    text = "Just plain text"
    cleaned = clean_ansi(text)
    assert cleaned == "Just plain text"

if __name__ == "__main__":
    test_clean_ansi_simple()
    test_clean_ansi_complex()
    test_clean_ansi_no_ansi()
    print("All tests passed!")
