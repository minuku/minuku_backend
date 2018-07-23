from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from bson.json_util import dumps

# This could be a SQLAlchemy model,
# an ElasticSearch document, a MongoDB document, etc
class User():
    def __init__(self, account=None, username=None, password=None):
        self.id = account
        self.account = account
        self.email = account
        self.username = username
        self.password = password

    def getProfile(user):
        profile = db.UserCollection.find({'id': user.id})
        if profile:
            return dumps(profile[0])
        return False

    def updateProfile(self, data):
        db.accountCollection.update_one(\
                     {'account':self.account},\
                     {'$set':{'username':data['username'],\
                             'password':data['password'],\
                             'email':data['email'],\
                             'updataTime':time.strftime("%c")}},upsert=True)
