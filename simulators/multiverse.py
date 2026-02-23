"""
🌌 MULTIVERSE SIMULATOR - Alternate timeline generator
Simulates "what if" scenarios based on past decisions
"""

from typing import Dict, List
import json


class MultiverseSimulator:
    """Simulate alternate decision timelines"""
    
    def __init__(self, llm_client):
        self.llm = llm_client
    
    def simulate_timeline(
        self,
        current_path: str,
        alternative: str,
        decisions: List[Dict],
        patterns: Dict
    ):
        """Simulate two parallel timelines"""
        
        # Build context from past decisions
        decision_context = self._build_decision_context(decisions)
        pattern_summary = self._summarize_patterns(patterns)
        
        prompt = f"""You are simulating alternate timelines based on past decision patterns.

CURRENT PATH: {current_path}
ALTERNATIVE: {alternative}

PAST DECISION PATTERNS:
{pattern_summary}

DECISION HISTORY:
{decision_context}

Simulate two detailed timelines:

TIMELINE A (Current Path):
- Immediate consequences
- 3-month outlook
- 6-month outlook
- Technical debt implications
- Alignment with past patterns

TIMELINE B (Alternative):
- Immediate consequences
- 3-month outlook
- 6-month outlook
- Technical debt implications
- Deviation from past patterns

COMPARISON:
- Performance implications
- Scalability differences
- Complexity trade-offs
- Long-term sustainability
- Which aligns better with established decision patterns

Be specific and analytical. Reference past decisions when relevant."""

        return {
            "prompt": prompt,
            "current_path": current_path,
            "alternative": alternative,
            "context": {
                "decisions": decision_context,
                "patterns": pattern_summary
            }
        }
    
    def _build_decision_context(self, decisions: List[Dict], limit: int = 10):
        """Build context from recent decisions"""
        recent = sorted(decisions, key=lambda x: x["timestamp"], reverse=True)[:limit]
        
        context = []
        for dec in recent:
            context.append(
                f"• {dec['decision']}\n"
                f"  Reason: {dec['reason']}\n"
                f"  Outcome: {dec.get('outcome', 'Unknown')}"
            )
        
        return "\n\n".join(context)
    
    def _summarize_patterns(self, patterns: Dict):
        """Summarize cognitive patterns"""
        summary = []
        
        if "preferences" in patterns:
            prefs = patterns["preferences"]
            top_prefs = sorted(prefs.items(), key=lambda x: x[1], reverse=True)[:3]
            summary.append("Top Preferences: " + ", ".join([f"{k} ({v})" for k, v in top_prefs]))
        
        if "recurring_themes" in patterns:
            themes = patterns["recurring_themes"]
            summary.append("Recurring Themes: " + ", ".join(list(themes.keys())[:5]))
        
        if "evolution" in patterns and "shift_detected" in patterns["evolution"]:
            shifts = patterns["evolution"]["shift_detected"]
            if shifts:
                summary.append("Recent Shifts: " + ", ".join([f"{s['preference']} {s['direction']}" for s in shifts]))
        
        return "\n".join(summary)
