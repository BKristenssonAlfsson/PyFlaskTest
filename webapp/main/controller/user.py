from sqlalchemy import create_engine
from flask import jsonify, Blueprint
from ..config.postgres import postgres
from datetime import datetime
from ..model.models import User

user_api = Blueprint('user_api', __name__)

engine = create_engine(postgres)
connection = engine.connect()


@user_api.route('/')
def list_all_users():

    results = connection.execute("SELECT * FROM temp")

    return jsonify([dict(row) for row in results])


@user_api.route('/add', methods = ['POST'])
def add_user():
    print("HERE")
    dt = datetime.now()
    new_user = User.insert()

    new_user.execute(name='Test', created_on=dt)
