## Notes for myself:
- When using ```flask_restful```, it's no longer needed to ```jsonify()``` our responses because ```flask_restful``` does it, 
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
    
- Line 40: Declaring `global items` before `items` is needed to specify that the value to filter is the value declared **outside** de function scope.  
    









