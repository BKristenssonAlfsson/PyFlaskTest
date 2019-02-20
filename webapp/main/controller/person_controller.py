from flask import request, Response
from ..model.person_model import Person
from ..model.role_model import Role
from datetime import datetime
from flask_restplus import Resource
from .. import session
from ..util.person_dto import PersonDto
from celery import Celery

api = PersonDto.api
user = PersonDto.user
test = PersonDto.test


app = Celery(broker='pyamqp://guest@localhost//')


@api.route('/')
class AllUsers(Resource):
    @api.marshal_list_with(test)
    def get(self):
        users = session.query(Person).filter(Person.role == Role.id).all()

        return users, 200


@api.route('/add')
class AddUser(Resource):
    @api.marshal_list_with(user)
    def post(self):
        dict_body = request.get_json()
        dt = datetime.now()

        user_to_add = Person(user=dict_body['name'],
                             created_on=dt,
                             role=dict_body['role'])

        session.add(user_to_add)
        session.commit()
        app.send_task('cms.tasks.tasks.enrollment', kwargs={"name": user_to_add.name,
                                                            "timestamp": user_to_add.created_on,
                                                            "role": user_to_add.role})
        session.close()

        return ({'message': 'New user was added.'}), 200


@api.route('/delete')
class DeleteUser(Resource):
    @api.marshal_list_with(user)
    def delete(self):

        user_id = request.args.get('id')

        user_to_delete = session.query(Person).filter(Person.id == user_id).first()

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

        session.query(Person).filter(Person.id == user_id).update({'name': dict_body['name']})

        response = Response({'User was updated'})

        session.commit()
        session.flush()
        session.close()

        return response, 202
