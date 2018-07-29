import sys
sys.path.append('~/minuku/api')

from api.returnMsg import responseMsg
from api import db
import time
from bson.json_util import dumps
from ..models import Project
from ..situation.models import Situation

#rules=['transpotation',
#       'accelerometer',
#      'rotation',
#       'gravity',
#       'gyroscope',
#       'light',
#       'magnetic',
#       'pressure',
#       'proximity',
#       'temperature',
#       'humidity',
#       'appUsage',
#       'ringer',
#       'battery',
#       'telephony',
#       'connectivity'
#       ]
 
class Condition():
	def __init__(self,projectOwner=None,projectName=None,conditionName=None,situationName=None,conditionContent=None):
		self.projectOwner = projectOwner
		self.projectName = projectName
		self.conditionName = conditionName
		self.situationName = situationName
		self.condition_schema = {
                                         'conditionName':conditionName,
                                         #'timeStart':'',
                                         #'timeEnd':'',
                                         #'timeLasting':'',
                                         #'timeLasting_unit':'',
                                         #'rules':,
                                         'createTime':'',
                                         'lastEditTime':'',
										 'conditionContent':conditionContent,
                   }

	def createCondition(self):
		result = Condition.verifyCondition(projectOwner = self.projectOwner,projectName = self.projectName,situationName = self.situationName,conditionName=self.conditionName)
		if(type(result) is not list):
			return result
		if(type(result) is list and len(result)==3):
			return responseMsg.condition_Error['msg2']
		if(type(result) is list and len(result)==1):
			return responseMsg.situation_Error['msg3']
		if(type(result) is list and len(result)==2):
			path = 'projects.'+str(result[0])+'.situations.'+str(result[1])+'.conditions'
			self.condition_schema['createTime']= time.strftime("%c")
			db.accountCollection.update({'profile.account':self.projectOwner},{'$push':{path:self.condition_schema}})
			return responseMsg.condition['msg1']

	def deleteCondition(self):
		result = Condition.verifyCondition(projectOwner = self.projectOwner,projectName = self.projectName,situationName = self.situationName,conditionName=self.conditionName)
		if(type(result) is not list):
			return result
		if(type(result)is list and len(result)==1):
			return responseMsg.situation_Error['msg3'] #means situation must not exist, but unsure situation array is empty 
		if(type(result)is list and len(result)==2): #means condition must not exist, but unsure condition array is empty
			return responseMsg.condition_Error['msg3']
		if(type(result)is list and len(result)==3): # means condition is exist
			path1 = 'projects.'+str(result[0])+'.situations.'+str(result[1])+'.conditions.'+str(result[2])
			path2 = 'projects.'+str(result[0])+'.situations.'+str(result[1])+'.conditions'
			db.accountCollection.update({'profile.account':self.projectOwner},{'$unset':{path1:'null'}})
			db.accountCollection.update({'profile.account':self.projectOwner},{'$pull':{path2:None}})
			return responseMsg.condition['msg2']

	def getCondition(self):
		result = Condition.verifyCondition(projectOwner=self.projectOwner,projectName = self.projectName,situationName=self.situationName,conditionName = self.conditionName)
		if(type(result) is not list ):
			return result
		if(type(result)is list and len(result)==1):
			return responseMsg.situation_Error['msg3']
		if(type(result)is list and len(result)==2):
			return responseMsg.condition_Error['msg3']	
		if(type(result)is list and len(result)==3):
			condition = db.accountCollection.find({'profile.account':self.projectOwner},{'projects':1})[0]['projects'][result[0]]['situations'][result[1]]['conditions'][result[2]]
			return dumps(condition)
	@staticmethod
	def getAllConditions(projectOwner,projectName,situationName):
		result = Condition.verifyCondition(projectOwner = projectOwner,projectName=projectName,situationName=situationName)
		if(type(result)is list):
			if(type(result[0]) is int):
				return responseMsg.condition_Error['msg1']
			else:
				#conditionList = []
				#for item in result:
				#	conditionList.append(item['conditionName'])
				#return dumps(conditionList)
				return dumps(result)
	
	def editCondition(self,newConditionName=None,newConditionContent=None):
		result = Condition.verifyCondition(projectOwner=self.projectOwner,projectName = self.projectName,situationName=self.situationName,conditionName = self.conditionName)
		if(type(result) is not list ):
			return result
		if(type(result)is list and len(result)==1):
			return responseMsg.situation_Error['msg3']
		if(type(result)is list and len(result)==2):
			return responseMsg.condition_Error['msg3']	
		if(type(result)is list and len(result)==3):
			path = 'projects.'+str(result[0])+'.situations.'+ str(result[1])+'.conditions.'+str(result[2])
			db.accountCollection.update({'profile.account':self.projectOwner},{'$set':{
			                                                                           path+'.lastEditTime':time.strftime("%c"),
																					   path+'.conditionContent':newConditionContent,
																					   path+'.conditionName':newConditionName
																					  }})


			return responseMsg.condition['msg3']


	@staticmethod
	def isConditionExist(conditionArray,conditionName):
		for item in conditionArray:
			if (conditionName==item['conditionName']):
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
	@staticmethod
	def verifyCondition(projectArray=None,projectOwner=None,projectName=None,situationName=None,conditionName=None):
		if(projectArray is None):
			obj = db.accountCollection.find({'profile.account':projectOwner},{'projects':1})
			projectArray = obj[0]['projects']
		else: projectArray = projectArray
		result = Situation.verifySituation(projectArray=projectArray,projectOwner=projectOwner,projectName=projectName,situationName=situationName)
		returnList = []
		if(type(result) is list):
			if(len(result)==1): return responseMsg.situation_Error['msg3']
			returnList.extend(result)
			conditionArray = projectArray[returnList[0]]['situations'][returnList[1]]['conditions']
			if(len(conditionArray)==0): return returnList 
			else:
				if conditionName is None:
					return conditionArray
				else: 
					if not Condition.isConditionExist(conditionArray,conditionName): return returnList
					else:
						conditionIndex = Condition.getConditionIndex(conditionArray,conditionName)
						returnList.append(conditionIndex)
						return returnList
		else: return result
