import requests

BASE_URL = "https://qa-scooter.praktikum-services.ru"

def create_courier(data):
    return requests.post(f"{BASE_URL}/api/v1/courier", json=data)

def login_courier(data):
    return requests.post(f"{BASE_URL}/api/v1/courier/login", json=data)

def delete_courier(courier_id):
    return requests.delete(f"{BASE_URL}/api/v1/courier/{courier_id}")

def create_order(data):
    return requests.post(f"{BASE_URL}/api/v1/orders", json=data)

def get_orders():
    return requests.get(f"{BASE_URL}/api/v1/orders")

def accept_order(order_id, courier_id):
    return requests.put(f"{BASE_URL}/api/v1/orders/accept", params={"orderId": order_id, "courierId": courier_id})

def get_order_by_track(track):
    return requests.get(f"{BASE_URL}/api/v1/orders/track", params={"t": track})
