import qrcode
 
# Data to be encoded
data = 'https://github.com/Qwabena-Proxy'
 
# Encoding data using make() function
img = qrcode.make(data)
 
# Saving as an image file
img.save('MyQRCode1.png')
print(img)
