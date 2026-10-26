import requests
from config import * 
import os

def getFile(url, save_path, user_token):
    if not os.path.exists(SOFTWARES_FOLDER):
        os.makedirs(SOFTWARES_FOLDER)
    response = requests.get(url, headers={'Authorization': 'Bearer ' + user_token})
    open(os.path.join(SOFTWARES_FOLDER,save_path), 'wb').write(response.content)

