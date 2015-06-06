__author__ = 'antoinepatton'

from flask import Flask, request, session, render_template
from flask.ext.restless import APIManager
from flask.ext.sqlalchemy import SQLAlchemy
from api.app import app as api_app
from werkzeug.serving import run_simple

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
    #events = api.call(get_event, arg0, arg1)
    data = dict()
    data['test'] = "whew who"
    data['matthew'] = None
    return render_template('index.html', data=data)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///api/firefighters.db'
db = SQLAlchemy(app)

class Firefighter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    dob = db.Column(db.Text)
    baseline_resting_heartrate = db.Column(db.Integer)
    baseline_active_heartrate = db.Column(db.Integer)
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)


class Type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)


class MeasurementObject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    description = db.Column(db.Text)
    normal_reading = db.Column(db.Integer)
    max_threshold = db.Column(db.Integer)
    min_threshold = db.Column(db.Integer)
    type = db.Column(db.Integer)  # FK to Type


class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    measurement = db.Column(db.Integer)  # FK to Measurement Object
    name = db.Column(db.Text)
    description = db.Column(db.Text)


class Reading(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sensor = db.Column(db.Integer)  # FK to Sensor
    firefighter = db.Column(db.Integer)  # FK to Firefighter
    measurement_object = db.Column(db.Integer)   # FK to Measurement Object
    value = db.Column(db.Integer)  # The value being read
    timestamp = db.Column(db.Text)  # The timestamp of the reading

db.create_all()

api_manager = APIManager(app, flask_sqlalchemy_db=db)
api_manager.create_api(Firefighter, methods=['GET', 'POST', 'DELETE', 'PUT'])
api_manager.create_api(Sensor, methods=['GET', 'POST', 'DELETE', 'PUT'])
api_manager.create_api(MeasurementObject, methods=['GET', 'POST', 'DELETE', 'PUT'])
api_manager.create_api(Type, methods=['GET', 'POST', 'DELETE', 'PUT'])
api_manager.create_api(Reading, methods=['GET', 'POST', 'DELETE', 'PUT'])

if __name__ == '__main__':
    app.run()