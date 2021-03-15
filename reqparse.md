#Validating and Sanitizing JSON Payload.

##flask_restful.reqparse
Request parsing makes sure that only some elements can be passed in through the JSON payload.

Flask-RESTful has a really nice way of doing this, which is using [reqparse](https://www.kite.com/python/docs/flask_restful.reqparse.RequestParser).

1.Import reqparse from Flask-RESTful.
```python
from flask_restful import reqparse
```

2. Go to the endpoint that needs the parsing and declare at the very top of the block of code:  

``` python
parser = reqparse.RequestParser() 
```

This initialises a new object, which we can use to parse the request.

We're going to run the request through it and see what arguments match those that we defined in the parser.

3. Define arguments: 
```python
parser.add_argument('price',
                    type=float,
                    required=True,
                    help="This field cannot be left blank!")
```

It accepts one or more arguments and additional information such as the type, required and help which is a description returned in the response when the argument is invalid. See [Argument's constructor](https://www.kite.com/python/docs/flask_restful.reqparse.Argument) for documentation on the available options.

When we run the request, is going to look in the JSON payload, but it would also look in, for example, form payloads, so if you have an HTML form that sends you some data, you can use this request parser to go through the form fields as well.

4. Assign data to be equal to the parsed argument: [parse_args()](https://www.kite.com/python/docs/flask_restful.reqparse.RequestParser.parse_args)
```python
data = parser.parse_args()
```

- Data will only receive the valid arguments.
- If any other arguments is sent in the JSON payload, it will just get erased and it will not be accepted.

Alltogether will look like this:
```python
def put(self, name):
    parser = reqparse.RequestParser() 
    parser.add_argument('price',
                    type=float,
                    required=True,
                    help="This field cannot be left blank!")
    data = parser.parse_args()

    item = next(filter(lambda x: x['name'] == name, items), None)
    if item is None:
        item = {'name': name, 'price': data['price']}
        items.append(item)
    else:
        item.update(data)
    return item
```

* In this example, we are only allowing the `price` to be updated. 
* We are preventing any changes on the `name`.

## Reusing the same parsing  on multiple endpoints
- Declare parser and define the argument(s) at the beginning of the class.  
```python
class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )
```

- Now the parser belongs to the class, as opposed to belonging to one of the methods.
- Notice there is no `self.` in front, so the parser belongs to the class itself, and not to one specific item resource, 
- The way to call and use this parser is by saying `Class-name.parser.parse_args` in this case:
```python
data = Item.parser.parse_args()
```
We can access `Item.parser.parse_args()` from multiple methods.

All together will look like this: 
```python
class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank!")
    
    def put(self, name):
    
        data = Item.parser.parse_args()
    
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item
```

<hr>
