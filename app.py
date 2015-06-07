__author__ = 'antoinepatton'

import sqlite3
import flask
from flask import Flask, request, session, render_template
import logging
import json
import requests
from api.app import Firefighter, MeasurementObject, Reading, Sensor
import logging

logger = logging.getLogger(__name__)

sh = logging.StreamHandler()
logger.addHandler(sh)
logger.setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def get_initial_data():
    #events = api.call(get_event, arg0, arg1)
    data = dict()
    data['test'] = "whew who"
    #return json.dumps(data)
    return render_template('index.html', data=data)

@app.route('/get_firefighter_stats',  methods=['GET'])
def firefighter_stats():
    data = dict()
    data['firefighters'] = requests.get('http://127.0.0.1:5001/api/firefighter').json()['objects']
    for firefighter in data['firefighters']:
       logger.debug(firefighter)

@app.route('/get_temperature_updates',  methods=['GET'])
def temperature_updates():
    try:
        data = dict()
        data['firefighters'] = requests.get('http://127.0.0.1:5001/api/firefighter').json()['objects']
        temp_list = []
        ff_final_data = dict()
        count = 0
        for ff in data['firefighters']:
            logger.debug(ff['id'])
            fire_fighter_id = str(ff['id'])
            data['temperatures'] = requests.get('http://127.0.0.1:5001/api/reading?q={"filters":[{"name":"firefighter","op":"eq","val":"'+fire_fighter_id+'"}]}').json()['objects']
            for temperature_obj in data['temperatures']:
                temp_list.append(temperature_obj)
            temp_list.reverse()
            firefighter_temp = []
            i = 0
            while len(firefighter_temp) <6:
                firefighter_temp.append(temp_list[i])
                i +=1
            firefighter_temp.reverse()
            ff_final_data[count] = firefighter_temp
            count +=1
        logger.debug(ff_final_data)
        return render_template('index.html', data=data)
    except Exception as inst:
        logger.debug(inst)


@app.route('/get_rehab_d',  methods=['GET'])
def get_rehab_data():

    data = dict()
    data['fighter1'] = ['touch', 'smell']
    data['fighter2'] = "Hey"
    data['fighter3'] = "Here we are"
    data['fighter4'] = ['touch', 'smell']
    return flask.jsonify(data)

@app.route('/get_messages',  methods=['GET'])
def messages_updates():
    pass

@app.route('/get_talia_analytics',  methods=['GET'])
def talia_analytics():
    pass




if __name__ == '__main__':
    app.run()