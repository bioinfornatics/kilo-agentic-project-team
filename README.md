# Kilo Code Web Starter (RAG‑ready)

A preconfigured starter for **Kilo Code** to speed up web projects with:
- **Custom personas** (single project‑level `./.kilocodemodes` JSON)
- **Role‑based routing rules** for retrieval/RAG
- **Cross‑cutting rules** (retrieval policy, prefixes, orchestrator cues)
- **Workflows** (slash commands)
- **Memory Bank** skeleton
- **Specs & UI** scaffolding
- **Qdrant** bootstrap for semantic codebase indexing
- A small **planner** to track tasks

> Explanations in this README are in **English**. Use the repository “as is” with the Kilo Code VS Code extension.

---

## Quick Start

### Prerequisites
- **VS Code** with the **Kilo Code** extension installed
- **Python ≥ 3.10** (for any scripts/tests you add)
- **Docker** or **Podman** (to run local services like Qdrant and Penpot)

### Steps

1. **Integrate the starter into your project:**
   - **Option 1:** Rename the `my-project` folder to your project name and work directly inside it.
   - **Option 2:** Copy the following into your existing project:
     - `.kilocode`
     - `.kilocodemodes`
     - `projects/`
   
2. **Launch preconfigured services** (Penpot & Qdrant):
   - Navigate to `penpot/` and run:
     ```bash
     podman-compose up -d
     ```
   - Navigate to `qdrant/` and run:
     ```bash
     podman-compose up -d
     ```

3. **Open the project in VS Code** with **Kilo Code** enabled.

4. **Run the workflows**:
   - `my-project/onboarding-web.md`
   - `my-project/enable-indexing.md`
   - `my-project/update-memory-bank.md`

5. **Test your setup**:
   - Try a quick task like *"Write an E2E test for login"*.
   - The orchestrator should switch to the `qa-engineer` mode automatically.
