from services.nlp.risk_scoring import calculate_risk_score

def test_risk_scoring_high_risk():
    """
    Test the risk scoring logic with a contract containing high-risk clauses.
    """
    clauses = [
        "This contract imposes unlimited liability on the counterparty.",
        "The terms include an auto-renewal clause without a notice period."
    ]
    result = calculate_risk_score(clauses)
    assert result["risk_level"] == "High"
    assert result["risk_score"] > 30

def test_risk_scoring_low_risk():
    """
    Test the risk scoring logic with a contract containing favorable clauses.
    """
    clauses = [
        "This agreement may be terminated for convenience by either party.",
        "The vendor's liability is limited to the fees paid in the preceding year."
    ]
    result = calculate_risk_score(clauses)
    assert result["risk_level"] == "Low"
    assert result["risk_score"] < 10
