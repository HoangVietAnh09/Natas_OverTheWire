import requests

url = 'http://natas3.natas.labs.overthewire.org'

s = requests.Session()
s.auth = ('natas3', '3gqisGdR0pjm6tpkDKdIWO2hSvchLeYH')
url_check = url + "/robots.txt"
r = s.get(url_check)
print(r.text)
print('------------------')
url += '/s3cr3t/users.txt'
r = s.get(url)
print(r.text)

