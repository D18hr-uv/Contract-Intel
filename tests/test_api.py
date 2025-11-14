from fastapi.testclient import TestClient
from services.api.main import app

client = TestClient(app)

def test_health_check():
    """
    Test the /health endpoint to ensure the API is running.
    """
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
