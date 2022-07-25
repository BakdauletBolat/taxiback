Создание акции под клиента 🕺
========================================



API для создания акции под клиента


.. function:: Сделайте запрос методом `POST` по ссылке: /api/v1/sale/to-client/create/


   *Заголовок*::
      
      - header 'Authorization: {Token}' 
      - header 'Content-Type: application/vnd.api+json' 

   *Тело запроса*:

 .. code-block:: json

    {
        "data": {
            "type": "Sale",
            "attributes": {
                "sale_type": "saletoclienttype",
                "is_intersects_models_ids": [1,2],
                "products_ids": [4000,4002,4003,4004,4005,4006,4007],
                "start_date": "2022-10-05 11:30:00",
                "end_date":  "2022-10-05 11:30:00",
                "payment_method": "Картой",
                "cities_ids": [1],
                "shops_ids": [1],
                "is_use_of_bonuses": true,
                "is_manual_sale": true,
                "is_compensated": true,
                "prioritet": 16,
                "is_reverse": false,
                "to_client_products": [
                {
                    "product_id": 4000,
                    "new_price": 3000,
                    "old_price": 1200,
                    "clients": [129341]
                },

                {
                    "product_id": 4002,
                    "new_price": 3000,
                    "old_price": 1200,
                    "clients": [129341]
                },
                {
                    "product_id": 4003,
                    "new_price": 3000,
                    "old_price": 1200,
                    "clients": [129341]
                },
                {
                    "product_id": 4004,
                    "new_price": 3000,
                    "old_price": 1200,
                    "clients": [129341]
                },
                {
                    "product_id": 4005,
                    "new_price": 3000,
                    "old_price": 1200,
                    "clients": [129341]
                },
                {
                    "product_id": 4006,
                    "new_price": 3000,
                    "old_price": 1200,
                    "clients": [129341]
                },
                {
                    "product_id": 4007,
                    "new_price": 3000,
                    "old_price": 1200,
                    "clients": [129341]
                }
                ]
            
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
   :param payment_method: "String", тип оплаты товара
   :param cities_ids: "String", тип города 
   :param shops_ids: "String", тип склада
   :param product_id: "Integer", id продукта
   :param new_price: "Integer", новая цена для продукта
   :param old_price: "Integer", старая цена продукта
   :param clients: "Integer", id клиента
   :type clients: Integer array
   
.. function:: Необязательные
   - Все необязательные поля, ниже предоставлены *url parameters*

   :param is_intersects_models_ids: список акций которые пересекаются
   :type is_intersects_models_ids: Integer Array
   :param is_use_of_bonuses: "Boolean", есть бонус или нет
   :param is_manual_sale: "Boolean", ручная скидка
   :param is_compensated: "Boolean", компенсируется или нет
   :param prioritet: "Integer", приоритет, чем больше приоритет тем первее он будет, default значение == 100
   :param is_reverse: "Boolean", при значении True, выбранные товары исключает из акции

*Ответ*::
   
   - Status: 201 Created

*Дата данные*:

.. code-block:: json

    {
        "data": {
            "type": "Sale",
            "id": "48",
            "attributes": {
                "start_date": "2022-10-05T11:30:00+06:00",
                "end_date": "2022-10-05T11:30:00+06:00",
                "payment_method": "Картой",
                "is_use_of_bonuses": true,
                "is_manual_sale": true,
                "is_compensated": true,
                "prioritet": 16,
                "sale_type": "saletoclienttype",
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
                        "id": 4,
                        "products": [
                            {
                                "id": 22,
                                "old_price": 1200,
                                "new_price": 3000,
                                "type_id": 4,
                                "product_id": 4000,
                                "clients": [
                                    {
                                        "type": "EUser",
                                        "id": "2054"
                                    }
                                ]
                            },
                            {
                                "id": 23,
                                "old_price": 1200,
                                "new_price": 3000,
                                "type_id": 4,
                                "product_id": 4002,
                                "clients": [
                                    {
                                        "type": "EUser",
                                        "id": "2054"
                                    }
                                ]
                            },
                            {
                                "id": 24,
                                "old_price": 1200,
                                "new_price": 3000,
                                "type_id": 4,
                                "product_id": 4003,
                                "clients": [
                                    {
                                        "type": "EUser",
                                        "id": "2054"
                                    }
                                ]
                            },
                            {
                                "id": 25,
                                "old_price": 1200,
                                "new_price": 3000,
                                "type_id": 4,
                                "product_id": 4004,
                                "clients": [
                                    {
                                        "type": "EUser",
                                        "id": "2054"
                                    }
                                ]
                            },
                            {
                                "id": 26,
                                "old_price": 1200,
                                "new_price": 3000,
                                "type_id": 4,
                                "product_id": 4005,
                                "clients": [
                                    {
                                        "type": "EUser",
                                        "id": "2054"
                                    }
                                ]
                            },
                            {
                                "id": 27,
                                "old_price": 1200,
                                "new_price": 3000,
                                "type_id": 4,
                                "product_id": 4006,
                                "clients": [
                                    {
                                        "type": "EUser",
                                        "id": "2054"
                                    }
                                ]
                            },
                            {
                                "id": 28,
                                "old_price": 1200,
                                "new_price": 3000,
                                "type_id": 4,
                                "product_id": 4007,
                                "clients": [
                                    {
                                        "type": "EUser",
                                        "id": "2054"
                                    }
                                ]
                            }
                        ]
                    }
                }
            }
        }
    }