import json
from typing import Dict

def analyze_risk(entities: Dict[str, list]) -> Dict[str, str]:
    """Analyzes risk based on extracted entities."""
    risk_scores = {}
    sanctions_list = {"Elon Musk": "Low", "Tesla": "Medium", "California": "Low"}  # Example data
    
    for category, values in entities.items():
        for value in values:
            clean_value = value.replace(" (Verified)", "")  # Normalize entity names
            risk_scores[value] = sanctions_list.get(clean_value, "Unknown")
    
    return risk_scores

if __name__ == "__main__":
    extracted_entities = {
        "PERSON": ["Elon Musk (Verified)"],
        "ORG": ["Tesla (Verified)"],
        "GPE": ["California (Verified)"]
    }
    print(json.dumps(analyze_risk(extracted_entities), indent=2))
