import requests
from requests.auth import HTTPBasicAuth
p = requests.get('http://localhost:5000/somma/', auth= HTTPBasicAuth('fabio','ik0ibh00'))
print(p,p.text)
r = requests.get('http://localhost:5000/somma/', params= {'val1': '10', 'val2': '20'})

myurl = 'http://localhost:5000/somma/'
cookies = dict(Session = '12ab3ccdef432')
r = requests.get(myurl,params= {'val1':'10','val2':'20'}, cookies=cookies)
print(r.text)
print(r.cookies)

myurl = 'http://www.cnn.com/'
r = requests.get(myurl)
print(r.cookies)

