import sys
sys.path.append('~/minuku/api')
from api.returnMsg import responseMsg
from . import situation_blueprint
from flask import request, make_response,json
from urllib import parse
from bson.json_util import dumps
from .models import Situation
from api.auth.views import verifyToken
@situation_blueprint.route('/project/<string:projectName>/situation',methods=['POST'])
def createsituation(projectName):
	token = parse.parse_qs(parse.urlparse(request.url).query)['token'][0]
	payload = verifyToken(token)
	if(type(payload)is not dict):
		return make_response(payload)
	else:	
		account = payload['sub']
		obj = request.get_json()
		situation = Situation(projectName=projectName,projectOwner= account,situationName=obj['situationName'])
		result = situation.createSituation()
		if result in list(responseMsg.situation_Error.values()):
			return make_response(json.jsonify({'error':result}),404)
		if result in list(responseMsg.project_Error.values()):
			return make_response(json.jsonify({'error':result}),404)
		else:
			return make_response(json.jsonify({'msg':result}),200)
@situation_blueprint.route('/project/<string:projectName>/situation/<string:situationName>',methods=['PUT'])
def editsituation(projectName,situationName):
	token = parse.parse_qs(parse.urlparse(request.url).query)['token'][0]
	payload = verifyToken(token)
	if(type(payload)is not dict):
		return make_response(payload)
	else:	
		account = payload['sub']
		obj = request.get_json()
		situation = Situation(projectName=projectName,projectOwner= account,requestBody=obj,situationName=situationName)
		result = situation.editSituation()
		if result in list(responseMsg.situation_Error.values()):
			return make_response(json.jsonify({'error':result}),404)
		if result in list(responseMsg.project_Error.values()):
			return make_response(json.jsonify({'error':result}),404)
		else:
			return make_response(json.jsonify({'msg':result}),200)



@situation_blueprint.route('/project/<string:projectName>/situation/<string:situationName>',methods=['DELETE'])
def deletesituation(projectName,situationName):
	token = parse.parse_qs(parse.urlparse(request.url).query)['token'][0]
	payload = verifyToken(token)
	if(type(payload)is not dict):
		return make_response(payload)
	else:	
		account = payload['sub']
		situation = Situation(projectName=projectName,projectOwner= account,situationName=situationName)
		result = situation.deleteSituation()
		if result in list(responseMsg.situation_Error.values()):
			return make_response(json.jsonify({'error':result}),404)
		if result in list(responseMsg.project_Error.values()):
			return make_response(json.jsonify({'error':result}),404)
		else:
			return make_response(json.jsonify({'msg':result}),200)

@situation_blueprint.route('/project/<string:projectName>/situation',methods=['GET'])
def getAllSituations(projectName):
	token = parse.parse_qs(parse.urlparse(request.url).query)['token'][0]
	payload = verifyToken(token)
	if(type(payload)is not dict):
		return make_response(payload)
	else:	
		account = payload['sub']
		result = Situation.getAllSituations(account,projectName)
		if result in list(responseMsg.situation_Error.values()):
			return make_response(json.jsonify({'error':result}),404)
		if result in list(responseMsg.project_Error.values()):
			return make_response(json.jsonify({'error':result}),404)
		else:
			return make_response(result,200)
@situation_blueprint.route('/project/<string:projectName>/situation/<string:situationName>',methods=['GET'])
def getSituation(projectName,situationName):
	token = parse.parse_qs(parse.urlparse(request.url).query)['token'][0]
	payload = verifyToken(token)
	if(type(payload)is not dict):
		return make_response(payload)
	else:	
		account = payload['sub']
		situation = Situation(projectName=projectName,projectOwner=account,situationName=situationName)
		result = situation.getSituation()
		if result in list(responseMsg.situation_Error.values()):
			return make_response(json.jsonify({'error':result}),404)
		if result in list(responseMsg.project_Error.values()):
			return make_response(json.jsonify({'error':result}),404)
		else:
			return make_response(result,200)
	
