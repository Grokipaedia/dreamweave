# dreamweave

**Intelligent long-term memory with nightly "dreaming" for local AI agents**

Inspired by the advanced memory consolidation system from the Anthropic Claude Code leak.

While most forks focus on raw power and tools, Dreamweave extracts and open-sources the most valuable hidden piece: turning short-term interactions into coherent, self-improving long-term memory.

## Features
- Lightweight memory index (no heavy databases needed)
- Background "dreaming" process that summarizes and connects memories
- Simple store / retrieve / consolidate API
- Easy to integrate with claw-code, Ollama, LangChain, or any local agent
- Ready for IBA governance (see [iba-claw-starter](https://github.com/Grokipaedia/iba-claw-starter))

## Why it matters
Local agents usually forget quickly. Dreamweave gives them persistent, evolving memory — the same technique that made Claude Code feel remarkably capable.

## Quick Start
```bash
git clone https://github.com/Grokipaedia/dreamweave.git
cd dreamweave
pip install -r requirements.txt
python example.py
