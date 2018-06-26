from flask import Flask,request,Request,Response,json
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
			if request_message['loginName'] == item['username']:
				if request_message['loginPassword'] == item['password']:
					#return json.jsonify(name="correct account",password="")
					return "correct account"
				#else :return json.jsonify(name="",password="wrong password")
				else : return "wrong Password"		
		#return json.jsonify(name="no this account",password="")
		return "no this account"
@app.route('/signup',methods=['GET','POST'])
def signup():
	if request.method=='GET':
		return 'postyes'
	if request.method=='POST':
		request_message = request.get_json()    
		account = {'username':request_message['signupUserName'],'name':request_message['signupName'],'password':request_message['signupPassword']}
		for item in accountCollection.find():
			if request_message['signupUserName'] == item['username']:
				return json.jsonify(username="this account already in use",name="",password="")
			if request_message['signupName'] == item['username']:
				return json.jsonify(username="",name="this account already apply",password="")
		accountCollection.insert_one(account)
		return json.jsonify(username="apply ok",name="",password="")

