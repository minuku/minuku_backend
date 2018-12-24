from .. import db
from ..returnMsg import responseMsg
from bson.json_util import dumps
import time
from bson import Code

class Project():
	def __init__(self,projectName=None,projectOwner=None,requestBody=None):
		self.projectName = projectName
		self.projectOwner =projectOwner
		self.requestBody=requestBody
		self.project_schema = {
                  'projectName':projectName,
                  'situations':[],
                  'createTime':'',
                  'lastEditTime':'',
				  'dataCollections':[],
				  'questionnaires':[]
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
			#return responseMsg.project_Error['msg2']
			return "project already exist"
			#return "yes"
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

	def android_getProject(self):
		result = Project.verifyProject(projectOwner = self.projectOwner,projectName = self.projectName)
		if(type(result)is int):
			path = 'projects.'+str(result)
			project = db.accountCollection.find({'profile.account':self.projectOwner},{'projects':1})[0]['projects'][result]
			project = Project.dealwithProject(project)
			return dumps(project)
		else : return result
	@staticmethod
	def dealwithProject(project):
		for key in list(project.keys()):
			if project[key] == "" or len(project[key])==0:
				del project[key]
			elif key=='dataCollections':
				i = 0
				while(i<len(project['dataCollections'])):
					for key in list(project['dataCollections'][i].keys()):
						if project['dataCollections'][i][key] =="" or len(project['dataCollections'][i][key])==0:
							del project['dataCollections'][i][key]
					i+=1	

			elif key=="situations":
				i = 0		
				while(i< len(project['situations'])):
					for key in list(project['situations'][i].keys()):
						if project['situations'][i][key]=="" or len(project['situations'][i][key])==0:
							del project['situations'][i][key]
						elif key=='conditions':
							j = 0
							while(j<len(project['situations'][i]['conditions'])):
								for key in list(project['situations'][i]['conditions'][j].keys()):
									if project['situations'][i]['conditions'][j][key]=="" or len(project['situations'][i]['conditions'][j][key])==0:
										del project['situations'][i]['conditions'][j][key]
								j+=1
					i+=1
		return project

	def editProject(self):
		result = Project.verifyProject(projectOwner = self.projectOwner,projectName = self.projectName)
		if(type(result) is int):
			path = 'projects.'+str(result)
			oldProjectName = self.projectName
			newProjectName = self.requestBody['newProjectName']
			temp = 'projects.'+str(result)+'.projectName'
			db.accountCollection.update({'profile.account':self.projectOwner},{'$set':{temp:newProjectName,'projects.'+str(result)+'.lastEditTime':time.strftime("%c")}})
			return "project edit success"
		else : return result
	
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
			
