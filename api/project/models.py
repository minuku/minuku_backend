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
                  'situations':[
                               	#{   'situationName':''
                                #    'schedules':[],
                                #    'datacollections':[],
                                #    'conditions':[]
                                #}
                               ],
                  'createTime':time.strftime("%c"),
                  'lastEditTime':''
                 }

	@staticmethod
	def isProjectExist(projectArray,projectName):
		for item in projectArray:
			if (projectName==item['projectName']):
				return True
		return False
	def createProject(self):
		obj = db.accountCollection.find({'profile.account':self.projectOwner},{'projects':1})
		projectArray = obj[0]['projects']
		if(Project.isProjectExist(projectArray,self.projectName)):
			return responseMsg.project_Error['msg2']
		else:
			projectArray.append(self.project_schema)
			db.accountCollection.update({'profile.account':self.projectOwner},\
                                          {'$push':{'projects':self.project_schema}},upsert=True)
			#return dumps(self.project_schema)
			return responseMsg.project['msg1']                                                                       
	def deleteProject(self):
		#db.accountCollection.find_one_and_update({'profile.account':self.owner},{'$pull':{'projects':{'$eq':self.name}}})
		obj = db.accountCollection.find({'profile.account':self.projectOwner},{'projects':1})
		projectArray = obj[0]['projects']
		if(len(projectArray)==0):
			return responseMsg.project_Error['msg1']
		
		elif not Project.isProjectExist(projectArray,self.projectName):
			return responseMsg.project_Error['msg3']
		else:
			i = -1
			for item in projectArray:
				i+=1
				if(item['projectName']==self.projectName):
					del projectArray[i]
					db.accountCollection.update({'profile.account':self.projectOwner},{'$set':{'projects':projectArray}})
					#return dumps(projectArray)
					return responseMsg.project['msg2']
			return responseMsg.project_Error['msg3']
	def getProject(self):
		obj = db.accountCollection.find({'profile.account':self.projectOwner},{'projects':1})
		projectArray = obj[0]['projects']
		if(len(projectArray)==0):
			return responseMsg.project_Error['msg1']
		else: 
			for item in projectArray:
				if(item['projectName']==self.projectName):
					return dumps(item)
			return responseMsg.project_Error['msg3']
			
	@staticmethod	
	def getAllProjects(account):
		obj = db.accountCollection.find({'profile.account':account},{'projects':1})
		projectArray = obj[0]['projects']
		projectList=[]
		if (len(projectArray)==0): return responseMsg.project_Error['msg1']
		else:  
			for item in projectArray:
				projectList.append(item['projectName'])
			return dumps(projectList)

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
		#db.accountCollection.find({'profile.account':self.owner}).forEach(Code('''function(doc){var index = -1;doc.projects.forEach(function(project){index++;if(project.projectName=='minuku')array_index = index;})}'''))
		#temp = 'projects.'+array_index+'.projectName'
		#db.accountCollection.find({'profile.account':self.owner},{'$set':{temp:'tomcat'}})   
	
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
