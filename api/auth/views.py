from . import auth
from .. import db 
from flask import request, make_response,json
import time
@auth.route('/login',methods=['GET','POST'])
def login():
	if request.method=='POST':
		request_message = request.get_json()
		for item in db.accountCollection.find():
			if request_message['account']==item['profile']['account']:
				if request_message['password']==item['profile']['password']:
					return make_response(json.jsonify({'msg':'success','username':item['profile']['username'],'account':item['profile']['account']}),200)
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
		return make_response(json.jsonify({'msg':'create account success','username':request_message['username'],'account':request_message['account']}),200)

