

# Pasta para fazer download dos arquivos de software
SOFTWARES_FOLDER = "./DMCDaemon/downloads/"


## Interfaces de programa ##

MICROCHIP = {
    # Executavel para o IPECMD
    'CMD': "/opt/microchip/mplabx/v5.45/mplab_platform/mplab_ipe/ipecmd.sh",

    # Programador utilizado
    'TOOL': "RICE", # "ICD3", "PK3", "ICD4"
}

NINAB11 = {
    # executavel para o JLinkExe
    'CMD': 'JLinkExe',

    # Um caminho auxiliar para dados do jlink
    'AUX_PATH': SOFTWARES_FOLDER + 'NINA/'
}

AVR = {
    'CMD': 'avrdude',
    'TOOL': 'dragon_isp'
}