import sys
sys.path.append('~/minuku/api')
from api.returnMsg import responseMsg
from . import condition_blueprint
from flask import request, make_response,json
from urllib import parse
from bson.json_util import dumps
from .models import Condition


@condition_blueprint.route('/project/<string:projectName>/situation/<string:situationName>/condition',methods=['POST'])
def createCondition(projectName,situationName):
	obj = request.get_json()
	condition = Condition(projectOwner = obj['account'],projectName = projectName, situationName = situationName,conditionName=obj['conditionName'])
	result = condition.createCondition()
	if result in list(responseMsg.situation_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	if result in list(responseMsg.project_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	if result in list(responseMsg.condition_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	else: return make_response(json.jsonify({'msg':result}),200)

@condition_blueprint.route('/project/<string:projectName>/situation/<string:situationName>/condition/<string:conditionName>',methods=['DELETE'])
def deleteCondition(projectName,situationName,conditionName):
	obj = request.get_json()
	condition = Condition(projectOwner = obj['account'],projectName = projectName,situationName=situationName, conditionName=conditionName)
	result = condition.deleteCondition()
	if result in list(responseMsg.situation_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	if result in list(responseMsg.project_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	if result in list(responseMsg.condition_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	else: return make_response(json.jsonify({'msg':result}),200)

@condition_blueprint.route('/project/<string:projectName>/situation/<string:situationName>/condition/<string:conditionName>',methods=['GET'])
def getCondition(projectName,situationName,conditionName):
	try:
		obj = request.get_json()
		account = obj['account']
	except TypeError:
		url = request.url
		account = parse.parse_qs(parse.urlparse(url).query)['account'][0]
	condition = Condition(projectOwner = account,projectName = projectName,situationName=situationName, conditionName=conditionName)
	result = condition.getCondition()
	if result in list(responseMsg.situation_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	if result in list(responseMsg.project_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	if result in list(responseMsg.condition_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	else: return make_response(result,200)

@condition_blueprint.route('/project/<string:projectName>/situation/<string:situationName>/condition',methods=['GET'])
def getAllConditions(projectName,situationName):
	try:
		obj = request.get_json()
		account = obj['account']
	except TypeError:
		url = request.url
		account = parse.parse_qs(parse.urlparse(url).query)['account'][0]
	result = Condition.getAllConditions(projectOwner=account,projectName = projectName,situationName = situationName)
	if result in list(responseMsg.situation_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	if result in list(responseMsg.project_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	if result in list(responseMsg.condition_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	else: return make_response(result,200)

