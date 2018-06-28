from flask import Flask,request,Request,Response,json,abort,make_response
#from flask_restful import abort, Api, fields, marshal_with, reqparse, Resource
from html.parser import HTMLParser
from pymongo import MongoClient,InsertOne, DeleteOne, ReplaceOne
from pymongo.cursor import CursorType
from pymongo.collection import Collection
import urllib.request
app = Flask(__name__)
client = MongoClient('localhost', 27017)#make a connection, which means you can connet to any database within this host
db = client.minukuTestDB# get a db
ssensorDataCollection = db.sensorDataCollection 
accountCollection = db.accountCollection  

@app.route('/login',methods=['GET','POST'])
def login():
	if request.method=='GET':
		return 'yes'
	if request.method=='POST':
		request_message = request.get_json()
		for item in accountCollection.find():
			if request_message['signupAccount'] == item['signupAccount']:
				if request_message['signupPassword'] == item['signupPassword']:
					#return json.jsonify(name="correct account",password="")
					#return "correct account"
					return make_response(json.jsonify({'msg':'success','userName':item['userName'],'signupAccount':item['signupAccount']}),200)
				#else :return json.jsonify(name="",password="wrong password")
				#else : return "wrong Password"
				else : return make_response(json.jsonify({'error':'wrong password'}),404)		
		#return json.jsonify(name="no this account",password="")
		#return "no this account"
		return make_response(json.jsonify({'error':'no this account'}),404)
@app.route('/signup',methods=['GET','POST'])
def signup():
	if request.method=='POST':
		request_message = request.get_json()    
		account = {'signupAccount':request_message['signupAccount'],'userName':request_message['userName'],'signupPassword':request_message['signupPassword'],'signupEmail':request_message['signupEmail']}
		for item in accountCollection.find():
			if request_message['signupAccount'] == item['signupAccount']:
				return make_response(json.jsonify({'error':'this account already used'}),404)
		accountCollection.insert_one(account)
		return make_response(json.jsonify({'msg':'create account success','userName':request_message['userName'],'signupAccount':request_message['signupAccount']}),200)

@app.route('/queryProfile',methods=['GET','POST'])
def queryProfile():
	if request.method =='GET':
		request_message = request.get_json()
		for item in accountCollection.find():
			if request_message['signupAccount']== item['signupAccount']:
				return make_response(json.jsonify({'signupAccount':item['signupAccount'],'userName':item['userName'],'signupPassword':item['signupPassword'],'signupEmail':item['signupEmail']}),200)

