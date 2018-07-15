from .. import db
from ..returnMsg import responseMsg
from bson.json_util import dumps
import time
from bson import Code

class Project():
	def __init__(self,projectName=None,projectOwner=None):
		self.projectName = projectName
		self.projectOwner =projectOwner
		self.project_schema = {
                  'projectName':projectName,
                  'situations':[],
                  'createTime':'',
                  'lastEditTime':''
                 }

	@staticmethod
	def isProjectExist(projectArray,projectName):
		for item in projectArray:
			if (projectName==item['projectName']):
				return True
		return False
	def createProject(self):
		result = Project.verifyProject(projectOwner = self.projectOwner,projectName = self.projectName)     
		if (type(result) is int):
			return result
		else:
			self.project_schema['createTime']= time.strftime("%c")
			db.accountCollection.update({'profile.account':self.projectOwner},{'$push':{'projects':self.project_schema}},upsert=True) 
			return responseMsg.project['msg1']
	def deleteProject(self):
		result = Project.verifyProject(projectOwner = self.projectOwner,projectName = self.projectName)
		if(type(result) is int):
			path = 'projects.'+str(result)
			db.accountCollection.update({'profile.account':self.projectOwner},{'$unset':{path:'null'}})
			db.accountCollection.update({'profile.account':self.projectOwner},{'$pull':{'projects':None}})
			return responseMsg.project['msg2']
		else: return result
	def getProject(self):
		result = Project.verifyProject(projectOwner = self.projectOwner,projectName = self.projectName)
		if(type(result) is int):
			path = 'projects.'+str(result)
			project = db.accountCollection.find({'profile.account':self.projectOwner},{'projects':1})[0]['projects'][result]
			return dumps(project)
		else : return result

	@staticmethod	
	def getAllProjects(account):
		result = Project.verifyProject(projectOwner = account)
		if(type(result) is list):
			projectList = []
			for item in result:
				projectList.append(item['projectName'])
			return dumps(projectList)
		else: return result		

	def editProject(self):
		array_index = 0;
		obj = db.accountCollection.find({'profile.account':self.projectOwner})	
		obj = obj[0]['projects']
		i = -1
		for index in obj:
			i+=1
			if index['projectName']=='tomcat':
				array_index = i
		temp = 'projects.'+str(array_index)+'.projectName'
		db.accountCollection.update({'profile.account':self.projectOwner},{'$set':{temp:'tomt'}})
		obj = db.accountCollection.find({'profile.account':self.owner})
		return dumps(obj[0]['projects'])
	
	@staticmethod
	def isProjectsEmpty(userAccount): 
		obj = db.accountCollection.find({'profile.account':userAccount},{'projects':1})
		projectArray = obj[0]['projects']
		if (len(projectArray)==0):
			return True
		else: return False
	@staticmethod
	def getProjectIndex(projectArray,projectName):
		i = -1
		for item in projectArray:
			i+=1
			if (projectName==item['projectName']):
				return i
		return -1
	@staticmethod
	def verifyProject(projectArray=None,projectOwner=None,projectName=None):#verify if project exist
		if projectArray is None:
			obj = db.accountCollection.find({'profile.account':projectOwner},{'projects':1})
			projectArray = obj[0]['projects']
		else:
			projectArray = projectArray
		if (len(projectArray)==0): return responseMsg.project_Error['msg1']
		if projectName is None:
			return projectArray
		else:
			if not Project.isProjectExist(projectArray,projectName): return responseMsg.project_Error['msg3']
			else : return Project.getProjectIndex(projectArray,projectName)
			
