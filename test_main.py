import pytest
from main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_math(client):
    test_number = 10
    response = client.get(f'/math/{test_number}')
    assert response.status_code == 200
    print(response.data.decode('utf-8'))

def test_second_page(client):
    response = client.get('/second')
    assert response.status_code == 200
    assert b'Second Page' in response.data
    print(response.data.decode('utf-8'))


