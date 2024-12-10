import app
from flask.testing import FlaskClient

def test_hello_world():
    client = app.app.test_client()  # Create a test client
    response = client.get('/api/hello')  # Test the /api/hello endpoint
    assert response.status_code == 200
    assert response.json['message'] == "Hello, world!"
