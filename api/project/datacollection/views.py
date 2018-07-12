from . import datacollection_blueprint
from flask import request, make_response,json
from urllib import parse
from bson.json_util import dumps
from .models import Datacollection

@datacollection_blueprint.route('/<string:projectName>/createDatacollection',methods=['POST'])
def createDatacollection(projectName):
	obj = request.get_json()
	datacollection = Datacollection(projectOwner = obj['account'],
                                        projectName = projectName, 
                                        datacollectionName=obj['datacollectionName'],
                                        datacollectionType=obj['datacollectionType'])
	result = datacollection.createDatacollection()
	if result in ['projectArray empty','project Not exist','datacollection already exist']:
		return make_response(json.jsonify({'error':result}),404)
	else: return make_response(result,200)

@datacollection_blueprint.route('/<string:projectName>/deleteDatacollection',methods=['POST'])
def deleteDatacollection(projectName):
	obj = request.get_json()
	datacollection = Datacollection(projectOwner = obj['account'],
                                        projectName = projectName,
                                        datacollectionName=obj['datacollectionName'],
                                        datacollectionType=obj['datacollectionType'])
	result = datacollection.deleteDatacollection()
	if result in ['projectArray empty','project Not exist','datacollection Not exist','datacollectionArray empty']:
		return make_response(json.jsonify({'error':result}),404)
	else: return make_response(result,200)
