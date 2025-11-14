from typing import List

def calculate_risk_score(clauses: List[str]) -> dict:
    """
    Calculates a risk score for a contract based on the presence or absence of key clauses.
    This is a simple, rule-based approach for the MVP.
    """
    risk_score = 0
    reasons = []

    # Define keywords for risky and favorable clauses
    risk_keywords = {
        "unlimited liability": 20,
        "auto-renewal": 15,
        "termination for convenience": -10  # Favorable clause
    }

    for clause in clauses:
        for keyword, score in risk_keywords.items():
            if keyword in clause.lower():
                risk_score += score
                if score > 0:
                    reasons.append(f"Contains a clause with '{keyword}'")
                else:
                    reasons.append(f"Contains a favorable clause: '{keyword}'")

    # Determine risk level
    if risk_score > 30:
        risk_level = "High"
    elif risk_score > 10:
        risk_level = "Medium"
    else:
        risk_level = "Low"

    return {
        "risk_score": risk_score,
        "risk_level": risk_level,
        "reasons": reasons
    }
