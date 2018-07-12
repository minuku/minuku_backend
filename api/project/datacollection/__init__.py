from flask import Blueprint
datacollection_blueprint = Blueprint('datacollection',__name__)

from . import views

