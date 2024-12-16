import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_recommendation(client):
    response = client.get('/recommend?user_id=1')
    assert response.status_code == 200
    data = response.get_json()
    assert "recommendations" in data
    assert len(data["recommendations"]) > 0