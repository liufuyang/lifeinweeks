import collections
import datetime
import json
import math
from operator import itemgetter
from operator import attrgetter
import logging
import flask
from flask_restful import Resource, Api
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

api = Api(app)
jwt = JWT(app, authenticate, identity)


# This returns correct error when not authenticated
# Try GET on localhost:8000/api_old/users
@app.route('/api_old/users')
@jwt_required()
def get_users():
    return flask.jsonify(users)


class Users(Resource):
    # Try GET on localhost:8000/api/users

    @jwt_required()  # This returns 500 however ...
    def get(self):
        return users

api.add_resource(Users, '/api/users')


# This is not working for flask_restful
@app.errorhandler(JWTError)
def handle_auth_error(error):
    return flask.jsonify(
        {
            'description': 'Request does not contain an access token',
            'error': 'Authorization Required. Using @app.errorhandler(JWTError)',
            'status_code': 401
        }), 401

# Not working either:
# @jwt.jwt_error_handler  # https://github.com/mattupstate/flask-jwt/issues/65
# def error_handler(e):
#     return flask.jsonify(
#         {
#             'description': 'Request does not contain an access token',
#             'error': 'Authorization Required. Using @jwt.jwt_error_handler',
#             'status_code': 401
#         }), 401

# Note about package versoins:
# aniso8601==1.2.0
# appdirs==1.4.0
# click==6.7
# configparser==3.5.0
# Flask==0.12
# Flask-Cors==3.0.2
# Flask-JWT==0.3.2
# Flask-RESTful==0.3.5
# gunicorn==19.6.0
# itsdangerous==0.24
# Jinja2==2.9.5
# MarkupSafe==0.23
# packaging==16.8
# PyJWT==1.4.2
# pyparsing==2.1.10
# python-dateutil==2.6.0
# pytz==2016.10
# six==1.10.0
# Werkzeug==0.11.15
#
# With python version: 3.5.1

if __name__ == "__main__":
    logging.info('Lifeinweeks backend is running on port:8000')
    app.run(host='0.0.0.0', port=8000, debug=Config.DEBUG)
