# REST-API-flask-RESTful

This project is a continuation of [my previous REST API](https://github.com/NeryCaballero/REST-API-flask) created with Python and ```flask```. 

This time I have used ```flask```, ```flask_restful``` and ```flask_jwt```.

I have applied a ["Test-first"](https://github.com/NeryCaballero/REST-API-flask-RESTful/blob/main/Test-first-API-design.md) design concept to determine all the endpoints needed before writing the code.

This API has 2 resources: ```Item``` and ```Items``` created based on [```flask_restful.Resource```](https://www.kite.com/python/docs/flask_restful.Resource) which represents an abstract RESTful resource. 

authentication
stored in memory database > Python list of dictionaries



## Notes
- When using ```flask_restful```, we'd no longer need to ```jsonify()``` our responses because ```flask_restful``` does it, 
so we can just return dictionaries.

  
- [```request.get_json()```](https://www.kite.com/python/docs/flask.request.get_json) : If the request does not attach a JSON payload: *a body*, or the request does not have the proper content-type header, it will give an ```error```. 
  There are a few ways to avoid this: 
  - ```request.get_json(force=true)```: if force is set to True, the mimetype is ignored. It means that the ```content-type``` header does not needs to be ```application/JSON```. This is nice, but it's also dangerous because, you're always going to be doing the processing of the text even if it is incorrect.
  - ```request.get_json(silent=true)```: if silent is set to True the method will fail silently and return ```None```. It doesn't give an error.


- [```filter(function, iterable)```](https://www.kite.com/python/docs/builtins.filter): returns a filter object composed of elements for which the filtering function is ```True```.
    - ```list(filter(function, iterable))```: returns a list of all the items that matched the filter function.
    - ```next(filter(function, iterable))``` = returns **the first item** found by the filter function.
        - we can call next again if there are more items and that would give us the second item and then the third item and so on.
        - ```next()``` can raise an ```error``` if there is no next item. 
        -  To avoid this, pass a 2nd argument to next : ```next(filter(function, iterable), None)```
    









