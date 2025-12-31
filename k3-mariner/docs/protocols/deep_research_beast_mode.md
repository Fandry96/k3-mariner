# Deep Research Protocol (Beast Mode)

The "Beast Mode" protocol is the K3 standard for high-bandwidth research sprints. It prioritizes rapid ingestion, dense synthesis, and strategic implication extraction.

## 1. The Five-Stage Loop

Derived from the `research.md` workflow (Dec 30, 2025).

### Stage 1: The Librarian (Structuring)

- **Action**: Define the scope, locate sources (files, URLs, terminal outputs), and initialize a dedicated research directory.
- **Goal**: Minimize "Search Space" noise.

### Stage 2: Beast Mode Ingestion (High-Bandwidth)

- **Action**: Execute ingestion scripts (e.g., `docx_reader.py`, `epub_ripper.py`) to convert binary/fragmented sources into clean Markdown.
- **Protocol**: Raw reading without judgment. The focus is on raw data throughput.

### Stage 3: Map & Reduce (Synthesis)

- **Action**: Process the clean Markdown chunks.
- **Mapping**: Identifying key terms, entities, and unique technical patterns.
- **Reducing**: Consolidating duplicate findings and resolving contradictions between sources.

### Stage 4: Chain of Density (Refinement)

- **Action**: Iteratively condense the findings.
- **Constraint**: Each pass must maintain information density while reducing word count.
- **Ref**: GAG "Zero-Fluff" principle.

### Stage 5: Final Output (The Brief)

- **Format**: Structured Markdown report.
- **Criteria**:
  - Explicit citations.
  - 0% generic fluff.
  - **Strategic Implications**: A dedicated section explaining *why* this matters for the K3 ecosystem (e.g., "This tool reduces token cost by 25%").

## 2. Beast Mode Personas

- **The Auditor (Fiduciary Sentinel)**: Invoked during Stage 2/3 to fact-check sources and flag risks.
- **GAG Chief**: Oversees the entire sprint, enforcing the 120-minute time cap and conciseness.

## 3. Tooling Integration

- **SISA Tools**: Used for Stage 1/2 to "crack open" opaque containers.
- **MRL (Matryoshka Retrieval)**: Used in Stage 3 to search through massive ingested corpora without blowing the context window.
