Получение списка продуктов
========================================



API для получения списка продуктов

.. function:: Сделайте запрос методом `GET` по ссылке: /api/v1/sale/30/products?page[number]=3&page[size]=3

.. note::
   Данная запрос отправляет ответ со списками продуктов

   Значение **page[number]** указывает на **id** страницы, 
   
   Значение **page[size]** указывает на количество акций, 
   

*Ответ*::
   
   - Status: 200 OK


*Дата данные*:

.. code-block:: json

    {
        "links": {
            "first": "http://127.0.0.1:8000/api/v1/sale/30/products/?page%5Bnumber%5D=1&page%5Bsize%5D=3",
            "last": "http://127.0.0.1:8000/api/v1/sale/30/products/?page%5Bnumber%5D=3&page%5Bsize%5D=3",
            "next": "http://127.0.0.1:8000/api/v1/sale/30/products/?page%5Bnumber%5D=2&page%5Bsize%5D=3",
            "prev": null
        },
        "data": [
            {
                "type": "Product",
                "id": "4000",
                "attributes": {
                    "full_name": "Смарт-часы Huawei Watch Fit New Isle Blue TIA-B09 MCHN03",
                    "category_id": 2168
                }
            },
            {
                "type": "Product",
                "id": "4002",
                "attributes": {
                    "full_name": "Кабель HARPER DCHM-372 HDMI - HDMI 2 м",
                    "category_id": 1287
                }
            },
            {
                "type": "Product",
                "id": "4003",
                "attributes": {
                    "full_name": "Кабель HDMI HARPER DCHM-791, 1 м",
                    "category_id": 1287
                }
            }
        ],
        "meta": {
            "pagination": {
                "page": 1,
                "pages": 3,
                "count": 7
            }
        }
    }