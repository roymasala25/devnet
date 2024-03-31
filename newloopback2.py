import requests
import json

url = "https://192.168.45.131/restconf/data/ietf-interfaces:interfaces/interface/"

payload = json.dumps({
  "ietf-interfaces:interface": [
    {
      "name": "Loopback100",
      "description": "new Loopback100 added by restconf",
      "type": "iana-if-type:softwareLoopback",
      "enabled": True,
      "ietf-ip:ipv4": {
        "address": [
          {
            "ip": "100.100.100.1",
            "netmask": "255.255.255.0"
          }
        ]
      },
      "ietf-ip:ipv6": {}
    }
  ]
})
headers = {
  'Content-Type': 'application/yang-data+json',
  'Accept': 'application/yang-data+json',
  'Authorization': 'Basic YWRtaW46YWRtaW4xMjM='
}

response = requests.request("POST", url, headers=headers, data=payload,verify=False)

print(response.text)
