import streamlit as st
import os
import sys
import re
import time
from io import StringIO
from contextlib import contextmanager
from dotenv import load_dotenv

# --- FRAMEWORK INJECTION ---
try:
    from smolagents import CodeAgent, LiteLLMModel, Tool, FinalAnswerTool
    from duckduckgo_search import DDGS
except ImportError:
    st.error(
        "CRITICAL: Missing dependencies. Run: `pip install smolagents litellm duckduckgo-search`"
    )
    st.stop()

load_dotenv(override=True)

# --- CONFIGURATION ---
st.set_page_config(
    page_title="K3 MARINER | Research Unit",
    page_icon="⚓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- STYLING ---
st.markdown(
    """
<style>
    .stApp { background-color: #050505; color: #e0e0e0; }
    .stTextInput > div > div > input { background-color: #1a1a1a; color: #00ff00; border: 1px solid #333; }
    .stMarkdown code { background-color: #222; color: #ffcc00; }
    div[data-testid="stMetricValue"] { font-family: 'Courier New', monospace; color: #00ff00; }
</style>
""",
    unsafe_allow_html=True,
)


# --- HELPER FUNCTIONS ---
# Pre-compile regex for performance
ANSI_ESCAPE = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")


@st.cache_data(ttl=3600, show_spinner=False)
def perform_search(query: str):
    """Cached DuckDuckGo search to prevent redundant network calls."""
    with DDGS() as ddgs:
        return list(ddgs.text(query, max_results=5))


# --- TOOL DEFINITION ---
class MarinerSearchTool(Tool):
    name = "web_search"
    description = "Searches the web using DuckDuckGo. Returns top 5 results."
    inputs = {"query": {"type": "string", "description": "Search query."}}
    output_type = "string"

    def forward(self, query: str) -> str:
        try:
            results = perform_search(query)
            if not results:
                return "No results found."
            return "\n".join(
                [f"- {r.get('title', '')} ({r.get('href', '')})" for r in results]
            )
        except Exception as e:
            return f"Search Error: {e}"


# --- AGENT ENGINE ---
@st.cache_resource
def get_agent(_api_key, model_id):
    """Initializes the Mariner Agent with cached resources."""
    if not _api_key:
        return None

    model = LiteLLMModel(
        model_id=model_id,
        api_key=_api_key,
        custom_llm_provider="gemini",
        temperature=0.0,
        max_tokens=8192,
    )

    return CodeAgent(
        tools=[MarinerSearchTool(), FinalAnswerTool()],
        model=model,
        add_base_tools=False,
        verbosity_level=1,
        max_steps=10,
        # Mariner Persona
        # Note: smolagents CodeAgent might expect prompt_templates in recent versions,
        # but passing it here or handling it via prompt templates is key.
        # For simplicity in this release, we'll keep it minimal or pass custom args if supported.
    )


# --- CAPTURE UTILS ---
def clean_ansi(text):
    """Removes ANSI escape sequences from text using pre-compiled regex."""
    return ANSI_ESCAPE.sub("", text)


@contextmanager
def capture_stdout(placeholder):
    """Redirects stdout to a Streamlit placeholder in real-time with throttling.

    Optimized to clean ANSI codes incrementally, avoiding O(N^2) string processing.
    """
    clean_buffer = StringIO()
    old_out = sys.stdout

    # State for throttling
    state = {"last_update_time": 0}
    UPDATE_INTERVAL = 0.1  # 100ms (10Hz)

    # State for incremental ANSI cleaning
    ansi_state = {"incomplete": ""}

    def update(force=False):
        current_time = time.time()

        # Only update if enough time has passed or forced
        if force or (current_time - state["last_update_time"] >= UPDATE_INTERVAL):
            # Display cached clean text
            placeholder.code(clean_buffer.getvalue(), language="text")
            state["last_update_time"] = current_time

    class RealTimeStream:
        def write(self, s):
            # Handle potential split ANSI codes (e.g., streaming output)
            text = s
            if ansi_state["incomplete"]:
                text = ansi_state["incomplete"] + text
                ansi_state["incomplete"] = ""

            # Heuristic: if chunk ends with ESC, buffer it
            if text.endswith("\x1B"):
                ansi_state["incomplete"] = "\x1B"
                text = text[:-1]

            if not text:
                return

            # Clean the new chunk and append to buffer
            clean_text = clean_ansi(text)
            clean_buffer.write(clean_text)

            # Force update on newline to simulate streaming
            if "\n" in s:
                update()

        def flush(self):
            old_out.flush()

    sys.stdout = RealTimeStream()
    try:
        yield
    finally:
        sys.stdout = old_out
        update(force=True)  # Final flush


# --- UI LAYOUT ---
with st.sidebar:
    st.header("⚓ K3 MARINER")
    st.caption("Community Edition v1.2")

    # Standard Env Var
    default_key = os.getenv("GOOGLE_API_KEY", "")
    api_key = st.text_input(
        "Google API Key",
        type="password",
        value=default_key,
        help="Get your key at https://aistudio.google.com/app/apikey",
    )

    # "Evergreen" model pointers
    model_choice = st.selectbox(
        "Model Core", ["gemini/gemini-flash-latest", "gemini/gemini-pro-latest"]
    )

    st.divider()
    st.metric("Agent Status", "ONLINE" if api_key else "OFFLINE")

st.title("Deep Research Protocol")
query = st.text_input(
    "Mission Objective", placeholder="e.g., What is the release date of Gemini 3 Pro?"
)

if st.button("EXECUTE", type="primary"):
    if not api_key:
        st.error("API Key required.")
    else:
        agent = get_agent(api_key, model_choice)
        log_container = st.empty()
        result_container = st.container()

        with st.spinner("Mariner is navigating..."):
            try:
                # Capture the agent's "Thinking" (stdout)
                with capture_stdout(log_container):
                    response = agent.run(query)

                # Display Result
                with result_container:
                    st.success("Mission Complete")
                    st.markdown("### Final Report")
                    st.markdown(response)

            except Exception as e:
                st.error(f"Mission Failed: {str(e)}")
