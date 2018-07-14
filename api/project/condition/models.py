import sys
sys.path.append('~/minuku/api')

from api import db
import time
from bson.json_util import dumps
from ..models import Project


rules=['transpotation',
       'accelerometer',
       'rotation',
       'gravity',
       'gyroscope',
       'light',
       'magnetic',
       'pressure',
       'proximity',
       'temperature',
       'humidity',
       'appUsage',
       'ringer',
       'battery',
       'telephony',
       'connectivity'
       ]
 
class Condition():
	def __init__(self,projectOwner=None,projectName=None,conditionName=None):
		self.projectOwner = projectOwner
		self.projectName = projectName
		self.conditionName = conditionName
		self.condition_schema = {'conditionName':conditionName,
                    'timeStart':'',
                    'timeEnd':'',
                    'timeLasting':'',
                    'timeLasting_unit':'',
                    'rules':rules
                   }

	def createCondition(self):
		obj = db.accountCollection.find({'profile.account':self.projectOwner},{'projects':1})
		projectArray = obj[0]['projects']
		if(len(projectArray)==0):
			return 'projectArray empty'
		#if (Project.isProjectsEmpty(self.projectOwner)):
		#	return 'projects is empty'
		else:
			if not Project.isProjectExist(projectArray,self.projectName):
				return 'project Not exist'
			else:
				i = -1
				projectIndex = 0
				projectIndex = Project.getProjectIndex(projectArray,self.projectName)
				if projectIndex != -1:
					project = projectArray[projectIndex]
				else: return 'project Not exist'
				conditionArray = project['conditions']
				if not Condition.isConditionExist(conditionArray,self.conditionName):
					project['conditions'].append(self.condition_schema)
					conditionArray = project['conditions']
				else: return 'condition already exist'
				projectArray[projectIndex] = project
				db.accountCollection.update({'profile.account':self.projectOwner},{'$set':{'projects':projectArray}})		
				return dumps(self.condition_schema)
	
	def deleteCondition(self):
		obj = db.accountCollection.find({'profile.account':self.projectOwner},{'projects':1})
		projectArray =  obj[0]['projects']
		if(len(projectArray)==0):
			return 'projectArray empty'
		if not Project.isProjectExist(projectArray,self.projectName):
			return 'project Not exist'
		else:
			i = -1
			projectIndex = Project.getProjectIndex(projectArray,self.projectName)
			if projectIndex != -1:
				project = projectArray[projectIndex]
			else: return 'project Not exist'
			conditionArray = project['conditions']
			if(len(conditionArray)==0): return 'conditionArray empty' 
			if Condition.isConditionExist(conditionArray,self.conditionName):
				conditionIndex = Condition.getConditionIndex(conditionArray,self.conditionName)
				del conditionArray[conditionIndex]
				project['conditions'] = conditionArray
				projectArray[projectIndex] = project
				db.accountCollection.update({'profile.account':'jim@test.com'},{'$set':{'projects':projectArray}})
				return dumps(conditionArray)
			else: return 'condition Not exist'
	def getCondition(self):
		obj = db.accountCollection.find({'profile.account':self.projectOwner},{'projects':1})
		projectArray =  obj[0]['projects']
		#assume project and condition must exist
		projectIndex = Project.getProjectIndex(projectArray,self.projectName)
		project = projectArray[projectIndex]
		conditionArray = project['conditions']
		if(Condition.isConditionExist(conditionArray,self.conditionName)):
			conditionIndex = Condition.getConditionIndex(conditionArray,self.conditionName)
			condition = conditionArray[conditionIndex]
			return dumps(condition)
		else: return 'condition Not exist'
	#def editCondition(self):
		
	@staticmethod
	def isConditionExist(conditionArray,conditionName):
		for item in conditionArray:
			if conditionName==item['conditionName']:
				return True
		return False
	@staticmethod
	def getConditionIndex(conditionArray,conditionName):
		i = -1
		for item in conditionArray:
			i+=1
			if conditionName==item['conditionName']:
				return i
		return -1
		
	#def getConditions():
	#def editCondition():
	#def deleteCondition():
