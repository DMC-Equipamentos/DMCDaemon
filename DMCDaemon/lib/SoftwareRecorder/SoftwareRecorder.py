import subprocess
from os import path
from ..ProgramInterfaces.ProgramPic import ProgramPic
from ..ProgramInterfaces.ProgramNina import ProgramNina
from ... import config

INTERFACE_FUCTIONS = {
    'microchip': ProgramPic.record,
    'nina': ProgramNina.record
}

INTERFACE_CONFIG = {
    'microchip': config.MICROCHIP,
    'nina': config.NINAB11    
}


def record_software(ctx, interface, file_path, **kwargs):
    print(kwargs, INTERFACE_CONFIG[interface])
    return INTERFACE_FUCTIONS[interface](ctx, file_path, ** {**kwargs, ** INTERFACE_CONFIG[interface]})
