from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user_service', description="You don't know the power of the dark side")

    service = api.model('user_service', {
      'id': fields.Integer(required=True, description=''),
      'name': fields.String(required=True, description=''),
      'created_on': fields.DateTime(required=True, description='')
    })
