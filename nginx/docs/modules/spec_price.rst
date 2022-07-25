Специальная цена  📈
========================================

API для создания акции со спец ценой




.. function:: Сделайте запрос методом `POST` по ссылке: /api/v1/sale/create/special-price/



   *Заголовок*::
      
      - header 'Authorization: {Token}' 
      - header 'Content-Type: application/vnd.api+json' 

   *Тело запроса*:

 .. code-block:: json

    {
        "data": {
            "type": "Sale",
            "attributes": {
                "sale_type": "percenttype",
                "percent_products": [
                {
                    "product_id": 4000,
                "percent": 20,
                    "old_price": 1200
                },

                {
                    "product_id": 4002,
                    "percent": 20,
                    "old_price": 1200
                },
                {
                    "product_id": 4003,
                    "percent": 20,
                    "old_price": 1200
                },
                {
                    "product_id": 4004,
                    "percent": 20,
                    "old_price": 1200
                },
                {
                    "product_id": 4005,
                    "percent": 20,
                    "old_price": 1200
                },
                {
                    "product_id": 4006,
                    "percent": 20,
                    "old_price": 1200
                },
                {
                    "product_id": 4007,
                    "percent": 20,
                    "old_price": 1200
                }
                ],
                "products_ids": [4000,4002,4003,4004,4005,4006,4007],
                "start_date": "2022-10-05 11:30:00",
                "end_date":  "2022-10-05 11:30:00",
                "payment_method": "Картой",
                "cities_ids": [1],
                "shops_ids": [1],
                "is_intersects_models_ids": [2,3,4],
                "is_use_of_bonuses": true,
                "is_manual_sale": true,
                "is_compensated": true,
                "prioritet": 10,
                "is_reverse": false
            }
        }   
        
    }

.. function:: Обязательные
   - Все поля обязательные, ниже предоставлены *url parameters*

   :param type: "String", поле которое указывает на тип модели
   :param sale_type: "String", тип акции
   :param product_id: "Integer",  id продукта
   :param old_price: "Integer", старая цена продукта
   :param new_price: "Integer",  новая цена продукта
   :param products_ids: список id продуктов, должен совпадает из объекта *special_price_products*
   :type products_ids: Integer Array
   :param start_date: "DateTimeField", дата начала действий акции
   :param end_date: "DateTimeField", дата окончания действий акции
   :param payment_method: "String", тип оплаты товара('Картой' или 'Наличными')
   :param cities_ids: "String", тип города 
   :param shops_ids: "String", тип склада

.. function:: Необязательные
   - Все необязательные поля, ниже предоставлены *url parameters*

   :param is_intersects_models: список акций которые пересекаются
   :type is_intersects_models: Integer Array
   :param is_use_of_bonuses: "Boolean", есть бонус или нет
   :param is_manual_sale: "Boolean", ручная скидка
   :param is_compensated: "Boolean", компенсируется или нет
   :param prioritet: "Integer", приоритет, чем больше приоритет тем первее он будет, default значение == 100
   :param is_reverse: "Boolean", при значении True, выбранные товары исключает из акции


*Ответ*::
   
   - Status: 201 Created


*Дата даннные*:

.. code-block:: json

    {
        "data": {
            "type": "Sale",
            "id": "41",
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
                        "id": 2,
                        "products": [
                            {
                                "id": 8,
                                "old_price": 1200,
                                "percent": 20,
                                "type_id": 2,
                                "product_id": 4000
                            },
                            {
                                "id": 9,
                                "old_price": 1200,
                                "percent": 20,
                                "type_id": 2,
                                "product_id": 4002
                            },
                            {
                                "id": 10,
                                "old_price": 1200,
                                "percent": 20,
                                "type_id": 2,
                                "product_id": 4003
                            },
                            {
                                "id": 11,
                                "old_price": 1200,
                                "percent": 20,
                                "type_id": 2,
                                "product_id": 4004
                            },
                            {
                                "id": 12,
                                "old_price": 1200,
                                "percent": 20,
                                "type_id": 2,
                                "product_id": 4005
                            },
                            {
                                "id": 13,
                                "old_price": 1200,
                                "percent": 20,
                                "type_id": 2,
                                "product_id": 4006
                            },
                            {
                                "id": 14,
                                "old_price": 1200,
                                "percent": 20,
                                "type_id": 2,
                                "product_id": 4007
                            }
                        ]
                    }
                }
            }
        }
    }