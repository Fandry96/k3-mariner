import os
import sys
from dotenv import load_dotenv

# Framework Imports
try:
    from smolagents import CodeAgent, LiteLLMModel, Tool, FinalAnswerTool
except ImportError:
    print("CRITICAL: 'smolagents' not installed. Run: pip install smolagents litellm")
    sys.exit(1)

# Search Dependency
try:
    from duckduckgo_search import DDGS
except ImportError:
    DDGS = None

load_dotenv(override=True)


class MarinerSearchTool(Tool):
    name = "web_search"
    description = (
        "Performs a web search using DuckDuckGo. Returns a summary of top results."
    )
    inputs = {
        "query": {
            "type": "string",
            "description": "The search query string. Be specific.",
        }
    }
    output_type = "string"

    def forward(self, query: str) -> str:
        """
        Executes the search with error handling for rate limits.
        """
        if DDGS is None:
            return "ERROR: 'duckduckgo_search' library is missing."

        try:
            # max_results=5 provides a good balance of context vs token usage
            with DDGS() as ddgs:
                results = list(ddgs.text(query, max_results=5))

            if not results:
                return "No results found."

            # Format results for the Agent's consumption
            # Optimization: Use generator expression to save memory
            formatted = "\n".join(
                f"- [Title]: {r.get('title', 'N/A')}\n  [Link]: {r.get('href', 'N/A')}\n  [Snippet]: {r.get('body', 'N/A')}"
                for r in results
            )
            return formatted

        except Exception as e:
            return f"SEARCH FAILED: {str(e)}"


class K3MarinerAgent(CodeAgent):
    """
    K3MarinerAgent: Autonomous Research Unit (Community Edition).
    """

    def __init__(self, model_id: str = "gemini/gemini-flash-latest", **kwargs):
        # 1. API Key Resolution (Standard Env Var)
        api_key = os.getenv("GOOGLE_API_KEY")

        if not api_key:
            print("[ERROR] NO API KEY FOUND.")
            print("Please set GOOGLE_API_KEY in a .env file or export it.")
            print("Tip: See GUIDE.md for configuration instructions.")
            sys.exit(1)

        # 2. Model Engine Configuration
        # LiteLLM requires specific handling for Gemini to ensure it uses the correct endpoint.
        # "Evergreen" Model Pointer: gemini-flash-latest
        self.model_engine = LiteLLMModel(
            model_id=model_id,
            api_key=api_key,
            # 'custom_llm_provider' helps LiteLLM route correctly if model_id is ambiguous
            custom_llm_provider="gemini",
            temperature=0.0,  # Precision mode
            max_tokens=8192,
        )

        # 3. Toolset Assembly
        self.toolbox = [
            MarinerSearchTool(),
            FinalAnswerTool(),
        ]

        # 4. K3 Mariner Persona
        # We inject a specialized system prompt to govern the agent's behavior.
        self.system_prompt = """
        IDENTITY:
        You are K3 MARINER, an autonomous research unit (Community Edition).
        
        DIRECTIVES:
        1. PRECISION: Your code must be exact. Avoid "hallucinated" imports.
        2. VERIFICATION: Verify information before reporting it as fact.
        3. FORMAT: Use clear, structured output. Use ASCII tables if presenting data.
        4. TONE: Professional, succinct, and cybernetic.
        
        PROTOCOL:
        - When solving a task, always THINK first to plan your approach.
        - Write robust Python code with error handling.
        - If a tool fails, analyze the error and TRY AGAIN with a different strategy.
        - CITE YOUR SOURCES.
        """

        super().__init__(
            tools=self.toolbox,
            model=self.model_engine,
            add_base_tools=False,  # We control the toolset explicitly
            verbosity_level=1,
            max_steps=15,
            **kwargs,
        )
        # Manually override the system prompt if the library allows,
        # or we will prepend it to tasks.
        self.system_prompt_template = self.system_prompt
        print(f"[Mariner] ONLINE. Engine: {model_id}")


if __name__ == "__main__":
    print("[System] Initializing Mariner Protocol...")

    try:
        agent = K3MarinerAgent()

        query = "What is the latest version of the 'smolagents' library on PyPI?"
        print(f"\n[Task] {query}\n")

        result = agent.run(query)

        print("\n" + "=" * 40)
        print(f"[FINAL ANSWER]: {result}")
        print("=" * 40)

    except Exception as e:
        print(f"\n[CRITICAL FAILURE]: {e}")
