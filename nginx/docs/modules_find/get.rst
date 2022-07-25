Получение акции по id 🔟
========================================



API для получения списка акций по id

.. function:: Сделайте запрос методом `GET` по ссылке: /api/v1/sale/{id}


.. note::
   Данная запрос отправляет ответ акцию по введеному id


**Успешный запрос:**

*Ответ*::
   
   - Status: 200 OK


*Дата данные*:

.. code-block:: json

    {
        "data": {
            "type": "SaleGetController",
            "id": "42",
            "attributes": {
                "start_date": "2022-10-05T11:30:00+06:00",
                "end_date": "2022-10-05T11:30:00+06:00",
                "payment_method": "Картой",
                "is_use_of_bonuses": true,
                "is_manual_sale": true,
                "is_compensated": true,
                "prioritet": 10,
                "sale_type": "percenttype",
                "is_active": false,
                "author_id": 1
            },
            "relationships": {
                "is_intersects_models": {
                    "data": [
                        {
                            "id": 2,
                            "model": "percenttype"
                        },
                        {
                            "id": 3,
                            "model": "gifttype"
                        },
                        {
                            "id": 4,
                            "model": "specialpricetype"
                        }
                    ]
                },
                "content_object": {
                    "data": {
                        "id": 3,
                        "products": [
                            {
                                "id": 15,
                                "old_price": 1200,
                                "percent": 20,
                                "type_id": 3,
                                "product_id": 4000
                            },
                            {
                                "id": 16,
                                "old_price": 1200,
                                "percent": 20,
                                "type_id": 3,
                                "product_id": 4002
                            },
                            {
                                "id": 17,
                                "old_price": 1200,
                                "percent": 20,
                                "type_id": 3,
                                "product_id": 4003
                            },
                            {
                                "id": 18,
                                "old_price": 1200,
                                "percent": 20,
                                "type_id": 3,
                                "product_id": 4004
                            },
                            {
                                "id": 19,
                                "old_price": 1200,
                                "percent": 20,
                                "type_id": 3,
                                "product_id": 4005
                            },
                            {
                                "id": 20,
                                "old_price": 1200,
                                "percent": 20,
                                "type_id": 3,
                                "product_id": 4006
                            },
                            {
                                "id": 21,
                                "old_price": 1200,
                                "percent": 20,
                                "type_id": 3,
                                "product_id": 4007
                            }
                        ]
                    }
                }
            }
        }
    }

.. note::
    Поле **content_object** описывает данные акции которые были созданы для товара
    
    Для каждой акции генерируется свой **content_object**




.. warning::
   **Запрос где не найдена id:**

*Ответ*::
   
   - Status: 500 Internal Server Error


*Дата данные*:

.. code-block:: json

    {
        "errors": "No Sale matches the given query."
    }