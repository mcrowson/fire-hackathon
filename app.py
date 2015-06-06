__author__ = 'antoinepatton'

from flask import Flask, request, session, render_template
app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
    #events = api.call(get_event, arg0, arg1)
    data = dict()

    data['test'] = "whew who"
    data['matthew'] = None
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(port=5000)