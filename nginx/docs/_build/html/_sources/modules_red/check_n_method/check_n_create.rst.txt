Создание N-ного чека
=======================================


API для создания n-ного чека


.. function:: Сделайте запрос методом `POST` по ссылке: /api/v1/sale/n-check/create/


   *Заголовок*::
      
      - header 'Authorization: {Token}' 
      - header 'Content-Type: application/vnd.api+json' 

   *Тело запроса*:

 .. code-block:: json

    {
        "data": {
            "type": "Sale",
            "attributes": {
                "sale_type": "checkntype",
                "is_intersects_models_ids": [1,2],
                "products_ids": [4000,4001,4002,4003,4004,4005,4006,4007],
                "start_date": "2022-10-05 11:30:00",
                "end_date":  "2022-10-05 11:30:00",
                "payment_method": "Картой",
                "shops_ids": [1],
                "cities_ids": [1],
                "is_use_of_bonuses": true,
                "is_manual_sale": true,
                "is_compensated": true,
                "prioritet": 300000,
                "every_n_check": 1040,
                "is_reverse": false
            }
        }   
        
    }

.. function:: Обязательные
   - Все поля обязательные, ниже предоставлены *url parameters*

   :param type: "String", поле которое указывает на тип модели
   :param sale_type: "String", тип акции
   :param products_ids: "Integer", продукты которые учавствуют в акции
   :type products_ids: Integer array
   :param start_date: "DateTimeField", дата начала действий акции
   :param end_date: "DateTimeField", дата окончания действий акции
   :param payment_method: "String", тип оплаты товара('Картой' или 'Наличными')
   :param cities_ids: "String", тип города 
   :param shops_ids: "String", тип склада
   :param every_n_check: "Integer", порядок чека при котором выдается акция

   
.. function:: Необязательные
   - Все необязательные поля, ниже предоставлены *url parameters*

   :param is_intersects_models_ids: список акций которые пересекаются
   :type is_intersects_models_ids: Integer Array
   :param is_use_of_bonuses: "Boolean", есть бонус или нет
   :param is_manual_sale: "Boolean", ручная скидка
   :param is_compensated: "Boolean", компенсируется или нет
   :param prioritet: "Integer", приоритет, чем больше приоритет тем первее он будет, default значение == 100

*Ответ*::
   
   - Status: 201 Created

*Дата данные*:

.. code-block:: json

    {
        "data": {
            "type": "Sale",
            "id": "45",
            "attributes": {
                "start_date": "2022-10-05T11:30:00+06:00",
                "end_date": "2022-10-05T11:30:00+06:00",
                "payment_method": "Картой",
                "is_use_of_bonuses": true,
                "is_manual_sale": true,
                "is_compensated": true,
                "prioritet": 300000,
                "sale_type": "checkntype",
                "is_active": false,
                "author_id": 1
            },
            "relationships": {
                "is_intersects_models": {
                    "data": [
                        {
                            "id": 1,
                            "model": "cascadetype"
                        },
                        {
                            "id": 2,
                            "model": "percenttype"
                        }
                    ]
                },
                "content_object": {
                    "data": {
                        "id": 3,
                        "every_n_check": 1040
                    }
                }
            }
        }
    }