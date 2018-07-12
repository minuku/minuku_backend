from flask import Flask
from flask_cors import CORS
import sys
sys.path.append('~/minuku/api')

#from api import db
app =Flask(__name__)
CORS(app)
from datacollection import datacollection_blueprint
app.register_blueprint(datacollection_blueprint)


if __name__ =='__main__':
	app.run(debug=True)
