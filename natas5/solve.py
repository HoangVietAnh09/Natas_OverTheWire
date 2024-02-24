import requests

url = "http://natas5.natas.labs.overthewire.org/"
s = requests.Session()
s.auth = ('natas5', 'Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD')
r = s.get(url)

r.headers['Set-Cookie'] = 'loggedin=1'
print(r.headers)