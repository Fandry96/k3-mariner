# K3 Mariner: Autonomous Research Unit (v1.2) - Community Release

> **Operation ANTIGRAVITY DROP**
> A "Zero-Config" autonomous research agent powered by `smolagents` and `Gemini`.

## What is this?

K3 Mariner is a lightweight, neuro-symbolic research agent. It combines:

1. **Smolagents**: Hugging Face's minimalist agent framework for "Code Agents".
2. **Gemini 1.5 Flash**: Google's high-speed, low-cost reasoning model.
3. **Streamlit**: A dashboard for real-time thought observation.

## Features

- **Deep Coder Engine**: Writes its own Python code to solve tasks.
- **Evergreen Stability**: Configured to avoid common `404` errors with Gemini API.
- **Research Cockpit**: A UI to watch the agent "think" in real-time.
- **Precision Mode**: `temperature=0.0` for deterministic outputs.

## Quickstart

### 1. Prerequisites

- Python 3.10+
- A Google Cloud API Key (AI Studio)

### 2. Install

```bash
pip install -r requirements.txt
```

### 3. Configure

Create a `.env` file (Required for CLI mode):

```ini
GOOGLE_API_KEY=your_key_here
```

> **Note**: If using the UI (`app.py`), you can enter this key in the sidebar instead.

### 4. Run (CLI Mode)

Execute the agent directly in terminal:

```bash
python agent.py
```

### 5. Run (UI Mode)

Launch the Research Cockpit:

```bash
streamlit run app.py
```

## Documentation

See `smolagents_bible.md` for a comprehensive guide on the underlying framework and architecture.

## 🔮 Roadmap

* **MRL Integration**: Future versions will support "Resolution Matching" to connect with local Vector/MRL stores.
- **Tool Plugins**: Drop-in support for additional MCP tools.

## License

MIT License. Free to fork, modify, and deploy.
