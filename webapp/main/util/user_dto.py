from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='Join the Empire. We have cookies!')

    user = api.model('user', {
        'id': fields.Integer(description='User id. Is auto incremented'),
        'name': fields.String(required=True, description='The name of the apprentice'),
        'created_on': fields.DateTime(description='Imperial join date')
    })
