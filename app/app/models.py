from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from bson.json_util import dumps

# This could be a SQLAlchemy model,
# an ElasticSearch document, a MongoDB document, etc
class User():
    def __init__(self, account=None, username=None, password=None):
        self.account = account
        self.name = username
        self.password = password

    def getProfile(self):
        profile = db.UserCollection.find({'account': self.account})
        return dumps(profile[0])

    def updateProfile(self,data):
        db.accountCollection.update_one(\
                     {'account':self.account},\
                     {'$set':{'username':data['username'],\
                             'password':data['password'],\
                             'email':data['email'],\
                             'updataTime':time.strftime("%c")}},upsert=True)
