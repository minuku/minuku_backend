import sys
sys.path.append('~/minuku/api')

from api.returnMsg import responseMsg
from api import db
import time
from bson.json_util import dumps
from ..models import Project
from ..datacollection.models import Datacollection

class Device():
	def __init__(self,projectOwner=None,projectName=None,situationName = None,datacollectionName = None,deviceName = None,deviceType=None,deviceContent=None):
		self.projectOwner = projectOwner
		self.projectName = projectName
		self.situationName = situationName
		self.datacollectionName = datacollectionName
		self.deviceName = deviceName
		self.deviceType = deviceType
		self.deviceContent = deviceContent
		self.device_schema = {
		                      'deviceName':deviceName,
							  'deviceContent':deviceContent,
							  'createTime':'',
							  'lastEditTime':'',
							  'deviceType':deviceType
							 }


	def createDevice(self):
		result = Device.verifyDevice(projectOwner = self.projectOwner,
		                             projectName = self.projectName,
									 situationName = self.situationName, 
									 datacollectionName = self.datacollectionName,
									 deviceName = self.deviceName
									)
		if(type(result) is not list):
			return result
		if(type(result) is list and len(result)==4):
			return responseMsg.device_Error['msg2']
		if(type(result) is list and len(result)==1):
			return responseMsg.situatino_Error['msg3']
		if(type(result) is list and len(result)==2):
			return responseMsg.datacollection_Error['msg3']
		if(type(result) is list and len(result)==3):
			path = 'projects.'+str(result[0])+'.situations.'+str(result[1])+'.dataCollections.'+str(result[2])+'.devices'
			self.device_schema['createTime']=time.strftime("%c")
			db.accountCollection.update({'profile.account':self.projectOwner},{'$push':{path:self.device_schema}})
			return responseMsg.device['msg1']
	
	def deleteDevice(self):
		result = Device.verifyDevice(projectOwner = self.projectOwner,
		                             projectName = self.projectName,
									 situationName = self.situationName, 
									 datacollectionName = self.datacollectionName,
									 deviceName = self.deviceName
									)
		if(type(result) is not list):
			return result
		if(type(result) is list and len(result)==1):
			return responseMsg.situatino_Error['msg3']
		if(type(result) is list and len(result)==2):
			return responseMsg.datacollection_Error['msg3']
		if(type(result) is list and len(result)==3):
			return responseMsg.device_Error['msg3']
		if(type(result) is list and len(result)==4):
			path1 =  'projects.'+str(result[0])+'.situations.'+str(result[1])+'.dataCollections.'+str(result[2])+'.devices.'+str(result[3])
			path2 = 'projects.'+str(result[0])+'.situations.'+str(result[1])+'.dataCollections.'+str(result[2])+'.devices'
			db.accountCollection.update({'profile.account':self.projectOwner},{'$unset':{path1:'null'}})
			db.accountCollection.update({'profile.account':self.projectOwner},{'$pull':{path2:None}})
			return responseMsg.device['msg2']
	
	def getDevice(self):
		result = Device.verifyDevice(projectOwner = self.projectOwner,
		                             projectName = self.projectName,
									 situationName = self.situationName, 
									 datacollectionName = self.datacollectionName,
									 deviceName = self.deviceName
									)
		if(type(result) is not list):
			return result
		if(type(result) is list and len(result)==1):
			return responseMsg.situatino_Error['msg3']
		if(type(result) is list and len(result)==2):
			return responseMsg.datacollection_Error['msg3']
		if(type(result) is list and len(result)==3):
			return responseMsg.device_Error['msg3']
		if(type(result) is list and len(result)==4):
			device = db.accountCollection.find({'profile.account':self.projectOwner},{'projects':1})[0]['projects'][result[0]]['situations'][result[1]]['dataCollections'][result[2]]['devices'][result[3]]
			return dumps(device)
	
	@staticmethod
	def getAllDevices(projectOwner,projectName,situationName,datacollectionName):
		result = Device.verifyDevice(projectOwner = projectOwner,
		                             projectName = projectName,
									 situationName = situationName, 
									 datacollectionName = datacollectionName 
									)
		if(type(result) is not list):
			return result
		if(type(result)is list):
			if(type(result[0]) is int):
				return responseMsg.device_Error['msg1']
			else:
				#deviceList = []
				#for item in result:
				#	deviceList.append(item['deviceName'])
				#return dumps(deviceList)
				return dumps(result )   #return whole deviceArray
	
	def editDevice(self,newDeviceName=None,newDeviceType=None,newDeviceContent=None):
		result = Device.verifyDevice(projectOwner = self.projectOwner,
		                             projectName = self.projectName,
									 situationName = self.situationName, 
									 datacollectionName = self.datacollectionName,
									 deviceName = self.deviceName
									)
		if(type(result) is not list):
			return result
		if(type(result) is list and len(result)==1):
			return responseMsg.situatino_Error['msg3']
		if(type(result) is list and len(result)==2):
			return responseMsg.datacollection_Error['msg3']
		if(type(result) is list and len(result)==3):
			return responseMsg.device_Error['msg3']
		if(type(result) is list and len(result)==4):
			path = 'projects.'+str(result[0])+'.situations.'+str(result[1])+'.dataCollections.'+str(result[2])+'.devices.'+str(result[3])
			db.accountCollection.update({'profile.account':self.projectOwner},{'$set':{path+'.lastEditTime':time.strftime("%c"),
		    	                                                                       path+'.deviceContent':newDeviceContent,
																					  }})
			return responseMsg.device['msg3']

	@staticmethod
	def isDeviceExist(deviceArray,deviceName):
		for item in deviceArray:
			if(deviceName == item['deviceName']):
				return True
		return False

	@staticmethod
	def getDeviceIndex(deviceArray,deviceName):
		i = -1 
		for item in deviceArray:
			i+=1
			if deviceName == item['deviceName']:
				return i
		return -1

	@staticmethod
	def verifyDevice(projectArray = None,projectOwner=None,projectName = None,situationName = None,datacollectionName=None,deviceName = None):
		if(projectArray is None):
			obj = db.accountCollection.find({'profile.account':projectOwner},{'projects':1})
			projectArray= obj[0]['projects']
		else: projectArray = projectArray
		result = Datacollection.verifyDatacollection(projectArray = projectArray,projectOwner = projectOwner,projectName=projectName,situationName = situationName,datacollectionName = datacollectionName)
		returnList = []
		if(type(result)is list):
			if(len(result)==1): return responseMsg.situation_Error['msg3']
			if(len(result)==2): return responseMsg.datacollection_Error['msg3']
			returnList.extend(result)
			deviceArray = projectArray[returnList[0]]['situations'][returnList[1]]['dataCollections'][returnList[2]]['devices']
			if(len(deviceArray)==0): return returnList
			else:
				if deviceName is None:
					return deviceArray
				else:
					if not Device.isDeviceExist(deviceArray,deviceName): return returnList 
					else: 
						deviceIndex = Device.getDeviceIndex(deviceArray,deviceName)
						returnList.append(deviceIndex)
						return returnList
		else: return  result
