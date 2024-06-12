import requests

url = 'http://natas0.natas.labs.overthewire.org'

s = requests.Session()
s.auth = ('natas0','natas0')
print(s.get(url).text)