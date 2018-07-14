from flask import Blueprint, jsonify, make_response, request, json
from app.models import User
from app import db
import time

user = Blueprint('user', __name__)

@user.route('/test')
def test():
    user_data = {
        'name': 'armuro',
        'email': 'minuku@gmail.com'
    }
    return jsonify(user_data)

@user.route('/signup', methods=['POST'])
def signup():
    if request.method=='POST':
        request_message= request.get_json()
        account = {
            'account': request_message['account'],
            'username': request_message['username'],
            'password': request_message['password'],
            'email': request_message['account'],
            'signupTime': time.strftime("%c")
        }
        for item in db.UserCollection.find():
            if request_message['account']==item['profile']['account']:
                return make_response(json.jsonify({'error':'this account already used'}), 404)
        db.UserCollection.insert_one({'profile': account})
        return make_response(json.jsonify({'msg':'create account success', 'username':request_message['username'], 'account':request_message['account']}), 200)

@user.route('/profile/<string:account>', methods=['GET'])
def profile(account):
    if request.method =='GET':
        user = User(account=account)
        return make_response(user.getProfile(), 200)
