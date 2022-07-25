Каскадная цена 🖇
========================================

API для создания каскадной акции

.. function:: Сделайте запрос методом `POST` по ссылке: /api/v1/sale/create/cascade/



   *Заголовок*::
      
      - header 'Authorization: {Token}' 
      - header 'Content-Type: application/vnd.api+json' 

   *Тело запроса*:

 .. code-block:: json

    {
        "data": {
            "type": "Sale",
            "attributes": {
                "cascade_positions": [
                    {
                        "position":1,
                        "percent":20
                    },
                    {
                        "position":2,
                        "percent":50
                    }
                ],
                "sale_type": "cascadetype",
                "prioritet": 7,
                "products_ids": [4000,4002,4003,4004,4005,4006,4007],
                "start_date": "2022-07-05 11:30:00",
                "end_date":  "2022-10-05 11:30:00",
                "payment_method": "Картой",
                "cities_ids": [1],
                "shops_ids": [1],
                "is_intersects_models_ids": [2],
                "is_use_of_bonuses": true,
                "is_manual_sale": true,
                "is_reverse": false,
                "is_compensated": true      
            }
        }   
        
    }

.. function:: Обязательные
   - Все обязательные поля, ниже предоставлены *url parameters*

   :param sale_type: "String", поле которое указывает на тип модели
   :param position: "Integer", позиция каскада
   :param percent: "Integer", процент для акции каскада
   :param count: "Integer", количество
   :param products_ids: список id продуктов
   :type products_ids: Integer Array
   :param start_date: "DateTimeField", дата начала действий акции
   :param end_date: "DateTimeField", дата окончания действий акции
   :param payment_method: "String", тип оплаты товара('Картой' или 'Наличными')
   :param cities_ids: "String", тип города 
   :param shops_ids: "String", тип склада

    
.. function:: Необязательные
   - Все необязательные поля, ниже предоставлены *url parameters*

   :param is_intersects_models_ids: список акций которые пересекаются
   :type is_intersects_models_ids: Integer Array
   :param is_use_of_bonuses: "Boolean", есть бонус или нет
   :param is_manual_sale: "Boolean", ручная скидка
   :param is_compensated: "Boolean", компенсируется или нет
   :param is_reverse: "Boolean", при значении True, выбранные товары исключает из акции
    

   

*Ответ*::
   
   - Status: 201 Created


*Дата данные*:

.. code-block:: json

    {
        "data": {
            "type": "Sale",
            "id": "39",
            "attributes": {
                "start_date": "2022-07-05T11:30:00+06:00",
                "end_date": "2022-10-05T11:30:00+06:00",
                "payment_method": "Картой",
                "is_use_of_bonuses": true,
                "is_manual_sale": true,
                "is_compensated": true,
                "prioritet": 7,
                "sale_type": "cascadetype",
                "is_active": true,
                "author_id": 1
            },
            "relationships": {
                "is_intersects_models": {
                    "data": [
                        {
                            "id": 2,
                            "model": "percenttype"
                        }
                    ]
                },
                "content_object": {
                    "data": {
                        "cascade_positions": [
                            {
                                "position": 1,
                                "percent": 20
                            },
                            {
                                "position": 2,
                                "percent": 50
                            }
                        ]
                    }
                }
            }
        }
    }