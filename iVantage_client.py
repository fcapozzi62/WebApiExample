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




