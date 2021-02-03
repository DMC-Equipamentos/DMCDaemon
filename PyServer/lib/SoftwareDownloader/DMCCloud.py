import requests

API_URL = "http://localhost:8000/api/"


def getSoftware(id):
    resp = requests.get(API_URL + 'version/{}'.format(id))
    return resp.json()
