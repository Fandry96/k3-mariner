or [RELEASE] K3 Mariner: A Neuro-Symbolic Approach to Local Agentic Inference

**Protocol**: `ANTIGRAVITY DROP`
**Target**: r/LocalLLaMA, r/MachineLearning

---

### Abstract

While DeepMind's "Project Mariner" demonstrates state-of-the-art performance in autonomous web navigation, its closed-source nature limits architectural introspection. We present **K3 Mariner (Community Edition)**, an open-source implementation of a Neuro-Symbolic Code Agent, built on the `smolagents` framework and optimized for the Gemini 1.5 Flash inference endpoint. This release democratizes access to "Type 2" Agentic Reasoning patterns, specifically integrating **ReFRAG (Recursive Fragmented Retrieval Augmented Generation)** and **Matryoshka Representation Learning (MRL)** for tiered memory access.

### 1. Architectural Overview

K3 Mariner operates on a modified **ReAct (Reasoning + Acting)** loop, enhanced by a **Cognitive Stratification** layer that decouples "Senses" (Tool Use) from "Brain" (Reasoning).

* **Logic Core**: `smolagents.CodeAgent` (Python AST Execution).
* **Inference Engine**: `LiteLLM` bridge to `gemini-1.5-flash-latest` (Zero-Shot Chain-of-Thought).
* **Observability**: Real-time Streamlit visualization of the "Thought-Action-Observation" trace.

### 2. The Innovation: Resolution Matching (MRL)

Current RAG implementations suffer from the "Context Economy" problem—fixed vector sizes (768d/1536d) create latency bottlenecks at scale. K3 Mariner introduces a **Tiered Retrieval Strategy** based on Matryoshka Representation Learning:

* **Tier 1 (Routing)**: Fast approximate nearest neighbor search using **64-dim** binary vectors.
* **Tier 2 (Senses)**: Re-ranking and filtering using **128-dim** vectors.
* **Tier 3 (Brain)**: Full context synthesis using **768-dim** high-fidelity vectors.

This "Funnel" architecture allows for **O(log n)** retrieval complexity while maintaining high precision for the final context window.

### 3. The ReFRAG Protocol (Micro-Chunking)

To solve the "Needle in a Haystack" problem in code traversal, we implement **ReFRAG**:

* **Micro-Chunks**: 16-token sliding windows with 8-token stride.
* **Dense Clustering**: Identifying "Density Peaks" in the vector space to localize retrieval target zones.
* **Zero-Config Indexing**: Automatic ingestion of local repositories without manual vector store setup.

### 4. Implementation Details

The agent is packaged as a standalone Python application with a Streamlit frontend.

* **Code Sandbox**: Local execution env with `pandas`, `requests`, `bs4`, and `markdownify`.
* **Safety**: "Fiduciary Sentinel" logic guards against destructive file operations (AST-level whitelist).
* **Connectivity**: Solves the generic `404` upstream model errors via "Evergreen" pointer resolution.

### 5. Research Implications

K3 Mariner serves as a baseline platform for researching **Agentic Flow Engineering**. By exposing the raw thought trace and offering a modular tool interface, researchers can experiment with:

* **Dynamic Tool Synthesis**: Agent writing its own tools.
* **Multi-Agent Swarm topologies**: Mariner + Opal + Writer.
* **Evolutionary Prompt Optimization**.

---

**Repository:** <https://github.com/Fandry96/k3-mariner>

**Citation:**

* **ReFRAG Protocol**: Adapted from the `Context-Engine` architectural patterns by **u/voarsh** (m1rl0k).
* *Promarkia, et al. "Agentic Operations: The Squad Model." 2025.*
* *Kusupati, et al. "Matryoshka Representation Learning." NeurIPS 2022.*
