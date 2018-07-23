import time
from app import db
from .model import Users
from . import user
from ..auth.auths import Auth
from flask import jsonify, make_response, request, json
from bson.json_util import dumps

from werkzeug.security import generate_password_hash, check_password_hash, safe_str_cmp

@user.route('/test')
def test():
    user_data = {
        'name': 'armuro',
        'email': 'minuku@gmail.com'
    }
    return jsonify(user_data)

@user.route('/register', methods=['POST'])
def register():

    if request.method=='POST':
        request_message= request.get_json()
        user = {
            'email': request_message['email'],
            'username': request_message['username'],
            'password': generate_password_hash(request_message['password']),
            'signupTime': time.strftime("%c"),
            'loginTime': None
        }
        if db.UserCollection.find_one({'username': request_message['username']}):
            return make_response(json.jsonify({'error':'this account already used'}), 404)

        db.UserCollection.insert_one(user)

        return make_response(json.jsonify({'msg':'create account success'}), 200)

@user.route('/login', methods=['POST'])
def login():

    if request.method=='POST':
        request_message= request.get_json()
        username = request_message['username']
        password = request_message['password']
        if (not username or not password):
            return make_response(json.jsonify({'msg':'login feild empty'}), 404)
        else:
            return Auth.authenticate(Auth, username, password)

@user.route('/user', methods=['GET'])
def get():

    result = Auth.identify(Auth, request)
    if (result['status'] and result['data']):
        user = Users.get(Users, result['data'])
        returnUser = {
            'email':user['email'],
            'username': user['username'],
            'login_time': user['login_time']
        }
        return make_response(json.jsonify(returnUser), 200)
    return jsonify(result)
