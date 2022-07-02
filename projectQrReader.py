import pyqrcode         #To generate qr code
from pyzbar.pyzbar import decode          #To decode qrcode
from PIL import Image         #To save in png formats

qr = pyqrcode.create("This is what converted into QR code.")          #Creating qr code
qr.png("qrCode.png", scale=16)          #Saving qr code in .png format. Scale refers to the scale of the png. Higher the scale, larger the image looks.

d = decode(Image.open("qrCode.png"))          #Opening the .png image and decoding the qr code
print(d[0].data.decode("ascii"))          #Displaying qr code in ascii format by decoding the binary information found in .png
