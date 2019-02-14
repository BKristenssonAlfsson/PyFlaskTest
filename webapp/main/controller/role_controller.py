from flask import request, Response
from ..model.role_model import Role
from flask_restplus import Resource
from .. import session
from ..util.role_dto import RoleDto

api = RoleDto.api
role = RoleDto.role


@api.route('/')
class AllRoles(Resource):
    @api.marshal_list_with(role)
    def get(self):

        roles = session.query(Role).all()

        return roles, 200
