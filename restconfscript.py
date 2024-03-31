import requests
import json

url = "https://192.168.45.131/restconf/data/ietf-interfaces:interfaces/"

payload = {}
headers = {
  'Content-Type': 'application/yang-data+json',
  'Authorization': 'Basic YWRtaW46MTIz'
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

print(response.text)