Купоны 🧾
========================================



API для создания купона


.. function:: Сделайте запрос методом `POST` по ссылке: /api/v1/sale/coupon/create/


   *Заголовок*::
      
      - header 'Authorization: {Token}' 
      - header 'Content-Type: application/vnd.api+json' 

   *Тело запроса*:

 .. code-block:: json

    {
        "data": {
            "type": "Sale",
            "attributes": {
                "sale_type": "coupontype",
                "is_intersects_models_ids": [2,3],
                "products_ids": [4000,4001,4002,4003,4004,4005,4006,4007],
                "start_date": "2022-10-05 11:30:00",
                "end_date":  "2022-10-05 11:30:00",
                "payment_method": "Картой",
                "cities_ids": [1],
                "shops_ids": [1],
                "is_use_of_bonuses": true,
                "is_manual_sale": true,
                "is_compensated": true,
                "prioritet": 2100 ,
                "coupon_type": "percent",
                "percent": "20",
                "activation_period_start": "2022-10-05 11:30:00",
                "activation_period_end":  "2022-10-05 11:30:00",
                "is_reverse": false
            }
        }   
        
    }
.. function:: Обязательные
   - Все поля обязательные, ниже предоставлены *url parameters*

   :param type: "String", поле которое указывает на тип модели
   :param sale_type: "String", тип акции
   :param start_date: "DateTimeField", дата начала действий акции
   :param end_date: "DateTimeField", дата окончания действий акции
   :param payment_method: "String", тип оплаты товара('Картой' или 'Наличными')
   :param cities_ids: "String", тип города 
   :param shops_ids: "String", тип склада
   :param coupon_type: "String", тип купона(*percent* или *fixed_price*) 
   :param percent: Проценты для продукта
   :param activation_period_start: DateTimeField, время начала активации
   :param activation_period_end: DateTimeField,конец активации

   
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
            "id": "47",
            "attributes": {
                "start_date": "2022-10-05T11:30:00+06:00",
                "end_date": "2022-10-05T11:30:00+06:00",
                "payment_method": "Картой",
                "is_use_of_bonuses": true,
                "is_manual_sale": true,
                "is_compensated": true,
                "prioritet": 2100,
                "sale_type": "coupontype",
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
                        }
                    ]
                },
                "content_object": {
                    "data": {
                        "id": 1,
                        "fixed_price": null,
                        "percent": 20,
                        "activation_period_start": "2022-10-05T11:30:00+06:00",
                        "activation_period_end": "2022-10-05T11:30:00+06:00",
                        "coupon_type": "percent"
                    }
                }
            }
        }
    }