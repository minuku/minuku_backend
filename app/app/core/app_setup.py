from ..main import app
from ..api import api

from flask import jsonify

@app.route("/")
def hello():
    # This could also be returning an index.html
    return '''Welcome to minuku backend, try <a href="/test/">/test/</test>'''

@app.route("/test")
def route_test():
    user_data = {
        'name': 'armuro',
        'email': 'minuku@gmail.com'
    }
    return jsonify(user_data)
