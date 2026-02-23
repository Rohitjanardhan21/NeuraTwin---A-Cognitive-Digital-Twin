"""
⚠️ BIAS DETECTOR - Identify cognitive biases
Detects patterns that might indicate cognitive biases
"""

from typing import List, Dict
from collections import Counter


class BiasDetector:
    """Detect cognitive biases in decision patterns"""
    
    BIAS_RULES = {
        "overengineering": {
            "keywords": ["complex", "sophisticated", "advanced", "comprehensive"],
            "threshold": 3,
            "description": "Tendency to choose complex solutions over simple ones"
        },
        "tool_switching": {
            "keywords": ["new tool", "switch to", "migrate to", "try"],
            "threshold": 4,
            "description": "Frequent switching between tools without full evaluation"
        },
        "premature_optimization": {
            "keywords": ["optimize", "performance", "faster", "efficient"],
            "threshold": 5,
            "description": "Optimizing before establishing baseline functionality"
        },
        "recency_bias": {
            "keywords": ["latest", "new", "recent", "modern"],
            "threshold": 4,
            "description": "Overvaluing recent information or trends"
        },
        "sunk_cost": {
            "keywords": ["already invested", "spent time", "too late", "committed"],
            "threshold": 2,
            "description": "Continuing with decisions due to past investment"
        },
        "confirmation_bias": {
            "keywords": ["as expected", "proves", "confirms", "validates"],
            "threshold": 3,
            "description": "Seeking information that confirms existing beliefs"
        }
    }
    
    def detect_biases(self, decisions: List[Dict], patterns: Dict):
        """Detect potential cognitive biases"""
        biases_found = []
        
        # Rule-based detection
        for bias_name, rule in self.BIAS_RULES.items():
            score = self._calculate_bias_score(decisions, rule)
            if score >= rule["threshold"]:
                biases_found.append({
                    "bias": bias_name,
                    "score": score,
                    "description": rule["description"],
                    "evidence": self._find_evidence(decisions, rule["keywords"])
                })
        
        # Pattern-based detection
        pattern_biases = self._detect_pattern_biases(patterns)
        biases_found.extend(pattern_biases)
        
        return biases_found
    
    def _calculate_bias_score(self, decisions: List[Dict], rule: Dict):
        """Calculate bias score based on keyword frequency"""
        score = 0
        keywords = rule["keywords"]
        
        for dec in decisions:
            text = f"{dec.get('decision', '')} {dec.get('reason', '')}".lower()
            for keyword in keywords:
                if keyword in text:
                    score += 1
        
        return score
    
    def _find_evidence(self, decisions: List[Dict], keywords: List[str]):
        """Find specific examples of bias"""
        evidence = []
        
        for dec in decisions:
            text = f"{dec.get('decision', '')} {dec.get('reason', '')}".lower()
            for keyword in keywords:
                if keyword in text:
                    evidence.append({
                        "decision": dec.get("decision", ""),
                        "reason": dec.get("reason", ""),
                        "timestamp": dec.get("timestamp", "")
                    })
                    break
            
            if len(evidence) >= 3:
                break
        
        return evidence
    
    def _detect_pattern_biases(self, patterns: Dict):
        """Detect biases from pattern analysis"""
        biases = []
        
        # Check for extreme preferences
        preferences = patterns.get("preferences", {})
        if preferences:
            max_pref = max(preferences.values()) if preferences.values() else 0
            total = sum(preferences.values())
            
            if total > 0 and max_pref / total > 0.6:
                dominant = max(preferences, key=preferences.get)
                biases.append({
                    "bias": "single_dimension_thinking",
                    "score": max_pref / total,
                    "description": f"Over-focusing on {dominant} at expense of other factors",
                    "evidence": [{"preference": dominant, "frequency": max_pref}]
                })
        
        # Check outcome patterns
        outcomes = patterns.get("outcome_patterns", {})
        unknown = outcomes.get("unknown", 0)
        total_outcomes = sum(outcomes.values())
        
        if total_outcomes > 0 and unknown / total_outcomes > 0.5:
            biases.append({
                "bias": "outcome_avoidance",
                "score": unknown / total_outcomes,
                "description": "Not tracking or evaluating decision outcomes",
                "evidence": [{"unknown_outcomes": unknown, "total": total_outcomes}]
            })
        
        return biases
