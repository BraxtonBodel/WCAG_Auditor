from fastapi.testclient import TestClient
from accessibility_ai.app.main import app, get_db
from unittest.mock import MagicMock

client = TestClient(app)

def test_guidelines_endpoint(mocker):
    """
    Verifica que el endpoint GET /guidelines/ devuelva una lista y status 200.
    """

    mock_db = MagicMock()

    mock_guidelines = [
        MagicMock(id=1,success_criterion="1.1.1", description="Texto alternativo", level="A"),
        MagicMock(id=2,success_criterion="1.2.1", description="Solo audio", level="A")
    ]

    mock_db.query.return_value.all.return_value = mock_guidelines
    
    def override_get_db():
        try:
            yield mock_db
        finally:
            pass
    
    app.dependency_overrides[get_db] = override_get_db

    response = client.get("/guidelines/")

    app.dependency_overrides = {}

    assert response.status_code == 200

    data = response.json()
    assert len(data) == 2
    assert data[0]["success_criterion"] == "1.1.1"

    print("\n Test de Integración (Mocking DB) -> PASÓ")
    