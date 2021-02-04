import requests

API_URL = "http://192.168.2.164/api/api/"


def getSoftware(id):
    resp = requests.get(API_URL + 'version/{}'.format(id))
    return resp.json()
