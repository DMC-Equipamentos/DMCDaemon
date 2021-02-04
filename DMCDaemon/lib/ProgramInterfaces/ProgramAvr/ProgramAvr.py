import subprocess
from os import path
# from ...config import *
import os
import signal



def record(ctx, hex_file, CMD = "", TOOL="", **kwargs):
    
    ctx.output = ""

    cmd = [
        # 'java', '-jar', 
        CMD, '-p', 'm16', '-c', TOOL, '-B', '10', '-P', 'usb', '-e', '-U', 'flash:w:{}'.format(hex_file), '-U', 'lfuse:w:0xe4:m'
    ] 

    print(" ".join(cmd))
    proc = subprocess.Popen(
        cmd,
        shell=False, stdout=subprocess.PIPE
    )
    ctx.process = proc
    for line in proc.stdout:
        ctx.output+=line.decode();
        print(line.decode())

    proc.wait()
    ret = proc.poll()
    print("IN WAIT", proc.returncode, ret)
    # process.wait()
    
    ctx.return_code = proc.returncode

    return ctx.return_code
