Получение городов 🏢
========================================



API для получения списка акций по id

.. function:: Сделайте запрос методом `GET` по ссылке: /api/v1/handbook/city/


.. note::
   Данная запрос отправляет ответ список городов


**Успешный запрос:**

*Ответ*::
   
   - Status: 200 OK


*Дата данные*:

.. code-block:: json

    {
        "links": {
            "first": "http://127.0.0.1:8000/api/v1/handbook/city/?page_number=1",
            "last": "http://127.0.0.1:8000/api/v1/handbook/city/?page_number=1",
            "next": null,
            "prev": null
        },
        "data": [
            {
                "type": "City",
                "id": "1",
                "attributes": {
                    "name": "Шымкент"
                }
            },
            {
                "type": "City",
                "id": "2",
                "attributes": {
                    "name": "Алматы"
                }
            },
            {
                "type": "City",
                "id": "3",
                "attributes": {
                    "name": "Астана"
                }
            },
            {
                "type": "City",
                "id": "4",
                "attributes": {
                    "name": "Караганда"
                }
            },
            {
                "type": "City",
                "id": "5",
                "attributes": {
                    "name": "Тараз"
                }
            },
            {
                "type": "City",
                "id": "6",
                "attributes": {
                    "name": "Кызылорда"
                }
            },
            {
                "type": "City",
                "id": "7",
                "attributes": {
                    "name": "Жетысай"
                }
            },
            {
                "type": "City",
                "id": "8",
                "attributes": {
                    "name": "Жаркент"
                }
            },
            {
                "type": "City",
                "id": "9",
                "attributes": {
                    "name": "Каскелен"
                }
            },
            {
                "type": "City",
                "id": "10",
                "attributes": {
                    "name": "Шу"
                }
            },
            {
                "type": "City",
                "id": "11",
                "attributes": {
                    "name": "Казыгурт"
                }
            },
            {
                "type": "City",
                "id": "12",
                "attributes": {
                    "name": "Арысь"
                }
            },
            {
                "type": "City",
                "id": "13",
                "attributes": {
                    "name": "Карабулак"
                }
            },
            {
                "type": "City",
                "id": "14",
                "attributes": {
                    "name": "Аральск"
                }
            },
            {
                "type": "City",
                "id": "15",
                "attributes": {
                    "name": "Аксукент"
                }
            },
            {
                "type": "City",
                "id": "16",
                "attributes": {
                    "name": "Ленгер"
                }
            },
            {
                "type": "City",
                "id": "17",
                "attributes": {
                    "name": "Сарыкемер"
                }
            },
            {
                "type": "City",
                "id": "18",
                "attributes": {
                    "name": "Сарыагаш"
                }
            },
            {
                "type": "City",
                "id": "19",
                "attributes": {
                    "name": "Тулькубас"
                }
            },
            {
                "type": "City",
                "id": "20",
                "attributes": {
                    "name": "Туркестан"
                }
            },
            {
                "type": "City",
                "id": "21",
                "attributes": {
                    "name": "Узынагаш"
                }
            },
            {
                "type": "City",
                "id": "22",
                "attributes": {
                    "name": "Торетам"
                }
            },
            {
                "type": "City",
                "id": "23",
                "attributes": {
                    "name": "Шиели"
                }
            },
            {
                "type": "City",
                "id": "24",
                "attributes": {
                    "name": "Айтеке би"
                }
            },
            {
                "type": "City",
                "id": "25",
                "attributes": {
                    "name": "Отеген Батыр"
                }
            },
            {
                "type": "City",
                "id": "26",
                "attributes": {
                    "name": "Астана"
                }
            }
        ],
        "meta": {
            "pagination": {
                "page": 1,
                "pages": 1,
                "count": 26
            }
        }
    }
