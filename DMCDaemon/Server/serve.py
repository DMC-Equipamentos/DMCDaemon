from gevent import monkey; monkey.patch_all()
from ..lib.SoftwareRecorder import SoftwareRecorder
from ..lib.PicRecorder.PicRecorder import record
from ..config import *
import gevent
from bottle import route, run, response, request, post, hook
from threading import Timer, Thread, Event
from ..lib.SoftwareDownloader import SoftwareDownloader
from .DMCService import dmcThreading

@hook('after_request')
def enable_cors():
    print("after_request hook")
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, PUT, PATCH, DELETE, HEAD, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
    response.headers['Content-type'] = 'application/json'


@route('/echo')
def echo():
    return {"running":"ok", 'threading': dmcThreading.is_running, 'output': dmcThreading.output, 'error':dmcThreading.error}


@route('/rec_software/<id>')
def record_software(id):
    # print(request.json)
    dmcThreading.downloadAndRecordPic(id=id)
    return {'status': 'waiting_resolution'}

@route('/stop_threading')
def stop_threading():
    dmcThreading.stopRec()
    return {'status': 'waiting_resolution'}

@route('/dismiss_error')
def dismiss_error():
    dmcThreading.eraseError()
    return {'status': 'waiting_resolution'}

def run_server():
    run(host='0.0.0.0', port=8080, server='gevent', debug = True)