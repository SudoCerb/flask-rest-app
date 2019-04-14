from werkzeug.security import safe_str_cmp
from models.user import UserModel

def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and user.password == password: # if user and safe_str_cmp(user.password, password) ## THIS IS THE SAFE VERSION TO USE WITH 2.7
        return user

# verifies the identity of the user requesting the data
def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
