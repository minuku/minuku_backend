import sys
sys.path.append('~/minuku/api')

from api.returnMsg import responseMsg
from api import db
import time
from bson.json_util import dumps
from ..models import Project
from ..situation.models import Situation

class Datacollection():
	def __init__(self,projectOwner=None,projectName=None,datacollectionName=None,datacollectionType=None):
		self.projectOwner = projectOwner
		self.projectName = projectName
		self.datacollectionName = datacollectionName
		self.datacollectionType = datacollectionType
		self.datacollection_schema = {'datacollectionName':datacollectionName,
                                              'datacollectionType':datacollectionType,
                                              'createTime':'',
                                              'lastEdittime':'',
                                              'devices':[]
                                             }
	def createDatacollection(self):		
		result = Datacollection.verifyDatacollection(projectOwner = self.projectOwner,projectName = self.projectName,datacollectionName=self.datacollectionName)
		if(type(result) is not list):
			return result
		if(type(result) is list and len(result)==2):
			return responseMsg.datacollection_Error['msg2']
		if(type(result) is list and len(result)==1):
			path = 'projects.'+str(result[0])+'.dataCollections'
			self.datacollection_schema['createTime']= time.strftime("%c")
			db.accountCollection.update({'profile.account':self.projectOwner},{'$push':{path:self.datacollection_schema}})
			return responseMsg.datacollection['msg1']
			
	def deleteDatacollection(self):
		result = Datacollection.verifyDatacollection(projectOwner = self.projectOwner,projectName = self.projectName,datacollectionName=self.datacollectionName)
		if(type(result) is not list):
			return result
		if(type(result)is list and len(result)==1):
			return responseMsg.datacollection_Error['msg3']
		if(type(result)is list and len(result)==2):
			path1 = 'projects.'+str(result[0])+'.dataCollections.'+str(result[1])
			path2 = 'projects.'+str(result[0])+'.dataCollections'
			db.accountCollection.update({'profile.account':self.projectOwner},{'$unset':{path1:'null'}})
			db.accountCollection.update({'profile.account':self.projectOwner},{'$pull':{path2:None}})
			return responseMsg.datacollection['msg2']

	def getDatacollection(self):
		result = Datacollection.verifyDatacollection(projectOwner = self.projectOwner,projectName = self.projectName,datacollectionName=self.datacollectionName)
		if(type(result) is not list):
			return result
		if(type(result)is list and len(result)==1):
			return responseMsg.datacollection_Error['msg3']
		if(type(result)is list and len(result)==2):
			datacollection = db.accountCollection.find({'profile.account':self.projectOwner},{'projects':1})[0]['projects'][result[0]]['dataCollections'][result[1]]
			return dumps(datacollection)

	def getAllDatacollections(projectOwner,projectName):
		result =Datacollection.verifyDatacollection(projectOwner=projectOwner,projectName=projectName)
		if(type(result)is list):
			if(type(result[0]) is int):	#datacollectionName is none, so if datacollectionArray exist,'result' must be array with datacollection name, instead 'result'
										#will be a int list with project index at result[0]
				return responseMsg.datacollection_Error['msg1']
			else:
				datacollectionList = []
				for item in result:
					datacollectionList.append(item['datacollectionName'])
				return dumps(datacollectionList)
		else: return result
	@staticmethod
	def isDatacollectionExist(datacollectionArray,datacollectionName):
		for item in datacollectionArray:
			if datacollectionName == item['datacollectionName']:
				return True
		return False

	@staticmethod
	def getDatacollectionIndex(datacollectionArray,datacollectionName):
		i = -1
		for item in datacollectionArray:
			i+=1
			if datacollectionName == item['datacollectionName']:
				return i
		return -1
	@staticmethod
	def verifyDatacollection(projectArray=None,projectOwner=None,projectName=None,datacollectionName=None):
		if(projectArray is None):
			obj = db.accountCollection.find({'profile.account':projectOwner},{'projects':1})
			projectArray = obj[0]['projects']
		else: projectArray = projectArray
		result = Project.verifyProject(projectArray=projectArray,projectOwner=projectOwner,projectName=projectName)
		returnList = []
		if(type(result) is int):
			returnList.append(result)
			datacollectionArray = projectArray[returnList[0]]['dataCollections']
			if(len(datacollectionArray)==0): return returnList
			else:
				if datacollectionName is None:
					return datacollectionArray
				else:
					if not Datacollection.isDatacollectionExist(datacollectionArray,datacollectionName): return returnList
					else:
						DatacollectionIndex = Datacollection.getDatacollectionIndex(datacollectionArray,datacollectionName)
						returnList.append(DatacollectionIndex)
						return returnList
		else: return result
