import requests


URL1 = "http://info.cern.ch/"
header = {}
data ={}

respond = requests.get(url= URL1, headers=header, data=data)
print(respond.text)
