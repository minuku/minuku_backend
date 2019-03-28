from flask import Blueprint

user_blueprint = Blueprint('uesr',__name__)
from .import views
