Активация промокода
========================================



API для активации промокода


.. function:: Сделайте запрос методом `POST` по ссылке: /api/v1/sale/promo-code/activate/


   *Заголовок*::
      
      - header 'Authorization: {Token}' 
      - header 'Content-Type: application/vnd.api+json' 

   *Тело запроса*:

.. code-block:: json

    {
        "data" : {
            "type": "Sale",
            "attributes": {
                "client_phone": "77077005975",
                "promo_code": "abc2f3irst2"
            }   
            
        }
        
    }



.. function:: Обязательные
   - Все поля обязательные, ниже предоставлены *url parameters*

   :param type: "String", поле которое указывает на тип модели
   :param client_phone: "String", номер телефона клиента
   :param promo_code: "String", уникальный id промокода, можно получить при создании


   
*Ответ*::
   
   - Status: 200 OK

*Дата данные*:

.. code-block:: json

    {
        "data": "PromoCode Activated Succesfully"
    }

*При повторной активации сервер выдает ответ:*

.. code-block:: json

    {
        "data": "PromoCode already activated"
    }