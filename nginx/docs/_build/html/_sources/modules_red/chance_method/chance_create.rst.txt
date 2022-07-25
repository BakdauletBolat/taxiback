Создание акции по количеству шансов
========================================



API для создание акции 


.. function:: Сделайте запрос методом `POST` по ссылке: /api/v1/sale/chance/create/


   *Заголовок*::
      
      - header 'Authorization: {Token}' 
      - header 'Content-Type: application/vnd.api+json' 

   *Тело запроса*:

 .. code-block:: json

    {
        "data": {
            "type": "Sale",
            "attributes": { 
                "sale_type": "chancetype",
                "min_amount": 50000,
                "multiplicity": 50000,
                "products_ids": [4000,4002,4003,4004,4005,4006,4007],
                "is_intersects_models_ids": [2,3,4],
                "start_date": "2022-07-07 11:30:00",
                "end_date":  "2022-07-20 11:30:00",
                "payment_method": "Картой",
                "cities_ids": [1],
                "shops_ids": [1],
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
   :param min_amount: "Integer", минимальный порог от общей суммы чека
   :param multiplicity: "Integer", минимальное число кратности для создания билетов
   :param start_date: "DateTimeField", дата начала действий акции
   :param end_date: "DateTimeField", дата окончания действий акции
   :param payment_method: "String", тип оплаты товара('Картой' или 'Наличными')
   :param cities_ids: "String", тип города 
   :param shops_ids: "String", тип склада
   :param products_ids: "Integer", продукты которые учавствуют в акции
   :type products_ids: Integer array

   
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
            "id": "43",
            "attributes": {
                "start_date": "2022-07-07T11:30:00+06:00",
                "end_date": "2022-07-20T11:30:00+06:00",
                "payment_method": "Картой",
                "is_use_of_bonuses": true,
                "is_manual_sale": true,
                "is_compensated": true,
                "prioritet": 10,
                "sale_type": "chancetype",
                "is_active": true,
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
                        "min_amount": 50000,
                        "multiplicity": 50000
                    }
                }
            }
        }
    }