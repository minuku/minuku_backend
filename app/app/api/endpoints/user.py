import os
import time
from flask import Flask,request,Request,Response,json,abort,make_response,jsonify
from pymongo import InsertOne, DeleteOne, ReplaceOne

from ...main import app, db
# from ...core.database import users

@app.route("/test")
def route_test():
    user_data = {
        'name': 'armuro',
        'email': 'minuku@gmail.com'
    }
    return jsonify(user_data)

@app.route("/login", methods=["POST"])
def login():
    request_message = request.get_json()
    for item in db.accountCollection.find():
        if request_message['email'] == item['profile']['email']:
            if request_message['password'] == item['profile']['password']:
                return make_response(json.jsonify({
                    'msg':'success',
                    'username':item['profile']['username'],
                    'email':item['profile']['email']
                }), 200)
            else :
                return make_response(json.jsonify({ 'error':'wrong password' }), 404)

    return make_response(json.jsonify({ 'error':'no this account' }), 404)

@app.route("/signup", methods=["POST"])
def signup():
    request_message = request.get_json()
    account = {
        'email': request_message['email'],
        'username': request_message['username'],
        'password': request_message['password'],
        'signupTime': time.strftime("%c")
    }

    print(db.accountCollection.find_one())

    for item in db.accountCollection.find():
        if account['email'] == item['profile']['email']:
            return make_response(json.jsonify({ 'error':'this account already used' }), 404)

    db.accountCollection.insert_one({'profile': account})
    return make_response(json.jsonify({
        'msg':'create account success',
        'username': account['username'],
        'email': account['email']
    }), 200)
