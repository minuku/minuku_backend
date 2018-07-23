from . import auth
from .. import db 
from flask import request, make_response,json
import time
import jwt
import datetime
from . import authConfig
from bson.json_util import dumps
def verifyToken(token):
	try:
		payload = jwt.decode(token,authConfig.SECRET_KEY,algorithm=authConfig.alg)
	except jwt.ExpiredSignatureError:
		return make_response(json.jsonify('token expired, please login again'),404)
	except jwt.DecodeError:
		return make_response(json.jsonify('token error, please login again'),404)
	return payload

def authenticate(payload):
	auth_token = jwt.encode(payload,authConfig.SECRET_KEY,algorithm=authConfig.alg)
	return auth_token

@auth.route('/login',methods=['GET','POST'])
def login():
	if request.method=='POST':
		request_message = request.get_json()
		for item in db.accountCollection.find():
			if request_message['account']==item['profile']['account']:
				if request_message['password']==item['profile']['password']:
					payload = {
                               'exp':datetime.datetime.utcnow()+datetime.timedelta(days=0,minutes=30, seconds=0),
                               'iat':datetime.datetime.utcnow(),
                               'sub':request_message['account']
                              }
					auth_token = authenticate(payload)
					return make_response(auth_token,200)
					#return make_response(json.jsonify({'msg':'success','username':item['profile']['username'],'account':item['profile']['account']}),200)
				else : return make_response(json.jsonify({'error':'wrong password'}),404)
		return make_response(json.jsonify({'error':'no this account'}),404)


@auth.route('/signup',methods=['GET','POST'])
def signup():
	if request.method=='POST':
		request_message= request.get_json()
		account = {'account':request_message['account'],'username':request_message['username'],'password':request_message['password'],'email':request_message['account'],'signupTime':time.strftime("%c")}
		for item in db.accountCollection.find():
			if request_message['account']==item['profile']['account']:
				return make_response(json.jsonify({'error':'this account already used'}),404)
		db.accountCollection.insert_one({'profile':account})
		payload = {
                   'exp':datetime.datetime.utcnow()+datetime.timedelta(days=0,minutes=30, seconds=0),
                   'iat':datetime.datetime.utcnow(),
                   'sub':request_message['account']
                  }
		auth_token = authenticate(payload)
		return make_response(auth_token,200)	
		#return make_response(json.jsonify({'msg':'create account success','username':request_message['username'],'account':request_message['account']}),200)

