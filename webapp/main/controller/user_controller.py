from flask import request, Response
from ..model.user_model import User
from datetime import datetime
from flask_restplus import Resource
from .. import session
from ..util.user_dto import UserDto

api = UserDto.api
user = UserDto.user

dt = datetime.now()


@api.route('/')
class AllUsers(Resource):
    @api.marshal_list_with(user)
    def get(self):

        users = session.query(User).all()

        return users, 200


@api.route('/add')
class AddUser(Resource):
    @api.marshal_list_with(user)
    def post(self):
        dict_body = request.get_json()

        user_to_add = User(user=dict_body['name'],
                           created_on=dt)

        session.add(user_to_add)
        session.commit()
        session.close()
        return ({'message': 'New user was added.'}), 200


@api.route('/delete')
class DeleteUser(Resource):
    @api.marshal_list_with(user)
    def delete(self):
        user_id = request.args.get('id')

        user_to_delete = session.query(User).filter(User.id == user_id).first()

        session.delete(user_to_delete)
        session.commit()
        session.close()
        return ({'message': 'A user was deleted.'}), 200


@api.route('/patch')
@api.response(404, "User not found")
class UpdateUser(Resource):
    @api.marshal_list_with(user)
    def patch(self):

        dict_body = request.get_json()
        user_id = dict_body['id']

        session.query(User).filter(User.id == user_id).update({'name': dict_body['name']})

        response = Response({'User was updated'})

        session.commit()
        session.flush()
        session.close()

        return response, 202
