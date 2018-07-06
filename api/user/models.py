from .. import db
from bson.json_util import dumps
import time

class User():
	def __init__(self,account=None,username=None,password=None):
		self.account = account
		self.name = username
		self.password = password

	def getProfile(self):
		profile = db.accountCollection.find({'profile.account':self.account},{'profile':1})
		return dumps(profile[0]['profile'])

	def updateProfile(self,data):
		db.accountCollection.update_one(\
                     {'profile.account':self.account},\
                     {'$set':{'profile.username':data['username'],\
                             'profile.password':data['password'],\
                             'profile.email':data['email'],\
                             'profile.updataTime':time.strftime("%c")}},upsert=True)
              		
