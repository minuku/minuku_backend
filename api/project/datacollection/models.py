import sys
sys.path.append('~/minuku/api')

from api import db
import time
from bson.json_util import dumps
from ..models import Project

class Datacollection():
	def __init__(self,projectOwner=None,projectName=None,datacollectionName=None,datacollectionType=None):
		self.projectOwner = projectOwner
		self.projectName = projectName
		self.datacollectionName = datacollectionName
		self.datacollectionType = datacollectionType
		self.datacollection_schema = {'datacollectionName':datacollectionName,
                                              'datacollectionType':datacollectionType,
                                              'createTime':time.strftime("%c"),
                                              'lastUpdatetime':'',
                                              'devices':[]
                                             }
	def createDatacollection(self):
		obj = db.accountCollection.find({'profile.account':self.projectOwner},{'projects':1})
		projectArray = obj[0]['projects']
		if(len(projectArray)==0):
			return 'projectArray empty'
		else:
			if not Project.isProjectExist(projectArray,self.projectName):
				return 'project Not exist'
			else:
				projectIndex = 0
				projectIndex = Project.getProjectIndex(projectArray,self.projectName)
				if projectIndex != -1:
					project = projectArray[projectIndex]
				else: return 'project Not exist'
				datacollectionArray = project['datacollections']
				if not Datacollection.isDatacollectionExist(datacollectionArray,self.datacollectionName):
					datacollectionArray.append(self.datacollection_schema)
				else: return 'datacollection already exist'
				
				update_path = 'projects.'+str(projectIndex)+'.datacollections'
				db.accountCollection.update({'profile.account':self.projectOwner},{'$set':{update_path:datacollectionArray}})
				return dumps(datacollectionArray)

	def deleteDatacollection(self):
		obj = db.accountCollection.find({'profile.account':self.projectOwner},{'projects':1})
		projectArray =  obj[0]['projects']
		if(len(projectArray)==0):
			return 'projectArray empty'
		if not Project.isProjectExist(projectArray,self.projectName):
			return 'project Not exist'
		else:
			projectIndex = Project.getProjectIndex(projectArray,self.projectName)
			if projectIndex != -1:
				project = projectArray[projectIndex]
			else: return 'project Not exist'
			datacollectionArray = project['datacollections']
			if(len(datacollectionArray)==0): return 'datacollectionArray empty'
			if Datacollection.isDatacollectionExist(datacollectionArray,self.datacollectionName):
				datacollectionIndex = Datacollection.getDatacollectionIndex(datacollectionArray,self.datacollectionName)
				del datacollectionArray[datacollectionIndex]
				project['datacollections'] = datacollectionArray
				projectArray[projectIndex] = project
				update_path = 'projects.'+str(projectIndex)+'.datacollections'
				#db.accountCollection.update({'profile.account':self.projectOwner},{'$set':{'projects':projectArray}})
				db.accountCollection.update({'profile.account':self.projectOwner},{'$set':{update_path:datacollectionArray}})
				return dumps(datacollectionArray)
			else: return 'datacollection Not exist'

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
