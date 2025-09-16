# Жанна Дмитрова, 34-я когорта — Финальный проект. Инженер по тестированию плюс

import requests
import configuration
import data


# 1. Создаем заказ
def create_order():
    response = requests.post(f"{configuration.BASE_URL}{configuration.CREATE_ORDER}", json=data.order_payload)
    print(f"Ответ на создание заказа: {response.status_code}, {response.json()}")
    return response


# 2. Получаем трек-номер
def get_track_from_response(response):
    track = response.json().get("track")
    print(f"Заказ создан. Трек-номер: {track}")
    return track


# 3. Получаем заказ по треку
def get_order_by_track(track):
    response = requests.get(f"{configuration.BASE_URL}{configuration.GET_ORDER_BY_TRACK}", params={"t": track})
    print(f"Данные заказа по треку {track}: {response.json()}")
    return response


# 4. Проверяем статус-код
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