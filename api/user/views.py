from .. import db
from . import user_blueprint
from flask import request,make_response,json
from urllib import parse
from bson.json_util import dumps
from .models import User
import jwt
import datetime
from ..auth.views import verifyToken
from ..auth import authConfig

@user_blueprint.route('/profile',methods=['GET'])
def query_profile():
	if request.method =='GET':
		token = parse.parse_qs(parse.urlparse(request.url).query)['token'][0]
		payload = verifyToken(token)
		if(type(payload) is not dict):
			return make_response(payload)
		else:
			account = payload['sub']
			user = User(account=account)
			return make_response(user.getProfile(),200)

@user_blueprint.route('/profile',methods=['POST','PUT'])
def updateProfile():
	if request.method=='PUT':
		token = parse.parse_qs(parse.urlparse(request.url).query)['token'][0]
		payload = verifyToken(token)
		if(type(payload) is not dict):
			return make_response(payload)
		else:
			account = payload['sub']
			user = User(account=account)
			update_data = request.get_json()
			user.updateProfile(update_data)
			return make_response('update profile success',200)

