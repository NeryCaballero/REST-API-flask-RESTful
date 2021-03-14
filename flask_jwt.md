# Authentication with flask_jwt

JWT stands for JSON Web Token.

Tokens are used as a means to know if a user has logged in.


## Create a new file: user.py
- Create a ```User``` class.
- Each user has an ```id```, a ``username`` and a `password` property.

```python
class User():
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password
```

## Create a new file: security.py

It will contain an in-memory table of our users to mimic a database and 2 important functions. 

```python
from werkzeug.security import safe_str_cmp
from user import User

users = [
    User(1, 'bob', '1234')
]

username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
```

1. Import the User model : ```from user import User```.
2. Create a ```users``` list. 
3. Create a `username_mapping` dictionary : ```{'username': {user object}}```.
4. Create a  `userid_mapping` dictionary : ```{userid: {user object}}```.
> We create this mappings so we don't have to iterate over our list every time.
> Each mapping lets us immediately find the user that we're looking for, just by knowing its username or its user ID.

5. Create the following functions:
- ```authenticate(username, password)```: finds a user by *username*. If there isn't a user with this username in the mapping, it will return ```none```.
  

- ```identity(payload)```: the payload is the contents of the JWT Token. ```payload['identity']``` contains the *used_id*. With the used_id we can retrieve the specific user that matches this payload via ```userID_mapping.get(userID)``` or ```none``` as a default.

**6. werkzeug.security, safe_str_cmp()**

Flask comes with the nice library called `werkzeug`, that has a very nice method to compare strings safely.

- On `security.py` :
    - `from werkzeug.security import safe_str_cmp`
    - `safe_str_cmp(user.password, password)` compares two strings. 
    - It does the same job as `user.password == password` but safer.

## On *app.py*

- Import:

``` py
from flask_jwt import JWT, jwt_required, current_identity
from security import authenticate, identity
```

- Declare:
``` py
app.secret_key = 'a_very_secure_long_complicated_key'
```  
[```app.secret_key```](https://www.kite.com/python/docs/flask.app.Flask.secret_key)  should be secret. **DO NOT publish the secret key**. 

Your key needs to be stored **securely**. It is recommended to make the key long and complicated.

*For the educational purpose of this project, it will be visible and simple.*


- Declare :
``` py 
jwt = JWT(app, authenticate, identity)
```
* `JWT` creates a new endpoint: ` POST /auth`.
* When we call `/auth` we send a `username` and a `password`.
* `JWT`  gets that `username` and `password` and sends it over to the `authenticate` function. 
* The `authenticate` function finds the correct `user` object.
* If the passwords match, it's going to return the user and that becomes the `payload['identity']`.
* Then, the `/auth` endpoint returns a `token`.
* The following request will be sent with the `token`.  
 * `JWT` calls the `identity` function uses the token to get the user's ID. 

>>> That's how a user gets **`authenticated`**.
   
* Add `@jwt_required` decorator in front of our GET method.

```python
class Item(Resource):
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404
```


### To test this endpoint with postman: 
1. Run the app on a local host port 5000.
2. Request POST : `localhost:5000/auth` 
  - Include the header: `Content-Type : application/json`
  - Pass on the body the information of an existing `user` in `users` in JSON format.
```json
{
  "username": "bob",
  "password": "1234"
}
```
  - It will respond with the `access token`:
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MTU3NTc0MjQsImlhdCI6MTYxNTc1NzEyNCwibmJmIjoxNjE1NzU3MTI0LCJpZGVudGl0eSI6MX0.qa6AYlTnMY7THYtBFzSs44H4Jc3uFSLa5vfpw6gQYLY",
}
```

3. Request GET : localhost:5000/item/item1          -- *make sure its been previously created*.
```json
{
    "description": "Request does not contain an access token",
    "error": "Authorization Required",
    "status_code": 401
}
```

- Without a token it fails the authentication and the information is not provided.

4. Include the header `Authorization : JWT <insert-the-token-without-the-quotation-marks-here>`
- `JWT` must be capital letters, there must be a `blank space` in between *JWT* and the token.
- Authentication succeeds and you can access the information.

...

...

...

...

...

...

...

...

...

...

...























