import sys
sys.path.append('~/minuku/api')
from api import db
from api.returnMsg import responseMsg
from bson.json_util import dumps
import time
from bson import Code
from ..models import Project


class Situation():
	def __init__(self,projectOwner=None,projectName=None,situationName=None,requestBody=None):
		self.projectOwner = projectOwner
		self.projectName = projectName
		self.situationName = situationName
		self.requestBody=requestBody
		self.situation_schema = {'situationName':situationName,
                                         'createTime':"",
                                         'lastEditTime':'',
                                         'conditions':[],
                                        }
	@staticmethod
	def isSituationExist(situationArray,situationName):
		for item in situationArray:
			if (situationName==item['situationName']):
				return True
		return False
	def createSituation(self):
		result = Situation.verifySituation(projectOwner = self.projectOwner,projectName = self.projectName,situationName = self.situationName)
		if(type(result) is not list):#means project or situation not exist
			return result
		if(type(result)is list and len(result)==2):
			return responseMsg.situation_Error['msg2']
		if(type(result)is list and len(result)==1): 
			path ='projects.'+str( result[0])+'.situations' # result[0] is projectIndex
			self.situation_schema['createTime'] = time.strftime("%c")
			db.accountCollection.update({'profile.account':self.projectOwner},{'$push':{path:self.situation_schema}})
			return responseMsg.situation['msg1']

	def deleteSituation(self):
		result = Situation.verifySituation(projectOwner = self.projectOwner,projectName = self.projectName,situationName = self.situationName)
		if(type(result) is not list ):
			return result
		if(type(result)is list and len(result)==1):
			return responseMsg.situation_Error['msg3']
		if(type(result)is list and len(result)==2):
			path1 = 'projects.'+str(result[0])+'.situations.'+str(result[1])
			path2 = 'projects.'+str(result[0])+'.situations'
			db.accountCollection.update({'profile.account':self.projectOwner},{'$unset':{path1:'null'}})
			db.accountCollection.update({'profile.account':self.projectOwner},{'$pull':{path2:None}})
			return responseMsg.situation['msg2']
				

	def getSituation(self):
		result = Situation.verifySituation(projectOwner = self.projectOwner,projectName = self.projectName,situationName = self.situationName)
		if(type(result) is not list ):
			return result
		if(type(result)is list and len(result)==1):
			return responseMsg.situation_Error['msg3']
		if(type(result)is list and len(result)==2):
			situation = db.accountCollection.find({'profile.account':self.projectOwner},{'projects':1})[0]['projects'][result[0]]['situations'][result[1]]
			return dumps(situation)
			
	@staticmethod
	def getAllSituations(projectOwner,projectName):
		result = Situation.verifySituation(projectOwner = projectOwner,projectName = projectName)
		if(type(result)is list):
			if(type(result[0]) is int):
				return responseMsg.situation_Error['msg1']
			else:
				situationList = []
				for item in result:
					situationList.append(item['situationName'])
				return dumps(situationList)
		else: return result
		
	@staticmethod
	def getSituationIndex(situationArray,situationName):
		i = -1
		for item in situationArray:
			i +=1
			if(situationName==item['situationName']):
				return i
		return -1
	def editSituation(self):
		result = Situation.verifySituation(projectOwner = self.projectOwner,projectName = self.projectName,situationName = self.situationName)
		if(type(result) is not list ):
			return result
		if(type(result)is list and len(result)==1):
			return responseMsg.situation_Error['msg3']
		if(type(result)is list and len(result)==2):
			path1 = 'projects.'+str(result[0])+'.situations.'+str(result[1])
			path2 = 'projects.'+str(result[0])+'.situations'
			oldSituationName = self.situationName
			newSituationName = self.requestBody['newSituationName']
			db.accountCollection.update({'profile.account':self.projectOwner},{'$set':{path1+'.situationName':newSituationName,path1+'.lastEditTime':time.strftime("%c")}})
			return responseMsg.situation['msg3']

	@staticmethod
	def verifySituation(projectArray=None,projectOwner=None,projectName=None,situationName=None):
		if projectArray is None:
			obj = db.accountCollection.find({'profile.account':projectOwner},{'projects':1})
			projectArray = obj[0]['projects']
		else: projectArray = projectArray
		
		result = Project.verifyProject(projectArray,projectOwner,projectName)
		returnList = []
		if(type(result) is int):
			projectIndex = result
			returnList.append(projectIndex)
			situationArray = projectArray[projectIndex]['situations']
			if (len(situationArray)==0): return returnList
			else:
				if situationName is None:
					return situationArray
				else:
					if not Situation.isSituationExist(situationArray,situationName): return returnList
					else:
						situationIndex = Situation.getSituationIndex(situationArray,situationName)
						returnList.append(situationIndex)
						return returnList
		else: return result
