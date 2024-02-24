import requests

url = 'http://natas3.natas.labs.overthewire.org'

s = requests.Session()
s.auth = ('natas3', 'G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q')
url_check = url + "/robots.txt"
r = s.get(url_check)
print(r.text)
print('------------------')
url += '/s3cr3t/'
r = s.get(url)
print(r.text)

