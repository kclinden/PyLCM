import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  # Disable SSL warning

def lcm_auth(lcmfqdn, user, password):
    #Builds an authentication token for the user. Takes the input of the LCM server, user and password.
    url = "https://{}/lcm/api/v1/login".format(lcmfqdn)
    payload = '{{"username":"{}","password":"{}"}}'.format(user, password)
    headers = {
        'accept': "application/json",
        'content-type': "application/json"
        }
    response = requests.request("POST", url, data=payload, headers=headers, verify=False)
    if response.status_code == 200:
        token = response.json()['token']
        return token
    else:
        raise Exception("Did not get status of 200 from server!")
