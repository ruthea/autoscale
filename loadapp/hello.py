import os
from flask import Flask
from flask import request
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
     url = 'http://helloflask25.cfapps.io/medium'
     time.sleep (random.random()*thread_delay)
     start = datetime.now()
     nf = urllib.urlopen(url)
     page = nf.read()
     end = datetime.now()
     r_time_str += str(start)[:-4] + ',' + str(page) + ',' + (str(end - start)[:-4])[5:] + '<br>'
     nf.close()


app = Flask(__name__)

@app.route('/start')
def start():
     InitiateLoad().start()
#      time.sleep(thread_delay)
     return '<h2>Starting Loadtest</h2>'

@app.route('/perf')
def perf():
    global r_time_str
    return r_time_str

@app.route('/stop')
def stop():
    global loadtest
    loadtest = 0
    env = str(os.environ)
    return '<h2>Stopping Loadtest</h2>' 

@app.route('/clearperf')
def clearperf():
    global r_time_str
    r_time_str = ''
    return 'Cleared Perf Metrics'

@app.route('/data')
def data():
    global thread_delay
    global num_threads
    response_str = ''
    tmp_delay = int(request.args.get('delay'))
    if tmp_delay >=0:
     thread_delay = tmp_delay
     response_str += 'Changed delay to ' + str(tmp_delay) + '<br>'

    tmp_num_threads = int(request.args.get('threads'))
    if tmp_num_threads >=0:
     num_threads = tmp_num_threads
     response_str += 'Changed num_threads to ' + str(tmp_num_threads) + '<br>'
    return response_str
