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

## 1) Quick start

### Prerequisites
- **VS Code** with the **Kilo Code** extension installed
- **Node.js ≥ 20** (for scripts/tests you add)
- **Docker** (to run local **Qdrant** for indexing)

### Steps
1. Extract the archive at the **root** of your repository.
2. Open the folder in VS Code with **Kilo Code** enabled.
3. Run the workflows:
   - `/onboarding-web.md`
   - `/enable-indexing.md` (choose embeddings provider, set Qdrant URL, save)
   - `/update-memory-bank.md` (refresh short project summaries)
4. Try a quick task to validate mode switching (e.g., “write an E2E test for login”) — the **Orchestrator** should switch to **`qa-engineer`** automatically.

---

## 2) Directory layout (high‑level)


