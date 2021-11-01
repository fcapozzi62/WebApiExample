import requests
from requests.auth import HTTPBasicAuth

# creo la API_key
# chiamo la api applicationservicegroupGet con le credenziali di fabio
API_key = dict(Session = 'abcd1234ffgghh')
p = requests.get('http://localhost:5010/applicationservicegroupGet', auth= HTTPBasicAuth('fabio', 'hello'), cookies=API_key)
print(p.text)

# creo la API_key
# chiamo la api applicationserviceGroupGet con le credenziali di massimo
API_key = dict(Session = '12345abcdffaa')
p = requests.get('http://localhost:5010/applicationservicegroupGet', auth= HTTPBasicAuth('massimo', 'bye'), cookies=API_key)
print(p.text)

API_key = dict(Session = '12345abcdffaa')
p = requests.get('http://localhost:5010/remoteRemoteIdGet?remote_id=1', auth= HTTPBasicAuth('massimo', 'bye'), cookies=API_key)
print(p.text)

API_key = dict(Session = '12345abcdffaa')
print("GET/inrouteInroutegroupId?inroutegroup_id=5")
p = requests.get('http://localhost:5010/inroutegroupInroutegroupIdGet?inroutegroup_id=5', auth= HTTPBasicAuth('massimo', 'bye'), cookies=API_key)
print(p.text)

print("GET/remoteRemoteId?remote_id=1")
p = requests.get('http://localhost:5010/remoteRemoteIdGet?remote_id=1', auth= HTTPBasicAuth('massimo', 'bye'), cookies=API_key)
print(p.text)

print("GET/remoteRemoteId?remote_id=2")
p = requests.get('http://localhost:5010/remoteRemoteIdGet?remote_id=2', auth= HTTPBasicAuth('massimo', 'bye'), cookies=API_key)
print(p.text)

print("GET/remoteRemote")
p = requests.get('http://localhost:5010/remoteRemoteGet', auth= HTTPBasicAuth('massimo', 'bye'), cookies=API_key)
print(p.text)

# Post request example
print("POST/downconverterPost")
data = {"id": 45, "name": "demoName", "parent_id": 15, "manufacturer_id": 211}
url = 'http://localhost:5010/downconverterPost/'
p = requests.post(url=url, data=data, timeout=2.5, auth=HTTPBasicAuth('massimo', 'bye'), cookies=API_key)
print(p.text)

# Same page, get request results in an html form to be compiled out by user
p = requests.get(url=url, auth=HTTPBasicAuth('massimo', 'bye'), cookies=API_key)
print(p.text)



