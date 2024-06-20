import base64
import requests

url = 'http://natas8.natas.labs.overthewire.org'

s = requests.Session()
s.auth = ('natas8', 'xcoXLmzMkoIP9D7hlgPlh9XD7OgLAe5Q')
r = s.get(url)
print(r.text)
print('--------------------------------------')
#decode secret
encodedSecret = "3d3d516343746d4d6d6c315669563362"
encodedSecret = bytes.fromhex(encodedSecret)
encodedSecret = encodedSecret[::-1]
encodedSecret = base64.decodebytes(encodedSecret).decode('UTF-8')
print('Decoded secret is: {encodedSecret}')
print('--------------------------------------')

data = {'secret': encodedSecret,
        'submit': 'submit+Quey'
        }
r = s.post(url, data=data)
print(r.text)

