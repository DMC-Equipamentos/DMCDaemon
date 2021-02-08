# from gevent import monkey; monkey.patch_all()
from bottle import route, run, response, hook
from .DMCService import dmcThreading

VERSION = "1.0.0"

@hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, PUT, PATCH, DELETE, HEAD, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
    response.headers['Content-type'] = 'application/json'


@route('/echo')
def echo():
    return {"running":"ok", 'threading': dmcThreading.is_running, 'output': dmcThreading.output, 'error':dmcThreading.error, 'version':VERSION}


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

def run_server(port):
    print("DMCService iniciando na porta {}".format(port))
    run(host='localhost', port=port, debug = False, quiet=True)