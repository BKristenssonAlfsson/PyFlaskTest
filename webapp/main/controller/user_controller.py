from flask import jsonify, request, json
from ..model.user_model import User
from datetime import datetime
from flask_restplus import Resource
from .. import session
from ..config.JsonEncoder import JsonEncoder
from ..util.user_dto import UserDto

user_api = UserDto.api
service = UserDto.service

dt = datetime.now()


@user_api.route('/', methods=['GET'])
class Test(Resource):
    @user_api.marshal_list_with(service, envelope='services')
    def list_all_users(self):
        print("HERE")
        users = session.query(User).all()
        return users
#        return (json.dumps(users, cls=JsonEncoder)), 200


@user_api.route('/add', methods=['POST'])
class Testa(Resource):
    @user_api.marshal_list_with(service, envelope='services')
    def add_user(self):
        dict_body = request.get_json()

        user = User(user=dict_body['name'],
                    created_on=dt)

        session.add(user)
        session.commit()
        session.close()
        return jsonify({'message': 'New user was added.'}), 200


@user_api.route('/delete', methods=['DELETE'])
class Tests(Resource):
    @user_api.marshal_list_with(service, envelope='services')
    def delete_user(self):
        user_id = request.args.get('id')

        user = session.query(User).filter(User.id == user_id).first()

        session.delete(user)
        session.commit()
        session.close()
        return jsonify({'message': 'A user was deleted.'}), 200


@user_api.route('/patch', methods=['PATCH'])
class Testq(Resource):
    @user_api.marshal_list_with(service, envelope='services')
    def patch_user(self):

        dict_body = request.get_json()

        user_id = dict_body['id']

        session.query(User).filter(User.id == user_id).update({'name': dict_body['name']})

        session.commit()
        session.flush()
        session.close()
        return jsonify({'message': 'A user was updated.'}), 200
