from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient, InsertOne, DeleteOne,ReplaceOne
from pymongo.collection import Collection

db = MongoClient('localhost',27017).minukuTestDB

def create_app():
	app = Flask(__name__)
	CORS(app)
	from .auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint)
	from .user import user_blueprint
	app.register_blueprint(user_blueprint)
	#from .user.test import user_testblueprint
	#app.register_blueprint(user_testblueprint)	
	from .project import project_blueprint
	app.register_blueprint(project_blueprint)
	from .project.situation import situation_blueprint
	app.register_blueprint(situation_blueprint)
	from .project.condition import condition_blueprint
	app.register_blueprint(condition_blueprint)
	from .project.datacollection import datacollection_blueprint
	app.register_blueprint(datacollection_blueprint)
	return app

