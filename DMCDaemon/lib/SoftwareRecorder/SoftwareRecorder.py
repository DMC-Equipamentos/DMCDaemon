import subprocess
from os import path

COMAND_RECORDER = "ipecmd.sh" 
SOFTWARE_FOLDER = "./"


RET_CODES = {
    0: "OK",
    9: "Programador não encontrado",
    7: "Processador não encontrado ou incorreto",

}

def errorExplanation(cod):
    if cod in RET_CODES:
        return RET_CODES[cod]
    else :
        return "Erro desconhecido!"

def record_software(hex_file, pic, programer, output = print, jar = 'ipecmd.sh'):

    cmd = ['java', '-jar', jar,
           "-F{}".format(path.join(SOFTWARE_FOLDER,hex_file)), # Arquivo hex
           '-P{}'.format(pic), # pic
           '-TP{}'.format(programer), # Programador
           '-M' # Gravar
    ] 
    print(" ".join(cmd))
    process = subprocess.Popen(
        cmd,
        #["ipecmd.sh -F'{}' -P{} -TP{} ".format(hex_file, pic, programer)],
                           shell=False, stdout=subprocess.PIPE)

    return process

    # for line in process.stdout:
    #     output(line)
        
    # process.wait()

    # print(process.returncode)
    return process.returncode
