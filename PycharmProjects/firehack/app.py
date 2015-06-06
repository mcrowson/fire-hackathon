__author__ = 'antoinepatton'

import sqlite3
from flask import Flask, request, session

app = Flask(__name__)
app.config.from_object(__name__)




if __name__ == '__main__':
    app.run()