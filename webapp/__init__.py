from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import user_api as ua

blueprint = Blueprint('user_api', __name__, url_prefix='/user_api')

api = Api(blueprint,
          title="End point setup",
          description="Join the Empire, they have cookies!")

api.add_namespace(ua, path='/test')
