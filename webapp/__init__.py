from flask import Blueprint
from flask_restplus import Api
from flask_cors import CORS

from .main.controller.person_controller import api as user
from .main.controller.role_controller import api as role

blueprint = Blueprint('api', __name__, url_prefix='/api')
CORS(blueprint)

api = Api(blueprint,
          title="Imperial REST service.",
          description='Join the Empire. You know you want to!')

'# Add more namespaces for other paths here'
api.add_namespace(user, path='/user')
api.add_namespace(role, path='/role')
