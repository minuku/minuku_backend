import sys
sys.path.append('~/minuku/api')
from api.returnMsg import responseMsg
from . import device_blueprint
from flask import request, make_response ,json
from urllib import parse
from bson.json_util import dumps
from .models import Device
from api.auth.views import verifyToken

@device_blueprint.route('/project/<string:projectName>/situation/<string:situationName>/datacollection/<string:datacollectionName>/device',methods=['POST'])
def createDevice(projectName,situationName,datacollectionName):
	token = parse.parse_qs(parse.urlparse(request.url).query)['token'][0]
	payload = verifyToken(token)
	if(type(payload)is not dict):
		return make_response(payload)
	else:
		account = payload['sub']
		obj = request.get_json()
		device = Device(projectOwner = account,
		                projectName =  projectName,
						situationName = situationName,
						datacollectionName = datacollectionName,
						deviceName = obj['deviceName'],
						deviceType = obj['deviceType'],
						deviceContent = obj['deviceContent']
					   )
		result = device.createDevice()
		return printResult(result)

@device_blueprint.route('/project/<string:projectName>/situation/<string:situationName>/datacollection/<string:datacollectionName>/device/<string:deviceName>',methods=['DELETE'])
def deleteDevice(projectName,situationName,datacollectionName,deviceName):
	token = parse.parse_qs(parse.urlparse(request.url).query)['token'][0]
	payload = verifyToken(token)
	if(type(payload) is not dict):
		return make_response(payload)
	else:
		account = payload['sub']
		device = Device(projectOwner = account,
		                projectName =  projectName,
						situationName = situationName,
						datacollectionName = datacollectionName,
						deviceName = deviceName
					   )
		result = device.deleteDevice()
		return printResult(result)

@device_blueprint.route('/project/<string:projectName>/situation/<string:situationName>/datacollection/<string:datacollectionName>/device/<string:deviceName>',methods=['GET'])
def getDevice(projectName,situationName,datacollectionName,deviceName):
	token = parse.parse_qs(parse.urlparse(request.url).query)['token'][0]
	payload = verifyToken(token)
	if(type(payload) is not dict):
		return make_response(payload)
	else:
		account = payload['sub']
		device = Device(projectOwner = account,
		                projectName =  projectName,
						situationName = situationName,
						datacollectionName = datacollectionName,
						deviceName = deviceName
					   )
		result = device.getDevice()
		if result in list(responseMsg.project_Error.values()):
			return make_response(json.jsonify({'error':result}),404)
		if result in list(responseMsg.situation_Error.values()):
			return make_response(json.jsonify({'error':result}),404)
		if result in list(responseMsg.datacollection_Error.values()):
			return make_response(json.jsonify({'error':result}),404)
		if result in list(responseMsg.device_Error.values()):
			return make_response(json.jsonify({'error':result}),404)
		else:
			return result
@device_blueprint.route('/project/<string:projectName>/situation/<string:situationName>/datacollection/<string:datacollectionName>/device',methods=['GET'])
def getAllDevices(projectName,situationName,datacollectionName):
	token = parse.parse_qs(parse.urlparse(request.url).query)['token'][0]
	payload = verifyToken(token)
	if(type(payload) is not dict):
		return make_response(payload)
	else:
		account = payload['sub']
	obj = request.get_json()
	result = Device.getAllDevices(projectOwner = account,
		                projectName =  projectName,
						situationName = situationName,
						datacollectionName = datacollectionName)
	if result in list(responseMsg.project_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	if result in list(responseMsg.situation_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	if result in list(responseMsg.datacollection_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	if result in list(responseMsg.device_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	else:
		return result

@device_blueprint.route('/project/<string:projectName>/situation/<string:situationName>/datacollection/<string:datacollectionName>/device/<string:deviceName>',methods=['PUT'])
def editDevice(projectName,situationName,datacollectionName,deviceName):
	token = parse.parse_qs(parse.urlparse(request.url).query)['token'][0]
	payload = verifyToken(token)
	if(type(payload) is not dict):
		return make_response(payload)
	else:
		account = payload['sub']
		obj = request.get_json()
		device = Device(projectOwner = account,
		                projectName =  projectName,
						situationName = situationName,
						datacollectionName = datacollectionName,
						deviceName = deviceName,
					   )
		result = device.editDevice(newDeviceContent=obj['deviceContent'])
		return printResult(result)
	

def printResult(result):
	if result in list(responseMsg.project_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	if result in list(responseMsg.situation_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	if result in list(responseMsg.datacollection_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	if result in list(responseMsg.device_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	else: return make_response(json.jsonify({'msg':result}),200)
