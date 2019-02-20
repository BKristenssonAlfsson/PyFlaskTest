from flask_restplus import Namespace, fields


class RoleDto:

    api = Namespace('role', description='Army personnel titles')

    role = api.model('role', {
        'id': fields.Integer(description='User id. Is auto incremented'),
        'role': fields.String(required=True, description='Type of soldier'),
     })

    trooper = api.model('trooper', {
        'trooper': fields.String(required=True, description='Type of soldier')
    })
