import os
from flask import Flask

app = Flask(__name__)

@app.route('/slow')
def slow():
    for x in xrange(1, 1000000):
     env2 = str(os.environ)
    env = os.environ
    return str(env['PORT'])

@app.route('/medium')
def medium():
    for x in xrange(1, 100000):
     env2 = str(os.environ)
    env = os.environ
    return str(env['PORT'])

@app.route('/fast')
def fast():
    for x in xrange(1, 10000):
     env2 = str(os.environ)
    env = os.environ
    return str(env['PORT'])

@app.route('/env')
def env():
    env = os.environ
    return str(env['VCAP_SERVICES'])
