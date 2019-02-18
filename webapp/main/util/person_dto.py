from flask_restplus import Namespace, fields


class PersonDto:

    api = Namespace('user', description='Signup roster for cadets!')

    user = api.model('user', {
        'id': fields.Integer(description='User id. Is auto incremented'),
        'name': fields.String(required=True, description='The name of the apprentice'),
        'created_on': fields.DateTime(description='Imperial join date'),
        'role': fields.Integer(required=True, description='Type of soldier')
    })

    role = api.model('role', {
        'role': fields.String()
    })

    test = api.model('test', {
        'name': fields.String(description='Name of person'),
        'created_on': fields.DateTime(description='Joined the army'),
        'role': fields.String(attribute='role.role', description='Trooper type')
    })
