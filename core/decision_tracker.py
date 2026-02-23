"""
📊 DECISION TRACKER - Timeline of choices
Stores decisions with context, constraints, and outcomes
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Optional


class DecisionTracker:
    """Track decisions with full context for timeline simulation"""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        self.decisions_file = os.path.join(data_dir, "decisions.json")
        self.decisions = self._load_decisions()
    
    def add_decision(
        self,
        decision: str,
        reason: str,
        alternatives: List[str] = None,
        constraints: Dict = None,
        outcome: str = None,
        tags: List[str] = None
    ):
        """Record a decision with full context"""
        decision_entry = {
            "id": f"dec_{len(self.decisions)}",
            "timestamp": datetime.now().isoformat(),
            "decision": decision,
            "reason": reason,
            "alternatives": alternatives or [],
            "constraints": constraints or {},
            "outcome": outcome,
            "tags": tags or [],
            "context_snapshot": self._capture_context()
        }
        
        self.decisions.append(decision_entry)
        self._save_decisions()
        
        return decision_entry["id"]
    
    def update_outcome(self, decision_id: str, outcome: str):
        """Update the outcome of a past decision"""
        for dec in self.decisions:
            if dec["id"] == decision_id:
                dec["outcome"] = outcome
                dec["outcome_timestamp"] = datetime.now().isoformat()
                break
        
        self._save_decisions()
    
    def get_recent_decisions(self, n: int = 10):
        """Get most recent decisions"""
        return sorted(self.decisions, key=lambda x: x["timestamp"], reverse=True)[:n]
    
    def get_decisions_by_tag(self, tag: str):
        """Get all decisions with a specific tag"""
        return [d for d in self.decisions if tag in d.get("tags", [])]
    
    def get_decision_timeline(self):
        """Get chronological decision timeline"""
        return sorted(self.decisions, key=lambda x: x["timestamp"])
    
    def find_similar_decisions(self, current_decision: str):
        """Find past decisions similar to current one (simple keyword matching)"""
        keywords = set(current_decision.lower().split())
        similar = []
        
        for dec in self.decisions:
            dec_keywords = set(dec["decision"].lower().split())
            overlap = len(keywords & dec_keywords)
            if overlap > 2:
                similar.append((dec, overlap))
        
        return sorted(similar, key=lambda x: x[1], reverse=True)
    
    def _capture_context(self):
        """Capture current context snapshot"""
        return {
            "timestamp": datetime.now().isoformat(),
            "decision_count": len(self.decisions)
        }
    
    def _load_decisions(self):
        """Load decisions from disk"""
        if os.path.exists(self.decisions_file):
            with open(self.decisions_file, 'r') as f:
                return json.load(f)
        return []
    
    def _save_decisions(self):
        """Save decisions to disk"""
        os.makedirs(self.data_dir, exist_ok=True)
        with open(self.decisions_file, 'w') as f:
            json.dump(self.decisions, f, indent=2)
