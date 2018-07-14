from flask import Blueprint, jsonify, make_response, request, json
from app.models import User
from app import db
import time
from bson.json_util import dumps
from werkzeug.security import generate_password_hash, check_password_hash

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
        user = {
            'account': request_message['account'],
            'username': request_message['username'],
            'password': generate_password_hash(request_message['password']),
            'email': request_message['account'],
            'signupTime': time.strftime("%c")
        }
        if db.UserCollection.find_one({'account': request_message['account']}):
            return make_response(json.jsonify({'error':'this account already used'}), 404)
        db.UserCollection.insert(user)
        return make_response(json.jsonify({'msg':'create account success'}), 200)

@user.route('/profile/<string:account>', methods=['GET'])
def profile(account):
    if request.method =='GET':
        user = User(account=account)
        return make_response(user.getProfile(), 200)
