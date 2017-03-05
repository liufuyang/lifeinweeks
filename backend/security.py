from werkzeug.security import safe_str_cmp

from models.user import UserModel

def authenticate(uid, password):
    user = UserModel.find_by_uid(uid)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    uid = payload['identity']
    return UserModel.find_by_uid(uid)
