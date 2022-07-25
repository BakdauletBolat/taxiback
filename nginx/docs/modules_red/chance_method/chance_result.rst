Создание билетов в зависимости от фискального чека 
========================================



API для создание билетов


.. function:: Сделайте запрос методом `POST` по ссылке: /api/v1/sale/chance/result/


   *Заголовок*::
      
      - header 'Authorization: {Token}' 
      - header 'Content-Type: application/vnd.api+json' 

   *Тело запроса*:

 .. code-block:: json

    {
        "data": {
            "type":"SaleCheck",
            "attributes": {
            "client_phone": "87077005975",
            "shop_id": 1,
            "products": [{
                "product_id":6000,
                "quantity": 1
            },{
                "product_id":4000,
                "quantity": 2
            },{
                "product_id":3000,
                "quantity": 2
            }
            ] 
            }
        }
                
    }



.. function:: Обязательные поля()
   - Все поля обязательные, ниже предоставлены *url parameters*

   :param type: "String", поле которое указывает на тип модели
   :param shop_id: "Integer", id магазина
   :param client_phone: "String", номер телефона клиента
   :param product_id: "Integer", id продукта
   :param quantity: "Integer", количество продукта


*Ответ*::
   
   - Status: 200 OK

*Дата данные*:

.. code-block:: json

    {
        "data": {
            "return_chance_ticket": {
                "result_chance": 4139,
                "chance_obj": {
                    "id": 3,
                    "min_amount": 1000,
                    "multiplicity": 100
                },
                "products": [
                    {
                        "product": {
                            "id": 6000,
                            "full_name": "Ноутбук Acer A315-42G NX.HF8ER.038",
                            "price": 1,
                            "category_id": 2047
                        },
                        "price": 313970
                    },
                    {
                        "product": {
                            "id": 4000,
                            "full_name": "Газовая колонка SUPERLUX 10L CF NG",
                            "price": 1,
                            "category_id": 400
                        },
                        "price": 49990
                    },
                    {
                        "product": {
                            "id": 4000,
                            "full_name": "Газовая колонка SUPERLUX 10L CF NG",
                            "price": 1,
                            "category_id": 400
                        },
                        "price": 49990
                    }
                ]
            }
        }
    }

.. function:: Значение полей

   :param result_chance: "String", количество билетов созданного для клиента
   :param min_amount: "Integer", минимальный порог сумму для участия в акции
   :param multiplicity: "Integer", кратность числа на которое делится сумма
