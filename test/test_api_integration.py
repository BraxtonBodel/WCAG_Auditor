from fastapi.testclient import TestClient
from accessibility_ai.app.main import app
from unittest.mock import MagicMock

client = TestClient(app)

def test_guidelines_endpoint(mocker):
    """
    Verifica que el endpoint GET /guidelines/ devuelva una lista y status 200.
    """

    mock_guidelines = [
        MagicMock(success_criterion="1.1.1", description="Texto alternativo", level="A"),
        MagicMock(success_criterion="1.2.1", description="Solo audio", level="A")
    ]

    response = client.get("/guidelines/")

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0