import requests

url1 = "http://info.corn.ch/"


response = requests.get(url=url1, headers={}, data={})

print(response)