from flask_restful import Resource, fields, marshal_with
from ..backend import database, auth

class GroupPrefixes(Resource):

    decorators = [auth.login_required]

    types = {
        'id': fields.Integer,
        'prefix': fields.String,
        'server': fields.String
    }

    def __init__(self):
        self.db = database

    @marshal_with(types)
    def get(self, groupId):
        return self.db.getGroupPrefixes(groupId)
