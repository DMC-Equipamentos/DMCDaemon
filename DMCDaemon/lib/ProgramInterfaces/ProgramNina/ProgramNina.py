import subprocess
from os import path, makedirs

JLINK_CMD = """eoe 1
device NRF52832_XXAA
si SWD
speed 4000
connect
erase
loadfile {}
q"""

def create_aux_file(aux_path, hex_path):

    if not path.exists(aux_path):
        makedirs(aux_path)
        
    fpath = path.join(aux_path, 'program.link')

    with open(fpath, 'w+') as link_file:
        link_file.write(
            JLINK_CMD.format(hex_path)
        )

    return fpath

def record(ctx, hex_file, CMD = "", AUX_PATH="", **kwargs):
    
    ctx.output = ""

    aux_file = create_aux_file(AUX_PATH, hex_file)

    cmd = [
            # 'java', '-jar', 
            CMD,
           "-commanderscript",
           aux_file # Arquivo hex
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

    return ctx.return_code
