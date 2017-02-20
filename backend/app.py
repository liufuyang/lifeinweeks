import collections
import datetime
import json
import math
from operator import itemgetter
from operator import attrgetter
import logging
import flask
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required, JWTError
from flask_cors import CORS

from utils.config.all_configs import Config
from security import authenticate, identity

logging.basicConfig(
    filename=Config.LOGGING_FILENAME,
    format='%(asctime)s : %(levelname)s : %(message)s',
    level=Config.LOGGING_DEBUG_LEVEL)

app = flask.Flask(__name__, static_url_path='/static')
app.secret_key = Config.SECRET_KEY
app.config['PROPAGATE_EXCEPTIONS'] = True

api = Api(app)
# CORS(app)  # for webpack server

# jwt will create a new endpoint: /auth which connect to the method
# authenticate
jwt = JWT(app, authenticate, identity)


def gen_clean_week_data():
    num_list = [x for x in range(0, 90 * 52)]
    itr = map(lambda num: {
        'id': num,
        'color': 0
    }, num_list)
    return list(itr)

# TODO use db later on
users = {
    '0': {
        'uid': '0',
        'birthday': datetime.date.today().isoformat()
    }
}

user_data = {
    '0': {
        'data': gen_clean_week_data()
    }
}


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/api/get')
def get():
    return flask.jsonify(gen_clean_week_data())


# POST - add user
@app.route('/api_old/user', methods=['POST'])
def create_user():
    request_data = flask.request.get_json()
    users[request_data['uid']] = request_data
    return flask.jsonify(request_data)


@app.route('/api_old/users')
@jwt_required()
def get_users():
    return flask.jsonify(users)


@app.route('/api_old/user/<string:uid>')
def get_user_info(uid):
    return flask.jsonify(users[uid])


@app.route('/api/user/<string:uid>/week-data', methods=['POST'])
def add_user_week_data(uid):
    pass


@app.route('/api/user/<string:uid>/week-data')
def get_user_week_data(uid):
    return flask.jsonify(user_data[uid])


@app.route('/test')
def test():
    logging.info('/test visited')
    return Config.LOGGING_FILENAME


# RESTFUL:
class User(Resource):

    @jwt_required()
    def get(self, uid):
        if uid in users:
            # no need to use jsonify as flask_restful does that for us
            return users[uid]
        else:
            return {'message': 'User does not exist'}, 404  # not found

    def post(self, uid):
        if uid in users:
            # bad request
            return {'message': 'A user with uid {} already exists'.format(uid)}, 400

        # request_data = flask.request.get_json()
        request_data = User.parser.parse_args()
        request_data['uid'] = uid
        users[uid] = request_data
        return request_data, 201

    def put(self, uid):

        request_data = User.parser.parse_args()

        if uid not in users:
            request_data['uid'] = uid
            users[uid] = request_data
        else:
            request_data['uid'] = uid
            users[uid].update(request_data)
        return request_data

    parser = reqparse.RequestParser()
    parser.add_argument('birthday',
                        type=str,
                        required=True,
                        help='This field cannot be left blank'
                        )


class Users(Resource):

    @jwt_required()
    def get(self):
        return users

api.add_resource(User, '/api/user/<string:uid>')
api.add_resource(Users, '/api/users')


if __name__ == "__main__":
    logging.info('Lifeinweeks backend is running on port:8000')
    app.run(host='0.0.0.0', port=8000, debug=Config.DEBUG)
