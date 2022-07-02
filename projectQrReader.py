import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

qr = pyqrcode.create("This is what converted into QR code.")
qr.png("qrCode.png", scale=16)

d = decode(Image.open("qrCode.png"))
print(d[0].data.decode("ascii"))