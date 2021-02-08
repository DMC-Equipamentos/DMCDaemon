from ..lib.SoftwareRecorder.SoftwareRecorder import record_software
from config import *
import gevent
from bottle import route, run, response, request
from threading import Timer, Thread, Event
from ..lib.SoftwareDownloader import SoftwareDownloader, DMCCloud
import os
import time
import sys
import traceback

def show_exception():
    exc_type, exc_value, exc_traceback = sys.exc_info()
    lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
    # print exc_traceback
    # print lines
    fname = 'error%s.log' % (time.time())
    with open(fname, 'w') as f:
        for l in lines:
            # print l
            f.write(l)
            print(l)
        print('\n\n')
        print("Foi encontrado um erro não esperado, o arquivo de logs foi gravado: %s" % (fname))

def safe_exec_try(func, *args, **kwargs):
    try:
        func(*args, **kwargs)
    except Exception as e:
        # print e
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        # print exc_traceback
        # print lines
        fname = 'error%s.log' % (time.time())
        with open(fname, 'w') as f:
            for l in lines:
                # print l
                f.write(l)
                print(l)
            print('\n\n')
            print("Foi encontrado um erro não esperado, o arquivo de logs foi gravado: %s" % (fname))



class DMCThread(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.event = Event()
        self.is_running = False
        self.output = ""
        self.return_code = 0
        self.error = ""
        self.task = None
        self.task_args = {}

    def download_and_program(self):
        software_data = DMCCloud.getSoftware(self.task_args['id'])
        print(software_data)
        variables = software_data['software']['recording_comand']['variables']
        interface = software_data['software']['recording_comand']['software_type']
        SoftwareDownloader.getFile(software_data['file'], 'myfile.hex')
        print("start run")
        self.output = "";
        ret_code = record_software(self, interface, os.path.join(SOFTWARES_FOLDER,'myfile.hex'), **variables)   
        return ret_code     

    def run(self):
        while True:
            if self.task == 'download_and_record':
                print("IN TASK")
                self.is_running = True
                ret_code = None
                self.error = ""
                try:
                    ret_code = self.download_and_program();
                    if ret_code != 0 and len(self.error) <= 1:
                        self.error = "Erro ao gravar!"
                except Exception as e:
                    exc_type, exc_value, exc_traceback = sys.exc_info()
                    lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
                    fname = 'error%s.log' % (time.time())
                    with open(fname, 'w') as f:
                        for l in lines:
                            f.write(l)
                            print(l)
                        print('\n\n')
                        print("Foi encontrado um erro não esperado, o arquivo de logs foi gravado: %s" % (fname))
                    self.error = "Algum erro inesperado aconteceu"

                
                self.task = None
                self.is_running = False
            time.sleep(1)

    def downloadAndRecordPic(self, **kwargs):
        self.task = "download_and_record"
        self.task_args = kwargs
        print("should download_and_record")

    def stopRec(self):
        if self.is_running and self.process:
            self.process.kill()

    def eraseError(self):
        self.error = ""

dmcThreading = DMCThread()
# print("start threading")
dmcThreading.start()