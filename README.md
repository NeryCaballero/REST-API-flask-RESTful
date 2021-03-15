# REST-API-flask-RESTful

This project is a continuation of [my previous REST API](https://github.com/NeryCaballero/REST-API-flask) created with Python and ```flask```. 

This time I have used ```flask```, ```flask_restful``` and ```flask_jwt```.

I have applied a ["Test-first"](https://github.com/NeryCaballero/REST-API-flask-RESTful/blob/main/Test-first-API-design.md) design concept to determine all the endpoints needed before writing the code.

This API has 2 resources: ```Item``` and ```Items``` created based on [```flask_restful.Resource```](https://www.kite.com/python/docs/flask_restful.Resource) which represents an abstract RESTful resource. 

`authentication` has been applied with `flask_jwt`.

The API information is stored in memory database in the form of a list of dictionaries.
I will be storing data on a `file.db` in my [next project](https://github.com/NeryCaballero/projectFlaskRESTfulSQLite).

The available endpoints are:
- GET `localhost:5000/items`
- GET POST PUT DEL `localhost:5000/item/<item-name>`

- Authentication  `localhost:5000/auth`
  - Instructions [here](https://github.com/NeryCaballero/REST-API-flask-RESTful/blob/main/flask_jwt.md)

<hr>
