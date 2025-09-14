# Жанна Дмитрова, 34-я когорта — Финальный проект. Инженер по тестированию плюс

import requests

BASE_URL = "https://1609e9ba-12ab-4a9a-b88f-bc9849ddb1c5.serverhub.praktikum-services.ru"  # URL тестового стенда

# 1. Выполняем запрос на создание заказа
def create_order():
    payload = {
        "firstName": "Иван",
        "lastName": "Иванов",
        "address": "Москва, ул. Ленина, 1",
        "metroStation": 4,
        "phone": "+79992345556",
        "rentTime": 5,
        "deliveryDate": "2025-09-13",
        "comment": "Комментарий",
        "color": ["BLACK"]
    }
    response = requests.post(f"{BASE_URL}/api/v1/orders", json=payload)
    print(f"Ответ на создание заказа: {response.status_code}, {response.json()}")
    return response

# 2. Сохраняем номер трека заказа
def get_track_from_response(response):
    track = response.json().get("track")
    print(f"Заказ создан. Трек-номер: {track}")
    return track

# 3. Выполняем запрос на получение заказа по треку заказа
def get_order_by_track(track):
    response = requests.get(f"{BASE_URL}/api/v1/orders/track", params={"t": track})
    print(f"Данные заказа по треку {track}: {response.json()}")
    return response

# 4. Проверяем, что код ответа равен 200
def check_response_status(response):
    assert response.status_code == 200, f"Ожидали 200, а получили {response.status_code}"
    print("Код ответа 200 — заказ успешно найден")

# Тест
def test_create_and_get_order():
    create_response = create_order()
    track = get_track_from_response(create_response)
    get_response = get_order_by_track(track)
    check_response_status(get_response)
    print("Тест успешно выполнен")