import requests

url = 'http://natas2.natas.labs.overthewire.org/'

s = requests.Session()
s.auth = ('natas2', 'TguMNxKo1DSa1tujBLuZJnDUlCcUAPlI')

url += 'files/users.txt'

print(s.get(url).text)