from flask import Flask
from flask.ext.restless import APIManager
from flask.ext.sqlalchemy import SQLAlchemy
 
app = Flask(__name__)

@app.route('/api/')
def index():
    return "Hello Hackathon"


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///firefighters.db'
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



if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5001, use_reloader=True)