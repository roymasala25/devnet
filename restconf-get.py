import json
import requests
requests.packages.urllib3.disable_warnings()
api_url = "https://192.168.45.131/restconf/data/ietf-interfaces:interfaces"
headers = { "Accept": "application/yang-data+json",
            "Content-type":"application/yang-data+json"
            }
basicauth = ("admin","admin123")
resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)
print(resp.text)