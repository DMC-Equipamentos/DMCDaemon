import requests
from config import * 
import os

def getFile(url, save_path):
    if not os.path.exists(SOFTWARES_FOLDER):
        os.makedirs(SOFTWARES_FOLDER)
    response = requests.get(url)
    open(os.path.join(SOFTWARES_FOLDER,save_path), 'wb').write(response.content)

