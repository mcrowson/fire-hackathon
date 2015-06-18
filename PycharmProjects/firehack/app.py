__author__ = 'antoinepatton'

import sqlite3
from flask import Flask, request, session, render_template

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def get_initial_data():
    #events = api.call(get_event, arg0, arg1)
    data = dict()
    data['test'] = "whew who"

    return render_template('index.html', data)


if __name__ == '__main__':
    app.run()