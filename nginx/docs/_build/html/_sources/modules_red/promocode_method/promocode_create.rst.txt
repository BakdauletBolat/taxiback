Создание промокода
=======================================



API для создания промокода


.. function:: Сделайте запрос методом `POST` по ссылке: /api/v1/sale/promo-code/create/


   *Заголовок*::
      
      - header 'Authorization: {Token}' 
      - header 'Content-Type: application/vnd.api+json' 

   *Тело запроса*:

 .. code-block:: json

    {
        "data": {
            "type": "Sale",
            "attributes": {
                "sale_type": "promocodetype",
                "is_intersects_models_ids": [1,2],
                "products_ids": [4000,4002,4003,4004,4005,4006,4007],
                "start_date": "2022-07-07 11:30:00",
                "end_date":  "2022-10-11 11:30:00",
                "payment_method": "Картой",
                "cities_ids": [1],
                "shops_ids": [1],
                "is_use_of_bonuses": true,
                "is_manual_sale": true,
                "is_compensated": true,
                "prioritet": 1001 ,
                "promocode_type": "fixed_price",
                "percent": "10000",
                "fixed_price": 10000,
                "promo_code": "dd",
                "activation_period_start": "2022-07-06 11:30:00",
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
   :param promocode_type: "String", тип купона(доступные значения ниже) 
   :param promocode_type(available): *percent*, *fixed_price*
   :param percent: Проценты для продукта
   :param fixed_price: Фиксированная цена для продукта
   :param promo_code: "String", уникальный id промокода;
   :param activation_period_start: DateTimeField, время начала активации
   :param activation_period_end: DateTimeField,конец активации

   .. note::
      При вводе одинакового {promo_code}, сервер выдает ошибку

      "message": "promo code type with this promo code already exists.",
 
                   


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
            "id": "46",
            "attributes": {
                "start_date": "2022-07-07T11:30:00+06:00",
                "end_date": "2022-10-11T11:30:00+06:00",
                "payment_method": "Картой",
                "is_use_of_bonuses": true,
                "is_manual_sale": true,
                "is_compensated": true,
                "prioritet": 1001,
                "sale_type": "promocodetype",
                "is_active": true,
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
                        "fixed_price": 10000,
                        "percent": 10000,
                        "promo_code": "dd",
                        "activation_period_start": "2022-07-06T11:30:00+06:00",
                        "activation_period_end": "2022-10-05T11:30:00+06:00",
                        "promocode_type": "fixed_price"
                    }
                }
            }
        }
    }