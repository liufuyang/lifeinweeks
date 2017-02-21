from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.user import UserModel

# RESTFUL:
class User(Resource):

    @jwt_required()
    def get(self, uid):
        user = UserModel.find_by_uid(uid)
        if user:
            # no need to use jsonify as flask_restful does that for us
            return user.json()
        else:
            return {'message': 'User does not exist'}, 404  # not found

    def post(self, uid):
        user = UserModel.find_by_uid(uid)
        if user:
            # bad request
            return {'message': 'A user with uid {} already exists'.format(uid)}, 400

        # request_data = flask.request.get_json()
        request_data = User.parser.parse_args()
        user = UserModel(uid, request_data['password'])
        
        try:
            user.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return user.json(), 201

    def put(self, uid):

        request_data = User.parser.parse_args()
        
        user = UserModel.find_by_uid(uid)

        if user:
            user.password = request_data['password']
        else:
            user = UserModel(uid, request_data['password'])
            
        try:
            user.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500
        return user.json()

    parser = reqparse.RequestParser()
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='This field cannot be left blank'
                        )


class Users(Resource):

    @jwt_required()
    def get(self):
        return dict(map(lambda x: (x.id, x.json()), UserModel.query.all()))