import requests

url = 'http://natas1.natas.labs.overthewire.org/'

s = requests.Session()
s.auth = ('natas1', '0nzCigAq7t2iALyvU9xcHlYN4MlkIwlq')
print(s.get(url).text)