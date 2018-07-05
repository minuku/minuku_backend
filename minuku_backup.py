from flask import Flask,request,Request,Response,json,abort,make_response
from flask_cors import CORS
#from flask_restful import abort, Api, fields, marshal_with, reqparse, Resource
from html.parser import HTMLParser
from pymongo import MongoClient,InsertOne, DeleteOne, ReplaceOne
from pymongo.cursor import CursorType
from pymongo.collection import Collection
from bson.json_util import dumps
from urllib import parse
from urllib import request as urlrequest
#import urllib.request
#import urllib.parse
import time
app = Flask(__name__)
CORS(app)
client = MongoClient('localhost', 27017)#make a connection, which means you can connet to any database within this host
db = client.minukuTestDB# get a db
ssensorDataCollection = db.sensorDataCollection 
accountCollection = db.accountCollection  

@app.route('/login',methods=['GET','POST'])
@cross_origin()
def login():
	if request.method=='GET':
		return 'yes'
	if request.method=='POST':
		request_message = request.get_json()
		for item in accountCollection.find():
			if request_message['account'] == item['profile']['account']:
				if request_message['password'] == item['profile']['password']:
					#return json.jsonify(name="correct account",password="")
					#return "correct account"
					return make_response(json.jsonify({'msg':'success','username':item['profile']['username'],'account':item['profile']['account']}),200)
				#else :return json.jsonify(name="",password="wrong password")
				#else : return "wrong Password"
				else : return make_response(json.jsonify({'error':'wrong password'}),404)		
		#return json.jsonify(name="no this account",password="")
		#return "no this account"
		return make_response(json.jsonify({'error':'no this account'}),404)
@app.route('/signup',methods=['GET','POST'])
@cross_origin()
def signup():
	if request.method=='POST':
		request_message = request.get_json()    
		account = {'account':request_message['account'],'username':request_message['username'],'password':request_message['password'],'email':request_message['email'],'signupTime':time.strftime("%c")}
		for item in accountCollection.find():
			if request_message['account'] == item['profile']['account']:
				return make_response(json.jsonify({'error':'this account already used'}),404)
		accountCollection.insert_one({'profile':account})
		return make_response(json.jsonify({'msg':'create account success','username':request_message['username'],'account':request_message['account']}),200)

@app.route('/<string:account>/profile',methods=['GET'])
@cross_origin()
def query_profile(account):
	if request.method =='GET':
		data = accountCollection.find({'profile.account':account},{'profile':1})
		return make_response(dumps(data[0]),200)


@app.route('/profile2',methods=['GET'])
@cross_origin()
def query_profile2():
	if request.method == 'GET':
		#url = urlrequest.Request.get_full_url()
		url = request.url
		query_component = parse.urlparse(url).query
		signupAccount = parse.parse_qs(query_component)['account'][0]
		data = accountCollection.find({'profile.account':signupAccount},{'profile':1})
		return make_response(dumps(data[0]),200)

