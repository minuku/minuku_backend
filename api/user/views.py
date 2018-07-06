from .. import db
from . import user_blueprint
from flask import request,make_response,json
from urllib import parse
from bson.json_util import dumps
from .models import User
@user_blueprint.route('/<string:account>/profile',methods=['GET'])
def query_profile(account):
	if request.method =='GET':
		user = User(account=account)
		return make_response(user.getProfile(),200)


@user_blueprint.route('/profile',methods=['GET'])
def query_profile2():
	if request.method == 'GET':
		#url = urlrequest.Request.get_full_url()
		url = request.url
		query_component = parse.urlparse(url).query
		account = parse.parse_qs(query_component)['account'][0]
		user = User(account=account)
		return make_response(user.getProfile(),200)

@user_blueprint.route('/updateProfile',methods=['POST','PUT'])
def updateProfile():
	if request.method=='PUT':
		url = request.url
		update_data = request.get_json()
		query_component = parse.urlparse(url).query
		account = parse.parse_qs(query_component)['account'][0]
		user = User(account= account)
		user.updateProfile(update_data)
		return make_response(user.getProfile(),200)
