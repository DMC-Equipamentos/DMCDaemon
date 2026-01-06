import subprocess
from os import path
# from ...config import *
import os
import signal
import platform

ERROR_MESSAGES = {
    9: "O programador não foi encontrado, certifique-se de que ele está conectado ao usb do computador.",
    7: "O processador não foi encontrado, certifique-se que a placa a ser gravada está conectada e alimentada.",
    10: "O programador não foi encontrado, certifique-se de que ele está conectado ao usb do computador.",
}

def record(ctx, hex_file, CMD = ""):
    
    ctx.output = ""

    baud = "900000" if platform.system() == "Linux" else "460800"

    cmd = [
        "python",
        "-m", "esptool",
        "-b", baud,
        "write_flash",
        "0x30000",
        hex_file, # Arquivo bin
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
