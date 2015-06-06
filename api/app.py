from flask import Flask
from flask.ext.restless import APIManager
from flask.ext.sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
 
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

db.create_all()
 
api_manager = APIManager(app, flask_sqlalchemy_db=db)
api_manager.create_api(Firefighter, methods=['GET', 'POST', 'DELETE', 'PUT'])
 
if __name__ == "__main__":
    app.run()