from flask import Blueprint
from flask_restplus import Api

from .main.controller.user_controller import api as user

blueprint = Blueprint('user', __name__)

api = Api(blueprint,
          title="Imperial REST service.",
          description='Filty rebelscum should not be here')

api.add_namespace(user, path='/user')
