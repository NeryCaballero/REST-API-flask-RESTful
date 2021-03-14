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


# username_mapping = {u.username: u for u in users}

# for each user in users,
# set the key u.username
# equal to the user object.

# {'bob': {
#         'id': 1,
#         'username': 'bob',
#         'password': '1234'
#     }
# }


# userid_mapping = {u.id: u for u in users}

# for each user in users,
# set the key u.userid
# equal to the user object.

# {1: {
#         'id': 1,
#         'username': 'bob',
#         'password': '1234'
#     }
# }

# safe_str_cmp(user.password, password) does the same job as < user.password == password > but safer.
