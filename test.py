import requests

BASE_URL = "http://127.0.0.1:5000"


def test_btc_address():
    response = requests.get(f"{BASE_URL}/btc-address")
    return response.json()


def test_eth_address():
    response = requests.get(f"{BASE_URL}/eth-address")
    return response.json()


def test_ltc_address():
    response = requests.get(f"{BASE_URL}/ltc-address")
    return response.json()


def test_doge_address():
    response = requests.get(f"{BASE_URL}/doge-address")
    return response.json()


def test_addresses():
    response = requests.get(f"{BASE_URL}/addresses")
    return response.json()


def test_addresses_id():
    response = requests.get(f"{BASE_URL}/addresses/123")
    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["id"] == 123
