__author__ = 'antoinepatton'

from flask import Flask, request, session, render_template
from werkzeug.serving import run_simple
from api.app import app as api_app
import requests
import logging

logger = logging.getLogger(__name__)

sh = logging.StreamHandler()
logger.addHandler(sh)
logger.setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
    #events = api.call(get_event, arg0, arg1)
    data = dict()
    firefighters = requests.get('http://127.0.0.1:5001/api/firefighter').json()['objects']
    for firefighter in firefighters:
        logger.debug(firefighter)

    data['test'] = "whew who"
    data['matthew'] = None
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.debug = True
    app.run(port=5000, use_reloader=True)