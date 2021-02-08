import subprocess
from os import path
# from ...config import *
import os
import signal

ERROR_MESSAGES = {
    9: "O programador não foi encontrado, certifique-se de que ele está conectado ao usb do computador.",
    7: "O processador não foi encontrado, certifique-se que a placa a ser gravada está conectada e alimentada.",
    10: "O programador não foi encontrado, certifique-se de que ele está conectado ao usb do computador.",
}

def record(ctx, hex_file, CMD = "", pic="", TOOL="", **kwargs):
    
    ctx.output = ""

    cmd = [
            # 'java', '-jar', 
            CMD,
           "-F{}".format(hex_file), # Arquivo hex
           '-P{}'.format(pic), # pic
           '-TP{}'.format(TOOL), # Programador
           '-M' # Gravar
    ]

    print(" ".join(cmd))
    proc = subprocess.Popen(
        cmd,
        shell=False, stdout=subprocess.PIPE)
    ctx.process = proc
    for line in proc.stdout:
        ctx.output+=line.decode();
        print(line.decode())

    proc.wait()
    ret = proc.poll()
    print("IN WAIT", proc.returncode, ret)
    # process.wait()
    
    ctx.return_code = proc.returncode

    if (ret in ERROR_MESSAGES.keys()):
        ctx.error = ERROR_MESSAGES[ret]

    return ctx.return_code
