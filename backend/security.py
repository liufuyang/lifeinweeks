from werkzeug.security import safe_str_cmp

from user import User

users = [
    User('0', 'asdf')
]

uid_mapping = {
    u.id: u for u in users
}


def authenticate(uid, password):
    user = uid_mapping.get(uid, None)
    if user and safe_str_cmp(user.password.encode('utf-8'),
                             password.encode('utf-8')):
        return user


def identity(payload):
    uid = payload['identity']
    return uid_mapping.get(uid, None)
