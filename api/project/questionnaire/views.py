import sys
sys.path.append('~/minuku/api')
from api.returnMsg import responseMsg
from . import questionnaire_blueprint
from flask import request, make_response,json
from urllib import parse
from bson.json_util import dumps
from .models import Questionnaire
from api.auth.views import verifyToken

@questionnaire_blueprint.route('/project/<string:projectName>/questionnaire',methods=['POST'])
def createDatacollection(projectName):
	token = parse.parse_qs(parse.urlparse(request.url).query)['token'][0]
	payload = verifyToken(token)
	if (type(payload)is not dict):
		return make_response(payload)
	else:
		account = payload['sub']
		obj = request.get_json()
		questionnaire = Questionnaire(projectOwner = account,
											projectName = projectName, 
											questionnaireName=obj['questionnaireName'],
											questionnaireType=obj['questionnaireType'],
											questionnaireContent=obj['questionnaireContent']

										   )
		result = questionnaire.createQuestionnaire()
		if result in list(responseMsg.project_Error.values()):
			return make_response(json.jsonify({'error':result}),404)
		if result in list(responseMsg.questionnaire_Error.values()):
			return make_response(json.jsonify({'error':result}),404)
		else: return make_response(json.jsonify({'msg':result}),200)


@questionnaire_blueprint.route('/project/<string:projectName>/questionnaire/<string:questionnaireName>',methods=['DELETE'])
def deleteQuestionnaire(projectName,questionnaireName):
	token = parse.parse_qs(parse.urlparse(request.url).query)['token'][0]
	payload = verifyToken(token)
	if (type(payload)is not dict):
		return make_response(payload)
	else:
		account = payload['sub']	
		questionnaire = Questionnaire(projectOwner = account,
                                        projectName = projectName,
                                        questionnaireName=questionnaireName
                                       )
		result = questionnaire.deleteQuestionnaire()
		if result in list(responseMsg.project_Error.values()):
			return make_response(json.jsonify({'error':result}),404)
		if result in list(responseMsg.questionnaire_Error.values()):
			return make_response(json.jsonify({'error':result}),404)
		else: return make_response(json.jsonify({'msg':result}),200)

@questionnaire_blueprint.route('/project/<string:projectName>/questionnaire/<string:questionnaireName>',methods=['GET'])
def getQuestionnaire(projectName,questionnaireName):
	token = parse.parse_qs(parse.urlparse(request.url).query)['token'][0]
	payload = verifyToken(token)
	if (type(payload)is not dict):
		return make_response(payload)
	else:
		account = payload['sub']
	questionnaire = Questionnaire(projectOwner = account,
                                        projectName = projectName,
                                        questionnaireName=questionnaireName
                                       )
	result = questionnaire.getQuestionnaire()
	if result in list(responseMsg.project_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	if result in list(responseMsg.questionnaire_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	else: return make_response(result,200)

@questionnaire_blueprint.route('/project/<string:projectName>/questionnaire',methods=['GET'])
def getAllQuestionnaires(projectName):
	token = parse.parse_qs(parse.urlparse(request.url).query)['token'][0]
	payload = verifyToken(token)
	if (type(payload)is not dict):
		return make_response(payload)
	else:
		account = payload['sub']
	result = Questionnaire.getAllQuestionnaires(projectOwner =account,
                                                      projectName = projectName,
                                                     )
	if result in list(responseMsg.project_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	if result in list(responseMsg.questionnaire_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	else: return make_response(result,200)

