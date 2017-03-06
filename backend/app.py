import collections
from datetime import datetime
from datetime import date
import dateutil.parser
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


def gen_clean_week_data(birthday):    
    num_list = [(y, w) for y in range(0, 90) for w in range(0, 52)]
    
    itr = map(lambda num: {
        'year_num': num[0],
        'week_num': num[1],
        'color': cal_base_color(num[0], num[1], birthday)
    }, num_list)

    return list(itr)

def cal_base_color(year, week, birthday):
    age_year, age_week =  cal_age_year_week(birthday)
    birth_week = cal_week_number(birthday)
    
    print('birth_week: '+ str(birth_week))
    print('age_week: '+ str(age_week))
    
    if age_year < 0:
        return 1

    # Note: Tricky part, if birth_week is large than age_week
    # then we need to let the data year starts from one year ahead.
    if birth_week > age_week:
        age_year = age_year + 1

    if year == 0:
        if year == age_year:
            return 1 if week < birth_week or week >= age_week else 0
        else:
            return 1 if week < birth_week else 0
    elif year < age_year:
        return 0
    elif year == age_year:
        return 0 if week <= age_week else 1
    elif year > age_year:
        return 1

def cal_age_year_week(birthday):
    today = date.today()
    
    age_year = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    age_week = cal_week_number(today)
    
    print('age_year: ' + str(age_year))
    print('age_week: ' + str(age_week))
    
    return (age_year, age_week)

def cal_week_number(input_date):
    # week_num = input_date.isocalendar()[1] - 1 # calculate current week number is not idea
    week_num = int((date(input_date.year, input_date.month, input_date.day) - date(input_date.year,1,1)).days / 7)
    week_num = 51 if week_num >= 52 else week_num
    return week_num


# TODO use db later on
user_data = {
    '0': {
        'data': gen_clean_week_data(date.today())
    }
}


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/api/get')
def get():
    return flask.jsonify(gen_clean_week_data(date.today()))


@app.route('/api/week-data', methods=['POST'])
def post_week_data():
    data = flask.request.get_json()
    # birthday = datetime.strptime(data['birthday'])
    birthday = dateutil.parser.parse(data['birthday'])
    print(type(birthday))
    print(birthday)
    return flask.jsonify(gen_clean_week_data(birthday))


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
