import re

def segment_into_clauses(text: str) -> list[str]:
    """
    Segments a contract's text into individual clauses.
    This is a rule-based approach for the MVP.
    """
    # This regex looks for common clause starters like "1. ", "a. ", or "Termination."
    # It's a simplistic approach and can be improved with more sophisticated NLP.
    clause_starters = r"\n\s*(\d+\.\s*|[a-zA-Z]\.\s*|[A-Z][a-zA-Z]+\s*\.)"

    # Split the text based on the clause starters
    clauses = re.split(clause_starters, text)

    # Filter out empty strings and whitespace
    clauses = [clause.strip() for clause in clauses if clause.strip()]

    return clauses
