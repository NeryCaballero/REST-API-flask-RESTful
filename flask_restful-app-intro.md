# To created a simple flask_restful app:

1. Imports:
     ```from flask import Flask```
     ```from flask_restful import Resource, Api```

2. Define app.

3. Define api : via [```api = Api(app)```](https://www.kite.com/python/docs/flask_restful.Api) this allows us to very easily add resources to the API.

4. Define resource(s), which in this case we've only got one: ```Student``` which inherits from class [```Resource```](https://www.kite.com/python/docs/flask_restful.Resource).

5. Define the methods that this resource is going to accept (get, post, delete, put and so on...).

6. Add the resource(s) via [```api.add_resource(resource, endpoint)```](https://www.kite.com/python/docs/flask_restful.Api.add_resource).
    - the method's parameter ```def get(self, name):``` goes into the endpoint's parameter ```'/student/<string:name>'```.

7. Finally, run the app and try it out in Postman.

```py
from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class Student(Resource):
    def get(self, name):
        return {'student': name}


api.add_resource(Student, '/student/<string:name>')

app.run(port=5000)
```

