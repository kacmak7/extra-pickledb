import flask
app = flask.Flas(__name__)

@app.route('status')
def show_status():
    return 'Yo, it\'s live !'
