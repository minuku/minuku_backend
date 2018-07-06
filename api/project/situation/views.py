from .. import db
from . import situation_blueprint
from flask import request, make_response,json
from urllib import parse
from bson.json_util import dumps

@situation_blueprint.route('
