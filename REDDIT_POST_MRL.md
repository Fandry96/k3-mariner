# Reddit Thread Title

**[P] I built a "Ctrl+F for Meaning" that runs on a potato (MRL Explained)**

## Post Body

**The Problem:**
I wanted to build a RAG app (Chat with my Codebase), but I didn't want to pay for a vector database (Pinecone/Weaviate) or run a heavy Docker container. I just wanted a simple python script I could run anywhere.

**The Solution: MRL (Matryoshka Representation Learning)**
I built **MRL v2.0**. It's an open-source indexer that uses Google's new Gemini Flash embeddings. But here is the cool part: **It shrinks vectors.**

**ELI5: How it works (The Potato Explanation)**

1. **Standard Embeddings**: Usually, when AI reads your code, it turns it into a list of **768 numbers**. Think of this like a **4K Ultra-HD photo**. It has tons of detail, but the file size is huge.
2. **MRL (The Magic)**: Matryoshka learning is like realizing you can shrink that 4K photo down to a pixelated **Thumbnail** (128 numbers).
3. **The Trick**: Even though it's blurry (compressed), **you can still tell it's a cat.**
4. **The Result**: My search index is **6x smaller** (83% reduction). I can fit thousands of code files into a tiny file that loads instantly on a laptop (or a toaster).

**New Features in v2.0 (The "Beast Mode" Update):**

* 🦁 **--beast**: A flag that disables all safety brakes. It batches 50 files at once and ingests faster than you can read this.
* 🧠 **GAG Protocol**: The search doesn't just return code chunks. It adopts a specific "Chief Architect" persona to answer your question without fluff.

**Repo (Open Source):**
[https://github.com/Fandry96/MRL](https://github.com/Fandry96/MRL)

It's literally one Python file.
`pip install -r requirements.txt` and `python indexer.py --beast`.

Let me know if you break it.
