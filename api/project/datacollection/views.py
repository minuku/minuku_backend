import sys
sys.path.append('~/minuku/api')
from api.returnMsg import responseMsg
from . import datacollection_blueprint
from flask import request, make_response,json
from urllib import parse
from bson.json_util import dumps
from .models import Datacollection

@datacollection_blueprint.route('/project/<string:projectName>/situation/<string:situationName>/datacollection',methods=['POST'])
def createDatacollection(projectName,situationName):
	obj = request.get_json()
	datacollection = Datacollection(projectOwner = obj['account'],
                                        projectName = projectName, 
                                        situationName = situationName,
                                        datacollectionName=obj['datacollectionName'],
                                        datacollectionType=obj['datacollectionType'],
                                       )
	result = datacollection.createDatacollection()
	if result in list(responseMsg.situation_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	if result in list(responseMsg.project_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	if result in list(responseMsg.datacollection_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	else: return make_response(json.jsonify({'msg':result}),200)


@datacollection_blueprint.route('/project/<string:projectName>/situation/<string:situationName>/datacollection/<string:datacollectionName>',methods=['DELETE'])
def deleteDatacollection(projectName,situationName,datacollectionName):
	obj = request.get_json()
	datacollection = Datacollection(projectOwner = obj['account'],
                                        projectName = projectName,
                                        situationName = situationName,
                                        datacollectionName=datacollectionName
                                       )
	result = datacollection.deleteDatacollection()
	if result in list(responseMsg.situation_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	if result in list(responseMsg.project_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	if result in list(responseMsg.datacollection_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	else: return make_response(json.jsonify({'msg':result}),200)

@datacollection_blueprint.route('/project/<string:projectName>/situation/<string:situationName>/datacollection/<string:datacollectionName>',methods=['GET'])
def getDatacollection(projectName,situationName,datacollectionName):
	try:
		obj = request.get_json()
		account = obj['account']
	except TypeError:
		url = request.url
		account = parse.parse_qs(parse.urlparse(url).query)['account'][0]
	datacollection = Datacollection(projectOwner = account,
                                        projectName = projectName,
                                        situationName = situationName,
                                        datacollectionName=datacollectionName
                                       )
	result = datacollection.getDatacollection()
	if result in list(responseMsg.situation_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	if result in list(responseMsg.project_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	if result in list(responseMsg.datacollection_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	else: return make_response(result,200)

@datacollection_blueprint.route('/project/<string:projectName>/situation/<string:situationName>/datacollection',methods=['GET'])
def getAllDatacollections(projectName,situationName):
	try:
		obj = request.get_json()
		account = obj['account']
	except TypeError:
		url = request.url
		account = parse.parse_qs(parse.urlparse(url).query)['account'][0]
	result = Datacollection.getAllDatacollections(projectOwner =account,
                                                      projectName = projectName,
                                                      situationName = situationName
                                                     )
	if result in list(responseMsg.situation_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	if result in list(responseMsg.project_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	if result in list(responseMsg.datacollection_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	else: return make_response(result,200)

