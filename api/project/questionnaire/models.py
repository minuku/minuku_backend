import sys
sys.path.append('~/minuku/api')

from api.returnMsg import responseMsg
from api import db
import time
from bson.json_util import dumps
from ..models import Project

class Questionnaire():
	def __init__(self,projectOwner=None,projectName=None,questionnaireName=None,questionnaireType=None,questionnaireContent=None):
		self.projectOwner = projectOwner
		self.projectName = projectName
		self.questionnaireName = questionnaireName
		self.questionnaireType = questionnaireType
		self.questionnaireContent = questionnaireContent
		self.questionnaire_schema = {'questionnaireName':questionnaireName,
                                              'questionnaireType':questionnaireType,
											  'questionnaireContent':questionnaireContent,
                                              'createTime':'',
                                              'lastEdittime':''
                                             }
	def createQuestionnaire(self):		
		result = Questionnaire.verifyQuestionnaire(projectOwner = self.projectOwner,projectName = self.projectName,questionnaireName=self.questionnaireName)
		if(type(result) is not list):
			return result
		if(type(result) is list and len(result)==2):
			return responseMsg.questionnaire_Error['msg2']
		if(type(result) is list and len(result)==1):
			path = 'projects.'+str(result[0])+'.questionnaires'
			self.questionnaire_schema['createTime']= time.strftime("%c")
			db.accountCollection.update({'profile.account':self.projectOwner},{'$push':{path:self.questionnaire_schema}})
			return responseMsg.questionnaire['msg1']
			
	def deleteQuestionnaire(self):
		result = Questionnaire.verifyQuestionnaire(projectOwner = self.projectOwner,projectName = self.projectName,questionnaireName=self.questionnaireName)
		if(type(result) is not list):
			return result
		if(type(result)is list and len(result)==1):
			return responseMsg.questionnaire_Error['msg3']
		if(type(result)is list and len(result)==2):
			path1 = 'projects.'+str(result[0])+'.questionnaires.'+str(result[1])
			path2 = 'projects.'+str(result[0])+'.questionnaires'
			db.accountCollection.update({'profile.account':self.projectOwner},{'$unset':{path1:'null'}})
			db.accountCollection.update({'profile.account':self.projectOwner},{'$pull':{path2:None}})
			return responseMsg.questionnaire['msg2']

	def getQuestionnaire(self):
		result = Questionnaire.verifyQuestionnaire(projectOwner = self.projectOwner,projectName = self.projectName,questionnaireName=self.questionnaireName)
		if(type(result) is not list):
			return result
		if(type(result)is list and len(result)==1):
			return responseMsg.questionnaire_Error['msg3']
		if(type(result)is list and len(result)==2):
			questionnaire = db.accountCollection.find({'profile.account':self.projectOwner},{'projects':1})[0]['projects'][result[0]]['questionnaires'][result[1]]
			return dumps(questionnaire)

	def getAllQuestionnaires(projectOwner,projectName):
		result =Questionnaire.verifyQuestionnaire(projectOwner=projectOwner,projectName=projectName)
		if(type(result)is list):
			if(type(result[0]) is int):	#datacollectionName is none, so if datacollectionArray exist,'result' must be array with datacollection name, instead 'result'
										#will be a int list with project index at result[0]
				return responseMsg.questionnaire_Error['msg1']
			else:
				questionnaireList = []
				for item in result:
					questionnaireList.append(item['questionnaireName'])
				return dumps(questionnaireList)
		else: return result
	@staticmethod
	def isQuestionnaireExist(questionnaireArray,questionnaireName):
		for item in questionnaireArray:
			if questionnaireName == item['questionnaireName']:
				return True
		return False

	@staticmethod
	def getQuestionnaireIndex(questionnaireArray,questionnaireName):
		i = -1
		for item in questionnaireArray:
			i+=1
			if questionnaireName == item['questionnaireName']:
				return i
		return -1
	@staticmethod
	def verifyQuestionnaire(projectArray=None,projectOwner=None,projectName=None,questionnaireName=None):
		if(projectArray is None):
			obj = db.accountCollection.find({'profile.account':projectOwner},{'projects':1})
			projectArray = obj[0]['projects']
		else: projectArray = projectArray
		result = Project.verifyProject(projectArray=projectArray,projectOwner=projectOwner,projectName=projectName)
		returnList = []
		if(type(result) is int):
			returnList.append(result)
			questionnaireArray = projectArray[returnList[0]]['questionnaires']
			if(len(questionnaireArray)==0): return returnList
			else:
				if questionnaireName is None:
					return questionnaireArray
				else:
					if not Questionnaire.isQuestionnaireExist(questionnaireArray,questionnaireName): return returnList
					else:
						QuestionnaireIndex = Questionnaire.getQuestionnaireIndex(questionnaireArray,questionnaireName)
						returnList.append(QuestionnaireIndex)
						return returnList
		else: return result
