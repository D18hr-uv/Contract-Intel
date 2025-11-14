from .celery_app import celery_app
import fitz  # PyMuPDF
import os
from services.nlp.clause_segmentation import segment_into_clauses
from services.nlp.risk_scoring import calculate_risk_score

@celery_app.task
def process_document(file_path: str):
    """
    Celery task to process an uploaded document.
    This task extracts text, segments it into clauses, and calculates a risk score.
    """
    try:
        # Verify the file exists
        if not os.path.exists(file_path):
            return {"status": "error", "message": f"File not found at {file_path}"}

        # Open the PDF document
        document = fitz.open(file_path)

        # Extract text from each page
        text = ""
        for page_num in range(len(document)):
            page = document.load_page(page_num)
            text += page.get_text()

        # Segment the text into clauses
        clauses = segment_into_clauses(text)

        # Calculate the risk score
        risk_analysis = calculate_risk_score(clauses)

        return {"status": "success", "risk_analysis": risk_analysis}

    except Exception as e:
        return {"status": "error", "message": str(e)}
