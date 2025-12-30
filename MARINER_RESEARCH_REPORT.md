# Research Report: The Tale of Two Mariners

## Executive Summary

There is a naming collision.

* **Google's "Project Mariner"**: A proprietary, experimental Chrome extension DeepMind agent powered by Gemini 2.0 (Prototype status, limited access).
* **K3's "Mariner"**: An open-source, `smolagents`-based Python agent named "Mariner" (Community Edition).

## The "Real" Project Mariner (Google)

* **Architecture**: Gemini 2.0 foundation.
* **Form Factor**: Chrome Extension.
* **Core Loop**: Observe-Plan-Act (OPA) completely within the browser DOM.
* **Capabilities**: Heavy focus on visual grounding, DOM manipulation, and user-supervised autonomy.
* **Availability**: Extremely limited (US AI Ultra subscribers, experimental).

## The Risk

Releasing our agent as simply "Mariner" on `r/googleantigravity` will cause confusion. Users may think:

1. We leaked Google's internal code.
2. We are masquerading as Google.
3. It's a "fan game" that doesn't work.

## The Strategy: "The Antigravity Alternative"

We lean into the collision. We position our Mariner as the **"Open Source Homage"** or **"The Mariner You Can Actually Use."**

### Differentiation Matrix

| Feature | Google's Mariner | K3's Mariner (Antigravity) |
| :--- | :--- | :--- |
| **Engine** | Gemini 2.0 (Proprietary) | Gemini 1.5 Flash (via LiteLLM) |
| **Access** | Waitlist / AI Ultra | Open Source (GitHub/Gist) |
| **Framework** | Internal DeepMind | Hugging Face `smolagents` |
| **Philosophy** | "Let us browse for you" | "Build your own agent" |

## Recommendation for Reddit Post

Rename the post title to facilitate clarity:

* **Old**: "[RELEASE] Mariner v1.2: Zero-Config Gemini Agent..."
* **New**: "[RELEASE] Mariner (Community Edition): The Open-Source Alternative to DeepMind's Project Mariner"

**Narrative Hook**: "Google has 'Project Mariner' (Gemini 2.0 browser agent). It's cool, but you can't have it yet. So I built my own using `smolagents` and Gemini Flash. Here is the code."
