from sqlalchemy import create_engine, orm, update
from flask import jsonify, Blueprint, request
from ..config.postgres import postgres
from ..model.models import User
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

user_api = Blueprint('user_api', __name__)

engine = create_engine(postgres)
connection = engine.connect()

Session = orm.sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(bind=engine)

dt = datetime.now()


@user_api.route('/')
def list_all_users():

    users = User.query.all()

    results = connection.execute("SELECT * FROM temp")

    return jsonify([dict(row) for row in results]), 200


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

    User.query.filter_by(id=user_id).delete()

    session.commit()
    session.close()
    return jsonify({'message': 'A user was deleted.'}), 200


@user_api.route('/patch', methods=['PUT'])
def patch_user():

    dict_body = request.get_json()

    user = User.query.filter_by(id=dict_body['id']).first()

    user.name = dict_body['name']

    session.commit()
    session.close()
    return jsonify({'message': 'A user was updated.'}), 200
