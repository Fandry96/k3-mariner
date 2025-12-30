# [RELEASE] K3 Mariner: The Unofficial Open-Source Alternative to "Project Mariner"

**Protocol**: `ANTIGRAVITY DROP`
**Target**: r/googleantigravity

---

### The Tale of Two Mariners

If you follow DeepMind, you know about **"Project Mariner"**—their experimental Gemini 2.0 agent that autonomously surfs the web in Chrome. It's incredible technology. It's also currently **closed access** (Waitlist/AI Ultra).

**We didn't want to wait.**

So we built **K3 Mariner (Community Edition)**.

This is **NOT** Google's internal tool. This is an open-source "Code Agent" built on Hugging Face's `smolagents` library, tuned to run on **Gemini 1.5 Flash** (via LiteLLM) right now, today, on your local machine.

### Why use this?

1. **It Exists**: You can run it today.
2. **No 404 Errors**: We solved the Gemini API connectivity issues plaguing other frameworks by using "Evergreen" model pointers.
3. **Transparent Thought**: Includes a "Research Cockpit" (Streamlit UI) that lets you see exactly what the agent is thinking and coding in real-time.

### Features

* **Deep Coder Engine**: Writes Python code to solve problems.
* **Gemini Native**: Optimized for `gemini-1.5-flash-latest`.
* **Zero-Config**: `pip install -r requirements.txt` -> `streamlit run app.py`.

### Artifacts Included

I've packaged this up for the community:

* `agent.py`: The core logic (Sanitized & Persona-Injected).
* `app.py`: The Research Cockpit UI.
* `smolagents_bible.md`: A 2,000-word reference manual on how to build high-reliability agents with this stack.

### Usage

1. Download the package (Link below).
2. Install dependencies.
3. Run the app.
4. Enter your Google API Key.
5. *Sail.*

### 🔮 Roadmap: The Full Stack Matryoshka

The Community Edition is designed for speed and simplicity. But the "Pro" integration is coming.

* **MRL Memory Integration**: Connect Mariner to your local vector store (Matryoshka Representation Learning).
* **Tiered Reasoning**: 64-dim binary retrieval for speed, 768-dim float retrieval for deep synthesis.
* **Zero-Config RAG**: Drag-and-drop document indexing.

*"The Agent is the Cortex. MRL is the Hippocampus."*

**Source Code:** [https://github.com/Fandry96/k3-mariner](https://github.com/Fandry96/k3-mariner)

*Gravity is optional.*
