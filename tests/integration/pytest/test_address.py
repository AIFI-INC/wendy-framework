from fastapi.testclient import TestClient
from wendy import app  # The app we want to test
from wendy.utilities import MSG_200_OK

client = TestClient(app)


def test_list():
    response = client.get("/v1/addresses")
    assert response.status_code == 200
