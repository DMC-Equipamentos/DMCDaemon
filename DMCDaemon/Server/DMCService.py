from ..lib.PicRecorder.PicRecorder import record
from ..config import *
import gevent
from bottle import route, run, response, request
from threading import Timer, Thread, Event
from ..lib.SoftwareDownloader import SoftwareDownloader, DMCCloud
import os
import time

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

    def run(self):
        while True:
            if self.task == 'download_and_record_pic':
                print("IN TASK")
                self.is_running = True
                software_data = DMCCloud.getSoftware(self.task_args['id'])
                print(software_data)
                pic = software_data['software']['recording_comand']['variables']['pic']
                SoftwareDownloader.getFile(software_data['file'], 'myfile.hex')
                print("start run")
                self.output = "";
                ret_code = record(self, hex_file = os.path.join(SOFTWARES_FOLDER,'myfile.hex'), pic=pic, programer='RICE') # '24F16KL401'
                if ret_code != 0:
                    self.error = "Erro ao gravar!"
                self.task = None
                self.is_running = False
            time.sleep(1)

    def downloadAndRecordPic(self, **kwargs):
        self.task = "download_and_record_pic"
        self.task_args = kwargs
        print("should download_and_record")

    def stopRec(self):
        if self.is_running and self.process:
            self.process.kill()

    def eraseError(self):
        self.error = ""

dmcThreading = DMCThread()
print("start threading")
dmcThreading.start()