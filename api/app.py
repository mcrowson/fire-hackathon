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

class MeasurementObject(db.Model):
    pass

class Sensor(db.Model):
    pass

db.create_all()
 
api_manager = APIManager(app, flask_sqlalchemy_db=db)
api_manager.create_api(Firefighter, methods=['GET', 'POST', 'DELETE', 'PUT'])
 
if __name__ == "__main__":
    app.run()