from user import User

users = [
    User('0', 'asdf')
]

uid_mapping = {
    u.id: u for u in users
}


def authenticate(uid, password):
    user = uid_mapping.get(uid, None)
    if user and user.password == password:
        return user


def identity(payload):
    uid = payload['identity']
    return uid_mapping.get(uid, None)
