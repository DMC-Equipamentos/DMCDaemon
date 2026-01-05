import yaml

with open('./config.yaml') as file:
    settings_data = yaml.load(file, Loader=yaml.FullLoader)

# Pasta para fazer download dos arquivos de software
SOFTWARES_FOLDER = settings_data['SOFTWARES_FOLDER']

DAEMON_PORT = settings_data['DAEMON_PORT']

## Interfaces de programa ##

MICROCHIP = settings_data['MICROCHIP']

NINAB11 = settings_data['NINAB11']

AVR = settings_data['AVR']

ESP32 = settings_data['ESP32']