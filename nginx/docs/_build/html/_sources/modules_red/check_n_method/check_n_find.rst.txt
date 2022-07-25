Поиск акции по n-ному чеку
=======================================



API для создания промокода


.. function:: Сделайте запрос методом `POST` по ссылке: /api/v1/sale/n-check/check/


   *Заголовок*::
      
      - header 'Authorization: {Token}' 
      - header 'Content-Type: application/vnd.api+json' 

   *Тело запроса*:

 .. code-block:: json

    {
        "data": {
            "type": "CheckController",
            "attributes": {
                "check_id": 25,
                "product_ids": [1,6000]
            }
        }
    }

.. function:: Обязательные
   - Все поля обязательные, ниже предоставлены *url parameters*

   :param type: "String", поле которое указывает на тип модели
   :param check_id: "Integer", номер чека
   :param products_ids: "Integer", продукты которые учавствуют в акции
   :type products_ids: Integer array


*Ответ*::
   
   - Status: 200 OK

*Дата данные*:

.. code-block:: json
    

    {
        "data": "У вас есть скидка"
    }

*Дата данные*:

*В случае если нету скидки*

.. code-block:: json
    
    {
        "data": "Нет скидки"
    }
