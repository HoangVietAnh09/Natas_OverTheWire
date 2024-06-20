import requests

url = "http://natas5.natas.labs.overthewire.org/"
s = requests.Session()
s.auth = ('natas5', '0n35PkggAPm2zbEpOU802c0x0Msn1ToK')
r = s.get(url)

r.headers['Set-Cookie'] = 'loggedin=1'
print(r.headers)