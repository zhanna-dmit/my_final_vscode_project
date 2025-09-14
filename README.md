# Работа с базой данных

# Первый запрос:

SELECT c."login", COUNT(o."courierId") AS active_orders
FROM "Orders" o
JOIN "Couriers" c ON o."courierId" = c."id"
WHERE o."inDelivery" = TRUE
GROUP BY c."login";

# Второй запрос:

SELECT 
    o."track",
    CASE
        WHEN o."finished" = TRUE THEN 2
        WHEN o."cancelled" = TRUE THEN -1
        WHEN o."inDelivery" = TRUE THEN 1
        ELSE 0
    END AS status
FROM "Orders" o;

# Автотест
# Тест на проверку получения данных заказа по треку заказа
- Для запуска тестов должны быть установлены пакеты pytest и requests
- Запуск автотестов выполняется командой pytest -s test_orders.py

# В проекте реализованы:
- функция создания заказа create_order;
- функция сохранения трека номера заказа get_track_from_response;
- функция получения данных заказа по треку get_order_by_track;
- проверка, что вернулся код 200 check_response_status.