import sys
sys.path.append('~/minuku/api')
from api.returnMsg import responseMsg
from . import situation_blueprint
from flask import request, make_response,json
from urllib import parse
from bson.json_util import dumps
from .models import Situation
@situation_blueprint.route('/<string:projectName>/situation',methods=['POST'])
def create_situation(projectName):
	obj = request.get_json()
	situation = Situation(projectName=projectName,projectOwner= obj['account'],situationName=obj['situationName'])
	result = situation.createSituation()
	if result in list(responseMsg.situation_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	else:
		return make_response(json.jsonify({'msg':result}),200)

@situation_blueprint.route('/<string:projectName>/situation/<string:situationName>',methods=['DELETE'])
def delete_situation(projectName,situationName):
	obj = request.get_json()
	situation = Situation(projectName=projectName,projectOwner= obj['account'],situationName=situationName)
	result = situation.deleteSituation()
	if result in list(responseMsg.situation_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	else:
		return make_response(json.jsonify({'msg':result}),200)

@situation_blueprint.route('/<string:projectName>/situation',methods=['GET'])
def get_all_situations(projectName):
	obj = request.get_json()
	result = Situation.getAllSituations(obj['account'],projectName)
	if result in list(responseMsg.situation_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	else:
		return make_response(result,200)
@situation_blueprint.route('/<string:projectName>/situation/<string:situationName>',methods=['GET'])
def get_situation(projectName,situationName):
	obj = request.get_json()
	situation = Situation(projectName=projectName,projectOwner= obj['account'],situationName=situationName)
	result = situation.getSituation()
	if result in list(responseMsg.situation_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	else:
		return make_response(result,200)
	
