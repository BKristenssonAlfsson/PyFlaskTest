from flask import jsonify, Blueprint, request, json
from ..model.models import User
from datetime import datetime
from .. import session
from ..config.JsonEncoder import JsonEncoder

user_api = Blueprint('user_api', __name__)

dt = datetime.now()


@user_api.route('/')
def list_all_users():

    users = session.query(User).all()

    return (json.dumps(users, cls=JsonEncoder)), 200


@user_api.route('/add', methods=['POST'])
def add_user():
    dict_body = request.get_json()

    user = User(user=dict_body['name'],
                created_on=dt)

    session.add(user)
    session.commit()
    session.close()
    return jsonify({'message': 'New user was added.'}), 200


@user_api.route('/delete', methods=['DELETE'])
def delete_user():
    user_id = request.args.get('id')

    user = session.query(User).filter(User.id == user_id).first()

    session.delete(user)
    session.commit()
    session.close()
    return jsonify({'message': 'A user was deleted.'}), 200


@user_api.route('/patch', methods=['PATCH'])
def patch_user():

    dict_body = request.get_json()
    user_id = dict_body['id']

    session.query(User).filter(User.id == user_id).update({'name': dict_body['name']})

    session.commit()
    session.flush()
    session.close()
    return jsonify({'message': 'A user was updated.'}), 200
