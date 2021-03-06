from flask_restful import Resource, fields, marshal_with
from ..backend import database, auth

class Players(Resource):

    decorators = [auth.login_required]

    types = {
        'uuid': fields.String,
        'name': fields.String,
        'prefix': fields.String,
        'suffix': fields.String
    }

    def __init__(self):
        self.db = database

    @marshal_with(types)
    def get(self, playerUuid=None):
        if playerUuid is None:
            return self.db.getPlayers()
        else:
            player = self.db.getPlayers(playerUuid)
            if player is None:
                return None, 404
            else:
                return player
