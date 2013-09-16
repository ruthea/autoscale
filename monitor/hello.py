import os
from flask import Flask
from flask import request
from flask import render_template
import urllib
import time
from datetime import datetime
import threading
import random


r_time_str = ''
num_threads = 5
thread_delay = 3
loadtest = 0

class InitiateLoad (threading.Thread):
 def run (self):
     global loadtest
     global num_threads
     global thread_delay
     loadtest = 1
     while (loadtest):
      for x in xrange ( num_threads ):
       MyThread().start()
      time.sleep(thread_delay)


class MyThread ( threading.Thread ):
 def run (self):
     global r_time_str
     global thread_delay
     url = 'http://helloflask25.cfapps.io/fast'
     time.sleep (random.random()*thread_delay)
     start = datetime.now()
     nf = urllib.urlopen(url)
     page = nf.read()
     end = datetime.now()
     r_time_str += str(start)[:-4] + ',' + str(page) + ',' + (str(end - start)[:-4])[5:] + '<br>'
     nf.close()


app = Flask(__name__)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/monitor/')
def monitor():
    return render_template('flot/ajax/index.html')

@app.route('/mon/')
def mon():
    return render_template('index.html')
@app.route('/data/')
def data():
    url = 'http://monitor25.cfapps.io/static/flot/examples/ajax/data-usa-gdp-growth.json'
    nf = urllib.urlopen(url)
    page = nf.read()
    nf.close()
    return page
