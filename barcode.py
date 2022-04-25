import qrcode
 
# Data to be encoded
data = 'https://github.com/Qwabena-Proxy'

# Creating an instance of QRCode class
qr = qrcode.QRCode(version = 1,
                   box_size = 10,
                   border = 5)
 
# Encoding data using make() function
img = qrcode.make(data)

qr.make(fit = True)
img = qr.make_image(fill_color = 'black',
                    back_color = 'white')
 
# Saving as an image file
img.save('MyQRCode1.png')
print(img)
