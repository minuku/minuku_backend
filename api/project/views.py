from .. import db
from . import project_blueprint
from flask import request, make_response,json
from urllib import parse
from bson.json_util import dumps
from .models import Project

@project_blueprint.route('/createProject',methods=['POST'])
def createProject():
	obj = request.get_json()
	project = Project(projectName=obj['projectName'],projectOwner=obj['account'])
	result = project.createProject()
	if result in ['project already exist']:
		return make_response(json.jsonify({'error':result}),404)
	else:
		return make_response(result,200)

@project_blueprint.route('/deleteProject',methods=['POST'])
def deleteProject():
	obj = request.get_json()
	project = Project(projectName=obj['projectName'],projectOwner=obj['account'])
	result = project.deleteProject()
	
	if result in ['project Not exist','projectArray empty','project Not exist']:
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
