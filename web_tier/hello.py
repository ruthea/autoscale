import os
from flask import Flask

app = Flask(__name__)

@app.route('/slow')
def slow():
    for x in xrange(1, 1000000):
     env = str(os.environ)
    return '<h2>Very slow!!!</h2>'

@app.route('/medium')
def medium():
    for x in xrange(1, 100000):
     env = str(os.environ)

    return '<h2>medium</h2>'

@app.route('/fast')
def fast():
    for x in xrange(1, 10000):
     env = str(os.environ)

    return '<h2>fast</h2>' 
