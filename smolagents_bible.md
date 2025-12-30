# The Smolagents Bible

## Community Edition | v1.23.0

> **Note:** This document is a consolidated reference for the `smolagents` library, derived from official documentation and practical implementation patterns. It serves as a guide for building robust, "Evergreen" agents.

---

## 1. Core Concepts: Agentic Systems

### What are Agents?

Agents are programs where **LLM outputs control the workflow**. Agency exists on a spectrum:

* **Simple Processor**: LLM processes input, no flow control.
* **Router**: LLM decides if/else paths.
* **Tool Calling**: LLM selects functions and arguments to execute.
* **Multi-step Agent**: LLM controls iteration (loops) and program continuation.
* **Multi-Agent**: Workflows triggering other agentic workflows.

### Why Code Agents?

`smolagents` prioritizes **Code Agents** over JSON-based tool calling.

* **Composability**: Code allows nesting and reusable definitions.
* **Object Management**: Native handling of complex objects (e.g., images, dataframes) without serialization bottlenecks.
* **Generality**: Code can express any computational task.
* **Training Data**: LLMs are heavily trained on code, making them naturally proficient at it.

---

## 2. Agents API

### Base Class: `MultiStepAgent`

The foundation for agents acting in steps (Thought → Tool Call → Execution).

* **Key Parameters**: `model`, `tools`, `max_steps`, `verbosity_level`.
* **Methods**:
  * `run(task, ...)`: Executes the agent on a task.
  * `step(memory_step)`: Performs a single ReAct step.
  * `replay()`: Replays the agent's history.
  * `write_memory_to_messages()`: Formats memory for LLM context.

### Implementations

#### 1. `CodeAgent` (Recommended)

Writes tool calls in **Python code**.

* **Executor**: Uses a local or remote Python executor (secure sandbox).
* **Features**: Supports complex logic, variables, and imports (if authorized).

#### 2. `ToolCallingAgent`

Writes tool calls in **JSON**.

* **Use Case**: For models strictly tuned for JSON tool calling or when legacy compatibility is required.

#### 3. Managed Agents

Agents that can be called by other agents.

* Pass a list of agents to the `managed_agents` parameter of a manager agent.
* Allows hierarchical task delegation (e.g., a Manager delegates web search to a SearchAgent).

---

## 3. Tools API

### Defining Tools

Tools are classes wrapping functions with metadata.

#### Class-Based Definition (Standard)

Subclass `smolagents.Tool`:

```python
from smolagents import Tool

class MyTool(Tool):
    name = "tool_name"
    description = "Description for the LLM."
    inputs = {"arg_name": {"type": "string", "description": "..."}}
    output_type = "string"

    def forward(self, arg_name: str):
        # Implementation
        return "result"
```

#### Decorator-Based

Use `@tool` for simple functions.

### Built-in Tools

* **Information**: `DuckDuckGoSearchTool`, `GoogleSearchTool`, `WikipediaSearchTool`.
* **Web**: `VisitWebpageTool` (navigates and reads pages).
* **System**: `PythonInterpreterTool`, `FinalAnswerTool`.
* **Multimodal**: `SpeechToTextTool`.

### Tool Collections & Hub

* **From Hub**: `load_tool("username/tool-name", trust_remote_code=True)`
* **From Spaces**: `Tool.from_space("space-id", ...)` imports Gradio spaces as tools.
* **ToolCollection**: `ToolCollection.from_hub(slug)` loads entire suites of tools.

### MCP (Model Context Protocol)

Connect to external data and tools via MCP servers.

* **Stdio**: Spawns a local subprocess (e.g., `uvx` command).
* **HTTP**: Connects to remote MCP endpoints.
* **Structured Output**: Enable `structured_output=True` to handle complex objects from MCP tools.

---

## 4. Models API

`smolagents` supports any LLM backend via the `Model` abstraction.

### Implementations

* **`TransformersModel`**: Runs local Hugging Face models using `transformers` (requires GPU).
* **`InferenceClientModel`**: Connects to Hugging Face Inference API (Serverless or Dedicated endpoints) and providers like Falcon, Fireworks, Together, etc.
* **`LiteLLMModel`**: Proxies requests via LiteLLM to support 100+ providers (Anthropic, Gemini, DeepSeek, etc.).
* **`OpenAIModel` / `AzureOpenAIModel`**: Native support for OpenAI-compatible APIs.
* **`AmazonBedrockModel`**: Connects to AWS Bedrock.
* **`MLXModel`**: Runs local models on Apple Silicon (M-series chips).

### Configuration

All models accept generation parameters (`temperature`, `max_tokens`, `top_p`) at instantiation.

---

## 5. Security & Sandboxing

**Warning**: Local code execution carries inherent risk.

### Local Python Executor (`LocalPythonExecutor`)

The default executor for `CodeAgent`.

* **Mechanism**: AST parsing (not eval).
* **Restrictions**:
  * Imports must be explicitly authorized.
  * No access to dangerous submodules (e.g., `random._os`).
  * Operation limits to prevent infinite loops.
* **Verdict**: Safer than `exec()`, but not a true sandbox.

### Remote Sandboxes (Recommended for Production)

For complete isolation, use `executor_type=` in `CodeAgent`.

1. **Blaxel** (`executor_type="blaxel"`):
    * Fast startup (<25ms).
    * Hibernates to zero.
    * Secure VM isolation.
2. **E2B** (`executor_type="e2b"`):
    * Dedicated cloud sandbox.
    * Requires E2B API key.
3. **Modal** (`executor_type="modal"`):
    * Runs execution in Modal containers.
4. **Docker** (`executor_type="docker"`):
    * Runs code in a local Docker container.
    * Requires Docker daemon.
5. **WebAssembly** (`executor_type="wasm"`):
    * Uses Pyodide + Deno.
    * Local process, but strictly sandboxed memory and capabilities.

---

## 6. Telemetry & Observability (OpenTelemetry)

Instrumentation is critical for debugging agent logic.

### Supported Integrations

* **Phoenix (Arize AI)**:
  * Install: `pip install 'smolagents[telemetry,toolkit]'`
  * Run: `python -m phoenix.server.main serve`
  * Instrument: `SmolagentsInstrumentor().instrument()`
* **Langfuse**:
  * Set `LANGFUSE_PUBLIC_KEY`, `LANGFUSE_SECRET_KEY`, `LANGFUSE_HOST`.
  * Instrument: `SmolagentsInstrumentor().instrument()`

---

## 7. Security & Configuration (The "Evergreen" Standard)

### Gemini / LiteLLM Integration Patterns

To ensure stability ("Evergreen" status) when using Google Gemini with `smolagents`, follow these strict configuration rules:

1. **Explicit API Key Passing:** Do not rely on implicit environment variable resolution by `litellm`. Pass the key explicitly.
2. **Model ID Prefix:** Always prefix the model ID with `gemini/`.
3. **Evergreen Model IDs:** Use dynamic pointers like `gemini/gemini-flash-latest` or `gemini/gemini-pro-latest` to avoid 404 errors with deprecated hard versions.
4. **Custom Provider:** Explicitly set `custom_llm_provider="gemini"` in `LiteLLMModel`.

#### Verified Code Snippet

```python
model_engine = LiteLLMModel(
    model_id="gemini/gemini-flash-latest", # Evergreen Pointer
    api_key=os.environ["GOOGLE_API_KEY"],  # Explicit Key
    custom_llm_provider="gemini",          # Explicit Provider
    temperature=0.0
)
```

### Dependency Management

* **`smolagents` vs `duckduckgo-search`:** The built-in `DuckDuckGoSearchTool` in `smolagents` can be fragile. It is recommended to implement a custom `Tool` wrapper around `duckduckgo_search` for better error handling and control.

---

## 8. Advanced Workflows

### Async Integration

Run synchronous agents in async apps (e.g., Starlette/FastAPI) using threading.

```python
# Starlette example
import anyio.to_thread
result = await anyio.to_thread.run_sync(agent.run, task)
```

### Memory Management

* **Replay**: `agent.replay()` to visualize past runs.
* **Inspection**: Access `agent.memory.steps` (list of `ActionStep`, `TaskStep`).
* **Callbacks**: Use `step_callbacks=[callback_function]` to modify memory dynamically (e.g.,pruning old screenshots).
* **Step-by-Step Execution**: Manually call `agent.step(memory_step)` for fine-grained control or long-running tasks.
