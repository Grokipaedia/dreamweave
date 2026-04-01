# dreamweave.py - Intelligent long-term memory with nightly "dreaming"
import json
import time
from datetime import datetime
from typing import Dict, List, Any

class Dreamweave:
    def __init__(self, memory_file: str = "dreamweave_memory.json"):
        self.memory_file = memory_file
        self.short_term: List[Dict] = []
        self.long_term: Dict[str, Dict] = {}
        self.load()

    def load(self):
        try:
            with open(self.memory_file, "r") as f:
                data = json.load(f)
                self.long_term = data.get("long_term", {})
        except FileNotFoundError:
            self.long_term = {}

    def save(self):
        data = {"long_term": self.long_term}
        with open(self.memory_file, "w") as f:
            json.dump(data, f, indent=2)

    def add(self, content: str, metadata: Dict = None):
        """Add interaction to short-term memory"""
        entry = {
            "id": len(self.short_term),
            "timestamp": datetime.now().isoformat(),
            "content": content,
            "metadata": metadata or {}
        }
        self.short_term.append(entry)
        print(f"📝 Dreamweave: Added to short-term memory ({len(self.short_term)} items)")

    def dream(self):
        """Nightly dreaming process - consolidate short-term into long-term memory"""
        if not self.short_term:
            print("😴 Dreamweave: Nothing to dream about tonight.")
            return

        print("🌙 Dreamweave dreaming started... consolidating memories")

        # Simple but effective consolidation
        summary = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "total_entries": len(self.short_term),
            "key_insights": [entry["content"][:150] + "..." for entry in self.short_term[:5]],
            "consolidated_at": datetime.now().isoformat()
        }

        dream_key = f"dream_{datetime.now().strftime('%Y%m%d_%H%M')}"
        self.long_term[dream_key] = summary

        # Clear short-term after dreaming
        self.short_term.clear()

        self.save()
        print(f"✅ Dreamweave complete. New long-term memory: {dream_key}")
        print(f"   Total long-term memories: {len(self.long_term)}")

    def recall(self, limit: int = 5) -> List[Dict]:
        """Recall recent long-term memories"""
        return list(self.long_term.values())[-limit:]

    def get_stats(self) -> Dict:
        return {
            "short_term_count": len(self.short_term),
            "long_term_count": len(self.long_term),
            "last_dream": list(self.long_term.keys())[-1] if self.long_term else "None"
        }


# Example usage
if __name__ == "__main__":
    memory = Dreamweave()

    print("🚀 Dreamweave Memory System Started\n")

    # Simulate daily interactions
    memory.add("User implemented IBA governance in Python agents")
    memory.add("Discussed Anthropic Claude Code leak architecture")
    memory.add("Built grk-html-2 visual demo for Intent-Bound Authorization")

    # Perform dreaming
    memory.dream()

    # Recall memories
    print("\n📚 Recalling long-term memories:")
    for mem in memory.recall():
        print(f"- {mem['date']}: {mem['key_insights'][0]}")

    print("\n📊 Stats:", memory.get_stats())
