__author__ = 'antoinepatton'

import sqlite3
import flask
from flask import Flask, request, session, render_template
import logging
import json
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
    pass

@app.route('/get_temperature_updates',  methods=['POST'])
def temperature_updates():
    data = dict()
    data['test'] = "whew who"
    #return json.dumps(data)
    return render_template('index.html', data=data)

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