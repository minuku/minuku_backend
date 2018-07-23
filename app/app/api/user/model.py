from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from bson.json_util import dumps

class Users():

    def __init__(self, username, password, email):
        # self.id = self.id
        self.email = email
        self.username = username
        self.password = password
        self.login_time = None

    def __str__(self):
        return "Users(id='%s')" % self.id

    def set_password(self, password):
        return generate_password_hash(password)

    def check_password(self, hash, password):
        return check_password_hash(hash, password)

    def get(self, username):
        profile = db.UserCollection.find_one({'username': username})
        if profile:
            return profile
        return False

    def add(self, user):
        Exist = db.UserCollection.find({'username': 'asd'})
        if Exist[0]:
            return False
        else:
            newUser = {
                'password': user.password,
                'username': user.username,
                'email': user.email
            }
            db.UserCollection.insert_one(newUser)
            return True

    def update(self, username, data):
        db.UserCollection.update_one(
                    {'username': username},
                    {
                        '$set': {
                            'login_time': data['login_time']
                        }
                    }, upsert=True)
