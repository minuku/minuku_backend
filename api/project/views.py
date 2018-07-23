from .. import db
from ..returnMsg import responseMsg
from . import project_blueprint
from flask import request, make_response,json
from urllib import parse
from bson.json_util import dumps
from .models import Project

@project_blueprint.route('/project',methods=['POST'])
def createProject():
	obj = request.get_json()
	project = Project(projectName=obj['projectName'],projectOwner=obj['account'])
	result = project.createProject()
	if result in list(responseMsg.project_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	else:
		return make_response(json.jsonify({'msg':result}),200)


@project_blueprint.route('/project',methods=['GET'])
def getAllProjects():
	account = parse.parse_qs(parse.urlparse(request.url).query)['account'][0]
	result = Project.getAllProjects(account)
	if result in list(responseMsg.project_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	else:
		return make_response(result,200)

@project_blueprint.route('/project/<string:projectName>',methods=['DELETE'])
def deleteProject(projectName):
	obj = request.get_json()
	project = Project(projectName=projectName,projectOwner=obj['account'])
	result = project.deleteProject()
	if result in list(responseMsg.project_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	else:
		return make_response(json.jsonify({'msg':result}),200)
@project_blueprint.route('/project/<string:projectName>',methods=['GET'])
def getProject(projectName):
	account = parse.parse_qs(parse.urlparse(request.url).query)['account'][0]
	project = Project(projectOwner = account,projectName = projectName)
	result = project.getProject()
	if result in list(responseMsg.project_Error.values()):
		return make_response(json.jsonify({'error':result}),404)
	else:
		return make_response(result,200)

@project_blueprint.route('/editProject',methods=['POST'])
def editProject():
	obj = request.get_json()
	project = Project(projectName=obj['projectName'],projectOwner=obj['account'])
	#project.editProject()
	#return make_response({},200)
	return make_response(project.editProject(),200)
