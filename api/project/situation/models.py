import sys
sys.path.append('~/minuku/api')
from api import db
from api.returnMsg import responseMsg
from bson.json_util import dumps
import time
from bson import Code
from ..models import Project


class Situation():
	def __init__(self,projectOwner=None,projectName=None,situationName=None):
		self.projectOwner = projectOwner
		self.projectName = projectName
		self.situationName = situationName
		self.situation_schema = {'situationName':situationName,
                                         'createTime':"",
                                         'lastEditTime':'',
                                         'conditions':[],
                                         'dataCollections':[]
                                        }
	@staticmethod
	def isSituationExist(situationArray,situationName):
		for item in situationArray:
			if (situationName==item['situationName']):
				return True
		return False
	def createSituation(self):
		#obj = db.accountCollection.find({'profile.account':self.projectOwner},{'projects':1})
		#projectArray = obj[0]['projects']
		#if(len(projectArray)==0):
		#	return returnErrorMsg.project_Error['msg1']
		#else:
		#	if not Project.isProjectExist(projectArray,self.projectName):
		#		return responseMsg.project_Error['msg3']
		#	else :
		#		projectIndex = Project.getProjectIndex(projectArray,self.projectName)
		#		if projectIndex != -1:
		#			project = projectArray[projectIndex]
		#		else:return responseMsg.project_Error['msg3']
		#		situationArray = project['situations']
		#		if not Situation.isSituationExist(situationArray,self.situationName):
					#project.['situations'].append(self.situation_schema)
		#			path = 'projects.'+str(projectIndex)+'.situations'
		#			db.accountCollection.update({'profile.account':self.projectOwner},{'$push':{path:self.situation_schema}})
		#			return responseMsg.situation['msg1']
		#		else : return responseMsg.situation_Error['msg2']
		result = Situation.verifySituation(projectOwner = self.projectOwner,projectName = self.projectName,situationName = self.situationName)
		if(type(result) is not list):#means project or situation not exist
			return result
		if(type(result)is list and len(result)==2):
			return responseMsg.situation_Error['msg2']
		if(type(result)is list and len(result)==1): 
			path ='projects.'+str( result[0])+'.situations' # 0 is projectIndex
			self.situation_schema['createTime'] = time.strftime("%c")
			db.accountCollection.update({'profile.account':self.projectOwner},{'$push':{path:self.situation_schema}})
			return responseMsg.situation['msg1']

	def deleteSituation(self):
		#obj = db.accountCollection.find({'profile.account':self.projectOwner},{'projects':1})
		#projectArray = obj[0]['projects']
		#if(len(projectArray)==0):
		#	return returnErrorMsg.project_Error['msg1']
		#else:
		#	if not Project.isProjectExist(projectArray,self.projectName):			
		#		return responseMsg.project_Error['msg3']
		#	else: 
		#		projectIndex = Project.getProjectIndex(projectArray,self.projectName)
		#		if projectIndex != -1:
		#			project = projectArray[projectIndex]
		#		else:return responseMsg.project_Error['msg3']
		#		situationArray = project['situations']
		#		if(len(situationArray)==0):
		#			return responseMsg.situation_Error['msg1']
		#		else:
		#			if Situation.isSituationExist(situationArray,self.situationName):
		#				situationIndex = Situation.getSituationIndex(situationArray,self.situationName)
		#				del situationArray[situationIndex]
		#				path = 'projects.'+str(projectIndex)+'.situations'
		#				db.accountCollection.update({'profile.account':self.projectOwner},{'$set':{path:situationArray}})
		#				return responseMsg.situation['msg2']
		#			else : return responseMsg.situation_Error['msg3']
	
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
		#obj = db.accountCollection.find({'profile.account':self.projectOwner},{'projects':1})
		#projectArray = obj[0]['projects']
		#if(len(projectArray)==0):
		#	return responseMsg.project_Error['msg1']
		#else:
		#	projectIndex = Project.getProjectIndex(projectArray,self.projectName)
		#	situationArray = projectArray[projectIndex]['situations']
		#	if(len(situationArray)==0):
		#		return responseMsg.situation_Error['msg1']
		#	else:
		#		situationIndex = Situation.getSituationIndex(situationArray,self.situationName)
		#		return dumps(situationArray[situationIndex])
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
		#obj = db.accountCollection.find({'profile.account':projectOwner},{'projects':1})
		#projectArray = obj[0]['projects']
		#assume project situation are exist
		#projectIndex = Project.getProjectIndex(projectArray,projectName)
		#situationArray = projectArray[projectIndex]['situations']
		#if(len(situationArray)==0): return responseMsg.situation_Error['msg1']
		#else:
		#	situationList =[]
		#	for item in situationArray:
		#		situationList.append(item['situationName'])
		#	return dumps(situationList)
		result = Situation.verifySituation(projectOwner = projectOwner,projectName = projectName)
		if(type(result) is not list ):
			return result
		if(type(result)is list):
			if(type(result[0]) is int):
				return responseMsg.situation_Error['msg1']
			else:
				situationList = []
				for item in result:
					situationList.append(item['situationName'])
				return dumps(situationList)
	
	@staticmethod
	def getSituationIndex(situationArray,situationName):
		i = -1
		for item in situationArray:
			i +=1
			if(situationName==item['situationName']):
				return i
		return -1

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
