import sys
sys.path.append('~/minuku/api')
from api.returnMsg import responseMsg
from . import situation_blueprint
from flask import request, make_response,json
from urllib import parse
from bson.json_util import dumps
from .models import Situation
@situation_blueprint.route('/project/<string:projectName>/situation',methods=['POST'])
def createsituation(projectName):
	obj = request.get_json()
	situation = Situation(projectName=projectName,projectOwner= obj['account'],situationName=obj['situationName'])
	result = situation.createSituation()
	if result in list(responseMsg.situation_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	if result in list(responseMsg.project_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	else:
		return make_response(json.jsonify({'msg':result}),200)

@situation_blueprint.route('/project/<string:projectName>/situation/<string:situationName>',methods=['DELETE'])
def deletesituation(projectName,situationName):
	obj = request.get_json()
	situation = Situation(projectName=projectName,projectOwner= obj['account'],situationName=situationName)
	result = situation.deleteSituation()
	if result in list(responseMsg.situation_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	if result in list(responseMsg.project_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	else:
		return make_response(json.jsonify({'msg':result}),200)

@situation_blueprint.route('/project/<string:projectName>/situation',methods=['GET'])
def getAllSituations(projectName):
	try:
		obj = request.get_json()
		account = obj['account']
	except TypeError:
		url = request.url
		account = parse.parse_qs(parse.urlparse(url).query)['account'][0]
	result = Situation.getAllSituations(account,projectName)
	if result in list(responseMsg.situation_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	if result in list(responseMsg.project_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	else:
		return make_response(result,200)
@situation_blueprint.route('/project/<string:projectName>/situation/<string:situationName>',methods=['GET'])
def getSituation(projectName,situationName):
	try:
		obj = request.get_json()
		account = obj['account']
	except TypeError:
		url = request.url
		account = parse.parse_qs(parse.urlparse(url).query)['account'][0]
	situation = Situation(projectName=projectName,projectOwner=account,situationName=situationName)
	result = situation.getSituation()
	if result in list(responseMsg.situation_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	if result in list(responseMsg.project_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	else:
		return make_response(result,200)
	
