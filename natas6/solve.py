import requests

url = 'http://natas6.natas.labs.overthewire.org/'
s = requests.Session()
s.auth = ('natas6', 'jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr')
r = s.get(url)

print(r.text)