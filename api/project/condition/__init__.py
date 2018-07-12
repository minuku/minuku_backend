from flask import Blueprint

condition_blueprint = Blueprint('condition',__name__)

from . import views

