# dreamweave

> **Long-term "dreaming" memory for AI agents.**

---

## The Problem

AI agents forget. Every session starts cold. Context windows fill and compress. The agent that built deep understanding yesterday knows nothing today.

Dreamweave extracts the most valuable pattern from advanced agent memory systems: turning short-term interactions into coherent, self-improving long-term memory through background consolidation — the same way human memory consolidates during sleep.

---

## Features

- **Lightweight memory index** — no heavy databases required
- **Background dreaming process** — summarizes and connects memories between sessions
- **Simple store / retrieve / consolidate API**
- **Easy integration** with any local agent framework
- **IBA-ready** — memory writes governed by signed intent certificate

---

## Quick Start

```bash
git clone https://github.com/Grokipaedia/dreamweave.git
cd dreamweave
pip install -r requirements.txt
python example.py
```

---

## IBA Integration

Memory writes are agent actions. An agent that can write to long-term memory without a signed intent certificate can silently expand its own knowledge base, modify its own behavior patterns, or accumulate unauthorized information across sessions.

Dreamweave is designed to integrate with IBA Intent Bound Authorization — the cert declares what the agent is permitted to remember, not just what it is permitted to do.

```python
from dreamweave import DreamWeave
dw = DreamWeave(memory_path="./agent_memory")
# Store with IBA cert reference
dw.store(content="session insight", cert_ref="HUMAN-AUTH-2026-04-20")
# Retrieve with governance audit
memories = dw.retrieve(query="authorized context")
```

---

## Related Repos

| Repo | Track |
|------|-------|
| [iba-governor](https://github.com/Grokipaedia/iba-governor) | Core gate · any agent |
| [contextweave](https://github.com/Grokipaedia/contextweave) | Context collapse management |
| [iba-devstack-governor](https://github.com/Grokipaedia/iba-devstack-governor) | Dev stack governance |

---

## Patent & Standards Record

```
Patent:   GB2603013.0 (Pending) · UK IPO · Filed February 10, 2026
Conception: February 5, 2026 · OTS timestamp + witness email
WIPO DAS: Confirmed April 15, 2026 · Access Code C9A6
PCT:      150+ countries · Protected until August 2028
IETF:     draft-williams-intent-token-00 · CONFIRMED LIVE
          datatracker.ietf.org/doc/draft-williams-intent-token/
NIST:     13 filings · NIST-2025-0035
NCCoE:    10 filings · AI Agent Identity & Authorization
```

---

## Acquisition Enquiries

IBA Intent Bound Authorization is available for acquisition.

**Jeffrey Williams**
IBA@intentbound.com
IntentBound.com
Patent GB2603013.0 Pending · WIPO DAS C9A6 · IETF draft-williams-intent-token-00
