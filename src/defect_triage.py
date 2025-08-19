from typing import List
import logging

class DefectTriager:
    """Defect triaging and root cause analysis."""
    def triage(self, defect_texts: List[str]) -> List[str]:
        results = []
        for t in defect_texts:
            severity = self.classify_severity(t)
            logging.info(f'Triaging defect: {t} | Severity: {severity}')
            results.append(f"Triaged ({severity}): {t}")
        return results

    def classify_severity(self, text: str) -> str:
        text_lower = text.lower()
        if any(word in text_lower for word in ["missing", "not recorded", "not updated"]):
            return "High"
        elif any(word in text_lower for word in ["inconsistent", "invalid", "duplicate", "unrecognized"]):
            return "Medium"
        else:
            return "Low"
