import base64

encodedSecret = "3d3d516343746d4d6d6c315669563362"
encodedSecret = bytes.fromhex(encodedSecret)
encodedSecret = encodedSecret[::-1]
encodedSecret = base64.decodebytes(encodedSecret).decode('UTF-8')
print(encodedSecret)
