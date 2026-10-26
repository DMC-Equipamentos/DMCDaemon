import requests

API_URL = "https://softwareserver-stg.k8s.dmcdev.net/api/api/"


def getSoftware(id, userToken):
    resp = requests.get(API_URL + 'version/{}'.format(id),
                        headers={'Authorization': 'Bearer {}'.format(userToken)})

    print(resp)
    
    return resp.json()
