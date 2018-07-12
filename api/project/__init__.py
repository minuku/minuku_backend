from flask import Blueprint

project_blueprint = Blueprint('project',__name__)

from . import views
