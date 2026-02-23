"""
🔍 PATTERN ANALYZER - Detect cognitive patterns
Identifies recurring themes, preferences, and tendencies
"""

import json
import os
from collections import Counter, defaultdict
from typing import List, Dict
from datetime import datetime, timedelta


class PatternAnalyzer:
    """Analyze cognitive patterns from decision history"""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        self.patterns_file = os.path.join(data_dir, "patterns.json")
        self.patterns = self._load_patterns()
    
    def analyze_decisions(self, decisions: List[Dict]):
        """Analyze patterns from decision history"""
        patterns = {
            "preferences": self._extract_preferences(decisions),
            "recurring_themes": self._find_recurring_themes(decisions),
            "decision_speed": self._analyze_decision_speed(decisions),
            "constraint_patterns": self._analyze_constraints(decisions),
            "outcome_patterns": self._analyze_outcomes(decisions),
            "evolution": self._track_evolution(decisions)
        }
        
        self.patterns = patterns
        self._save_patterns()
        
        return patterns
    
    def _extract_preferences(self, decisions: List[Dict]):
        """Extract decision preferences"""
        preferences = defaultdict(int)
        
        for dec in decisions:
            reason = dec.get("reason", "").lower()
            
            # Look for preference keywords
            if "efficient" in reason or "performance" in reason:
                preferences["efficiency"] += 1
            if "simple" in reason or "minimal" in reason:
                preferences["simplicity"] += 1
            if "scalable" in reason or "scale" in reason:
                preferences["scalability"] += 1
            if "fast" in reason or "quick" in reason:
                preferences["speed"] += 1
            if "reliable" in reason or "stable" in reason:
                preferences["reliability"] += 1
            if "novel" in reason or "innovative" in reason:
                preferences["innovation"] += 1
        
        return dict(preferences)
    
    def _find_recurring_themes(self, decisions: List[Dict]):
        """Find recurring themes in decisions"""
        all_tags = []
        for dec in decisions:
            all_tags.extend(dec.get("tags", []))
        
        tag_counts = Counter(all_tags)
        return dict(tag_counts.most_common(10))
    
    def _analyze_decision_speed(self, decisions: List[Dict]):
        """Analyze how quickly decisions are made"""
        # This is simplified - in reality you'd track decision start/end times
        return {
            "total_decisions": len(decisions),
            "decisions_per_month": self._calculate_decision_rate(decisions)
        }
    
    def _analyze_constraints(self, decisions: List[Dict]):
        """Analyze common constraints"""
        constraint_types = Counter()
        
        for dec in decisions:
            constraints = dec.get("constraints", {})
            for key in constraints.keys():
                constraint_types[key] += 1
        
        return dict(constraint_types)
    
    def _analyze_outcomes(self, decisions: List[Dict]):
        """Analyze decision outcomes"""
        outcomes = {"success": 0, "failure": 0, "unknown": 0}
        
        for dec in decisions:
            outcome = dec.get("outcome", "").lower()
            if outcome in ["success", "successful", "good"]:
                outcomes["success"] += 1
            elif outcome in ["failure", "failed", "bad"]:
                outcomes["failure"] += 1
            else:
                outcomes["unknown"] += 1
        
        return outcomes
    
    def _track_evolution(self, decisions: List[Dict]):
        """Track how decision patterns evolve over time"""
        if len(decisions) < 2:
            return {"status": "insufficient_data"}
        
        sorted_decisions = sorted(decisions, key=lambda x: x["timestamp"])
        midpoint = len(sorted_decisions) // 2
        
        early = sorted_decisions[:midpoint]
        recent = sorted_decisions[midpoint:]
        
        return {
            "early_preferences": self._extract_preferences(early),
            "recent_preferences": self._extract_preferences(recent),
            "shift_detected": self._detect_preference_shift(early, recent)
        }
    
    def _detect_preference_shift(self, early: List[Dict], recent: List[Dict]):
        """Detect if preferences have shifted"""
        early_prefs = self._extract_preferences(early)
        recent_prefs = self._extract_preferences(recent)
        
        shifts = []
        all_keys = set(early_prefs.keys()) | set(recent_prefs.keys())
        
        for key in all_keys:
            early_val = early_prefs.get(key, 0)
            recent_val = recent_prefs.get(key, 0)
            if abs(recent_val - early_val) > 2:
                shifts.append({
                    "preference": key,
                    "direction": "increasing" if recent_val > early_val else "decreasing"
                })
        
        return shifts
    
    def _calculate_decision_rate(self, decisions: List[Dict]):
        """Calculate decisions per month"""
        if not decisions:
            return 0
        
        sorted_decisions = sorted(decisions, key=lambda x: x["timestamp"])
        first = datetime.fromisoformat(sorted_decisions[0]["timestamp"])
        last = datetime.fromisoformat(sorted_decisions[-1]["timestamp"])
        
        days = (last - first).days
        if days == 0:
            return len(decisions)
        
        return len(decisions) / (days / 30)
    
    def _load_patterns(self):
        """Load patterns from disk"""
        if os.path.exists(self.patterns_file):
            with open(self.patterns_file, 'r') as f:
                return json.load(f)
        return {}
    
    def _save_patterns(self):
        """Save patterns to disk"""
        os.makedirs(self.data_dir, exist_ok=True)
        with open(self.patterns_file, 'w') as f:
            json.dump(self.patterns, f, indent=2)
