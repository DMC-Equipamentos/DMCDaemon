import subprocess
from os import path
from ...config import *
import os
import signal



def record(ctx, hex_file="", pic="", programer=""):
    
    ctx.output = ""
    
    cmd = [
            # 'java', '-jar', 
            IPECMD,
           "-F{}".format(hex_file), # Arquivo hex
           '-P{}'.format(pic), # pic
           '-TP{}'.format(programer), # Programador
           '-M' # Gravar
    ] 

    print(" ".join(cmd))
    proc = subprocess.Popen(
        cmd,
        shell=False, stdout=subprocess.PIPE)
    ctx.process = proc
    for line in proc.stdout:
        ctx.output+=line.decode();
        if line.decode().startswith('Target device was not found'):
            print("NOT FOUNDDDDD")

            # proc.kill()
            # break
            # subprocess.Popen.kill(proc)
            # os.killpg(os.getpgid(proc.pid), signal.SIGTERM)  
        print(line.decode())

    ret = proc.poll()
    print("IN WAIT", proc.returncode, ret)
    # process.wait()
    
    ctx.return_code = proc.returncode

    return ctx.return_code
