from . import condition_blueprint
from flask import request, make_response,json
from urllib import parse
from bson.json_util import dumps
from .models import Condition

@condition_blueprint.route('/<string:projectName>/createCondition',methods=['POST'])
def createCondition(projectName):
	obj = request.get_json()
	condition = Condition(projectOwner = obj['account'],projectName = projectName, conditionName=obj['conditionName'])
	result = condition.createCondition()
	if result in ['projectArray empty','project Not exist','condition already exist']:
		return make_response(json.jsonify({'error':result}),404)
	else: return make_response(result,200)
@condition_blueprint.route('/<string:projectName>/deleteCondition',methods=['POST'])
def deleteCondition(projectName):
	obj = request.get_json()
	condition = Condition(projectOwner = obj['account'],projectName = projectName, conditionName=obj['conditionName'])
	result = condition.deleteCondition()
	if result in ['projectArray empty','project Not exist','condition Not exist','conditionArray empty']:
		return make_response(json.jsonify({'error':result}),404)
	else: return make_response(result,200)
@condition_blueprint.route('/<string:projectName>/Condition',methods=['GET'])
def getCondition(projectName):
	url = request.url
	query_component = parse.urlparse(url).query
	conditionName = parse.parse_qs(query_component)['conditionName'][0]
	account = parse.parse_qs(query_component)['account'][0]
	temp = ''+account+','+conditionName
	condition = Condition(projectOwner = account,projectName = projectName, conditionName=conditionName)
	result = condition.getCondition()
	if result in ['condition Not exist','projectArray empty','project Not exist','conditionArray empty']:
		return make_response(json.jsonify({'error':result}),404)
	return make_response(result,200)
