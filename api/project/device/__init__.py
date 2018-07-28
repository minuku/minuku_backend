from flask import Blueprint

device_blueprint = Blueprint('deivce',__name__)

from . import views


