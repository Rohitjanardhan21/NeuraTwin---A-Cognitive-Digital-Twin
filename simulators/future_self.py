"""
🔮 FUTURE SELF PREDICTOR - Predict cognitive evolution
Predicts future specialization and learning direction
"""

from typing import Dict, List
from datetime import datetime, timedelta
from collections import Counter


class FutureSelfPredictor:
    """Predict future cognitive evolution"""
    
    def __init__(self, llm_client):
        self.llm = llm_client
    
    def predict_trajectory(
        self,
        decisions: List[Dict],
        patterns: Dict,
        memories: List[Dict] = None
    ):
        """Predict future trajectory based on trends"""
        
        # Analyze recent activity
        recent_activity = self._analyze_recent_activity(decisions)
        learning_trends = self._extract_learning_trends(decisions, memories)
        skill_gaps = self._identify_skill_gaps(patterns)
        
        prompt = f"""Based on cognitive patterns and recent activity, predict future trajectory.

RECENT ACTIVITY (Last 3 months):
{recent_activity}

LEARNING TRENDS:
{learning_trends}

IDENTIFIED SKILL GAPS:
{skill_gaps}

Predict:

1. LIKELY SPECIALIZATION (6-12 months):
   - Primary technical focus
   - Secondary interests
   - Confidence level: [Low/Medium/High]

2. TECHNOLOGY GRAVITATIONAL PULL:
   - Technologies being drawn toward
   - Why these align with past patterns
   - Potential blind spots

3. SKILL PRIORITIES:
   - Critical skills to develop
   - Skills being naturally acquired
   - Skills being avoided (and why)

4. CAREER TRAJECTORY:
   - Most likely path
   - Alternative paths
   - Inflection points to watch for

5. COGNITIVE EVOLUTION:
   - How thinking patterns are shifting
   - Emerging biases or strengths
   - Recommended interventions

Be specific and evidence-based. Reference concrete patterns."""

        return {
            "prompt": prompt,
            "analysis": {
                "recent_activity": recent_activity,
                "trends": learning_trends,
                "gaps": skill_gaps
            }
        }
    
    def _analyze_recent_activity(self, decisions: List[Dict], days: int = 90):
        """Analyze recent decision activity"""
        cutoff = datetime.now() - timedelta(days=days)
        recent = [d for d in decisions if datetime.fromisoformat(d["timestamp"]) > cutoff]
        
        if not recent:
            return "No recent activity"
        
        tags = []
        for dec in recent:
            tags.extend(dec.get("tags", []))
        
        tag_counts = Counter(tags).most_common(5)
        
        activity = [
            f"Total decisions: {len(recent)}",
            f"Top areas: {', '.join([f'{tag} ({count})' for tag, count in tag_counts])}"
        ]
        
        return "\n".join(activity)
    
    def _extract_learning_trends(self, decisions: List[Dict], memories: List[Dict] = None):
        """Extract learning trends from decisions and memories"""
        trends = []
        
        # Analyze decision complexity over time
        sorted_decisions = sorted(decisions, key=lambda x: x["timestamp"])
        if len(sorted_decisions) >= 4:
            early = sorted_decisions[:len(sorted_decisions)//2]
            recent = sorted_decisions[len(sorted_decisions)//2:]
            
            early_complexity = sum(len(d.get("constraints", {})) for d in early) / len(early)
            recent_complexity = sum(len(d.get("constraints", {})) for d in recent) / len(recent)
            
            if recent_complexity > early_complexity * 1.3:
                trends.append("Increasing decision complexity - handling more constraints")
            elif recent_complexity < early_complexity * 0.7:
                trends.append("Simplifying decisions - focusing on core factors")
        
        # Analyze tag evolution
        if len(sorted_decisions) >= 4:
            early_tags = set()
            recent_tags = set()
            
            for d in sorted_decisions[:len(sorted_decisions)//2]:
                early_tags.update(d.get("tags", []))
            
            for d in sorted_decisions[len(sorted_decisions)//2:]:
                recent_tags.update(d.get("tags", []))
            
            new_areas = recent_tags - early_tags
            if new_areas:
                trends.append(f"Exploring new areas: {', '.join(list(new_areas)[:3])}")
        
        return "\n".join(trends) if trends else "Stable focus areas"
    
    def _identify_skill_gaps(self, patterns: Dict):
        """Identify potential skill gaps from patterns"""
        gaps = []
        
        preferences = patterns.get("preferences", {})
        
        # Check for imbalanced preferences
        if preferences.get("speed", 0) > preferences.get("reliability", 0) * 2:
            gaps.append("Reliability/testing practices may be underdeveloped")
        
        if preferences.get("innovation", 0) > preferences.get("scalability", 0) * 2:
            gaps.append("Production scalability considerations may need attention")
        
        if preferences.get("efficiency", 0) > preferences.get("simplicity", 0) * 2:
            gaps.append("May be over-optimizing at expense of maintainability")
        
        return "\n".join(gaps) if gaps else "No obvious skill gaps detected"
