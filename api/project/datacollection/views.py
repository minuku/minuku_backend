import sys
sys.path.append('~/minuku/api')
from api.returnMsg import responseMsg
from . import datacollection_blueprint
from flask import request, make_response,json
from urllib import parse
from bson.json_util import dumps
from .models import Datacollection
from api.auth.views import verifyToken

@datacollection_blueprint.route('/project/<string:projectName>/datacollection',methods=['POST'])
def createDatacollection(projectName):
	token = parse.parse_qs(parse.urlparse(request.url).query)['token'][0]
	payload = verifyToken(token)
	if (type(payload)is not dict):
		return make_response(payload)
	else:
		account = payload['sub']
		obj = request.get_json()
		datacollection = Datacollection(projectOwner = account,
											projectName = projectName, 
											datacollectionName=obj['datacollectionName'],
											datacollectionType=obj['datacollectionType'],
										   )
		result = datacollection.createDatacollection()
		if result in list(responseMsg.project_Error.values()):
			return make_response(json.jsonify({'error':result}),404)
		if result in list(responseMsg.datacollection_Error.values()):
			return make_response(json.jsonify({'error':result}),404)
		else: return make_response(json.jsonify({'msg':result}),200)


@datacollection_blueprint.route('/project/<string:projectName>/datacollection/<string:datacollectionName>',methods=['DELETE'])
def deleteDatacollection(projectName,datacollectionName):
	token = parse.parse_qs(parse.urlparse(request.url).query)['token'][0]
	payload = verifyToken(token)
	if (type(payload)is not dict):
		return make_response(payload)
	else:
		account = payload['sub']	
		datacollection = Datacollection(projectOwner = account,
                                        projectName = projectName,
                                        datacollectionName=datacollectionName
                                       )
		result = datacollection.deleteDatacollection()
		if result in list(responseMsg.project_Error.values()):
			return make_response(json.jsonify({'error':result}),404)
		if result in list(responseMsg.datacollection_Error.values()):
			return make_response(json.jsonify({'error':result}),404)
		else: return make_response(json.jsonify({'msg':result}),200)

@datacollection_blueprint.route('/project/<string:projectName>/datacollection/<string:datacollectionName>',methods=['GET'])
def getDatacollection(projectName,datacollectionName):
	token = parse.parse_qs(parse.urlparse(request.url).query)['token'][0]
	payload = verifyToken(token)
	if (type(payload)is not dict):
		return make_response(payload)
	else:
		account = payload['sub']
	datacollection = Datacollection(projectOwner = account,
                                        projectName = projectName,
                                        datacollectionName=datacollectionName
                                       )
	result = datacollection.getDatacollection()
	if result in list(responseMsg.project_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	if result in list(responseMsg.datacollection_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	else: return make_response(result,200)

@datacollection_blueprint.route('/project/<string:projectName>/datacollection',methods=['GET'])
def getAllDatacollections(projectName):
	token = parse.parse_qs(parse.urlparse(request.url).query)['token'][0]
	payload = verifyToken(token)
	if (type(payload)is not dict):
		return make_response(payload)
	else:
		account = payload['sub']
	result = Datacollection.getAllDatacollections(projectOwner =account,
                                                      projectName = projectName,
                                                     )
	if result in list(responseMsg.project_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	if result in list(responseMsg.datacollection_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	else: return make_response(result,200)

