import requests

API_URL = "http://192.168.0.163:8000/api/"


def getSoftware(id):
    resp = requests.get(API_URL + 'version/{}'.format(id))
    return resp.json()
