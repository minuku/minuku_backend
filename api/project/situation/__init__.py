from flask import Blueprint

situation_blueprint = Blueprint('situation',__name__)

from . import views
