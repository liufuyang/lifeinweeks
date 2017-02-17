import collections
import json
import math
from operator import itemgetter
from operator import attrgetter
import logging
import flask
from flask_cors import CORS

from utils.config.all_configs import Config

logging.basicConfig(
    filename=Config.LOGGING_FILENAME,
    format='%(asctime)s : %(levelname)s : %(message)s',
    level=Config.LOGGING_DEBUG_LEVEL)

app = flask.Flask(__name__, static_url_path='/static')
# CORS(app)  # for webpack server


@app.route("/")
def index():
    return flask.render_template('index.html')


@app.route("/api/get")
def get():
    w_data = {}
    num_list = [x for x in range(0, 90*52)]
    itr = map(lambda num: {
            'id': num,
            'color': 0
        }, num_list)
    w_data['data'] = list(itr)
    return flask.jsonify(w_data)

@app.route('/test')
def test():
    logging.info('/test visited')
    return Config.LOGGING_FILENAME

@app.route("/post", methods=['POST'])
def post():
    return flask.jsonify(flask.request.get_json())

if __name__ == "__main__":
    logging.info('Lifeinweeks backend is running on port:8000')
    app.run(host='0.0.0.0', port=8000, debug=Config.DEBUG)
