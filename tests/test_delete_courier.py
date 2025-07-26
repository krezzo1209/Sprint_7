from utils.api_client import delete_courier

def test_delete_non_existing_courier():
    response = delete_courier(999999)
    assert response.status_code == 404
