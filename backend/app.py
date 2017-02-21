import collections
import datetime
import json
import math
from operator import itemgetter
from operator import attrgetter
import logging
import flask
from flask_restful import Api
from flask_jwt import JWT
from flask_cors import CORS

from utils.config.all_configs import Config
from security import authenticate, identity
from db import db
from resources import user_resources

logging.basicConfig(
    filename=Config.LOGGING_FILENAME,
    format='%(asctime)s : %(levelname)s : %(message)s',
    level=Config.LOGGING_DEBUG_LEVEL)

app = flask.Flask(__name__, static_url_path='/static')
app.secret_key = Config.SECRET_KEY
app.config['PROPAGATE_EXCEPTIONS'] = True

api = Api(app)
# CORS(app)  # for webpack server
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{}:{}@{}:{}/{}'.format(
    Config.DB_USER, Config.DB_PASS, Config.DB_HOST, Config.DB_PORT, Config.DB_NAME)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_first_request
def create_tables():
    logging.info('create_tables...')
    db.create_all()

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


@app.route('/api/user/<string:uid>/week-data', methods=['POST'])
def add_user_week_data(uid):
    pass


@app.route('/api/user/<string:uid>/week-data')
def get_user_week_data(uid):
    return flask.jsonify(user_data[uid])


api.add_resource(user_resources.User, '/api/user/<string:uid>')
api.add_resource(user_resources.Users, '/api/users')


if __name__ == "__main__":
    logging.info('Lifeinweeks backend is running on port:8000')
    app.run(host='0.0.0.0', port=8000, debug=Config.DEBUG)
