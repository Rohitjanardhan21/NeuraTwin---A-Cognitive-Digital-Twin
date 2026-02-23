"""
👥 PARALLEL SELVES GENERATOR - Alternate persona simulator
Generates alternate versions with different priorities
"""

from typing import Dict, List


class ParallelSelvesGenerator:
    """Generate alternate persona versions"""
    
    PERSONAS = {
        "researcher": {
            "priorities": ["novelty", "theoretical depth", "publications", "rigor"],
            "risk_tolerance": "high",
            "time_horizon": "long-term",
            "success_metrics": ["citations", "breakthroughs", "understanding"],
            "avoids": ["shortcuts", "pragmatic compromises", "market pressure"]
        },
        "founder": {
            "priorities": ["speed", "market fit", "user value", "iteration"],
            "risk_tolerance": "very high",
            "time_horizon": "short-term",
            "success_metrics": ["users", "revenue", "growth", "product-market fit"],
            "avoids": ["perfectionism", "over-engineering", "analysis paralysis"]
        },
        "engineer": {
            "priorities": ["reliability", "scale", "maintainability", "efficiency"],
            "risk_tolerance": "low",
            "time_horizon": "medium-term",
            "success_metrics": ["uptime", "performance", "code quality", "team velocity"],
            "avoids": ["technical debt", "untested code", "complexity"]
        }
    }
    
    def __init__(self, llm_client):
        self.llm = llm_client
    
    def generate_parallel_responses(
        self,
        problem: str,
        baseline_personality: Dict,
        patterns: Dict
    ):
        """Generate responses from three parallel selves"""
        
        personality_summary = self._summarize_personality(baseline_personality, patterns)
        
        prompt = f"""You are simulating three parallel versions of the same person with different career paths.

BASELINE PERSONALITY:
{personality_summary}

PROBLEM TO SOLVE:
{problem}

Generate detailed responses from three versions:

═══════════════════════════════════════
🔬 RESEARCH-FOCUSED VERSION
═══════════════════════════════════════
Priorities: {', '.join(self.PERSONAS['researcher']['priorities'])}
Risk Tolerance: {self.PERSONAS['researcher']['risk_tolerance']}
Time Horizon: {self.PERSONAS['researcher']['time_horizon']}

APPROACH:
[Detailed approach from research perspective]

REASONING:
[Why this approach, what tradeoffs]

SUCCESS LOOKS LIKE:
[How they measure success]

═══════════════════════════════════════
🚀 STARTUP FOUNDER VERSION
═══════════════════════════════════════
Priorities: {', '.join(self.PERSONAS['founder']['priorities'])}
Risk Tolerance: {self.PERSONAS['founder']['risk_tolerance']}
Time Horizon: {self.PERSONAS['founder']['time_horizon']}

APPROACH:
[Detailed approach from founder perspective]

REASONING:
[Why this approach, what tradeoffs]

SUCCESS LOOKS LIKE:
[How they measure success]

═══════════════════════════════════════
⚙️ INDUSTRY ENGINEER VERSION
═══════════════════════════════════════
Priorities: {', '.join(self.PERSONAS['engineer']['priorities'])}
Risk Tolerance: {self.PERSONAS['engineer']['risk_tolerance']}
Time Horizon: {self.PERSONAS['engineer']['time_horizon']}

APPROACH:
[Detailed approach from engineer perspective]

REASONING:
[Why this approach, what tradeoffs]

SUCCESS LOOKS LIKE:
[How they measure success]

═══════════════════════════════════════
🔍 COMPARATIVE ANALYSIS
═══════════════════════════════════════
Key Differences:
- Decision logic
- Risk assessment
- Time allocation
- Resource priorities
- Definition of "done"

Which version is closest to baseline personality?
What does this reveal about current trajectory?"""

        return {
            "prompt": prompt,
            "personas": self.PERSONAS,
            "baseline": personality_summary
        }
    
    def _summarize_personality(self, baseline: Dict, patterns: Dict):
        """Summarize baseline personality from patterns"""
        summary = []
        
        if "preferences" in patterns:
            prefs = patterns["preferences"]
            top_3 = sorted(prefs.items(), key=lambda x: x[1], reverse=True)[:3]
            summary.append(f"Core values: {', '.join([k for k, v in top_3])}")
        
        if "decision_speed" in patterns:
            rate = patterns["decision_speed"].get("decisions_per_month", 0)
            if rate > 10:
                summary.append("Decision style: Fast-paced, iterative")
            elif rate > 5:
                summary.append("Decision style: Balanced, thoughtful")
            else:
                summary.append("Decision style: Deliberate, careful")
        
        if "outcome_patterns" in patterns:
            outcomes = patterns["outcome_patterns"]
            success_rate = outcomes.get("success", 0) / max(sum(outcomes.values()), 1)
            if success_rate > 0.7:
                summary.append("Track record: High success rate")
            elif success_rate > 0.4:
                summary.append("Track record: Mixed results, learning-focused")
            else:
                summary.append("Track record: Experimental, high-risk tolerance")
        
        return "\n".join(summary) if summary else "Baseline personality not yet established"
