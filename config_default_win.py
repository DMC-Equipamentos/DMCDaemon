
# Pasta para fazer download dos arquivos de software
SOFTWARES_FOLDER = "./DMCDaemon/downloads/"


## Interfaces de programa ##

MICROCHIP = {
    # Executavel para o IPECMD
    'CMD': "C:\\Program Files (x86)\\Microchip\\MPLABX\\v5.20\\mplab_platform\\mplab_ipe\\ipecmd.exe",

    # Programador utilizado
    'TOOL': "ICD3", # "ICD3", "PK3", "ICD4"
}

NINAB11 = {
    # executavel para o JLinkExe
    'CMD': 'C:\\Program Files (x86)\\SEGGER\\JLink\\JLink.exe',

    # Um caminho auxiliar para dados do jlink
    'AUX_PATH': SOFTWARES_FOLDER + 'NINA/'
}

AVR = {
    'CMD': 'avrdude',
    
}