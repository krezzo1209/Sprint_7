from utils.api_client import login_courier

def test_login_success(new_courier):
    courier, _ = new_courier
    response = login_courier({"login": courier["login"], "password": courier["password"]})
    assert response.status_code == 200
    assert "id" in response.json()
