import requests

BASE_URL = "http://localhost:8000"


def test_btc_address():
    response = requests.get(f"{BASE_URL}/btc-address")
    assert response.status_code == 200
    assert "address" in response.json()


def test_eth_address():
    response = requests.get(f"{BASE_URL}/eth-address")
    assert response.status_code == 200
    assert "address" in response.json()


def test_ltc_address():
    response = requests.get(f"{BASE_URL}/ltc-address")
    assert response.status_code == 200
    assert "address" in response.json()


def test_doge_address():
    response = requests.get(f"{BASE_URL}/doge-address")
    assert response.status_code == 200
    assert "address" in response.json()


def test_addresses():
    response = requests.get(f"{BASE_URL}/addresses")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_addresses_id():
    response = requests.get(f"{BASE_URL}/addresses/123")
    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["id"] == 123
