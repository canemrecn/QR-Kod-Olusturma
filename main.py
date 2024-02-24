import qrcode
from PIL import Image
# QR kodu oluşturma
qr = qrcode.QRCode(version=15, box_size=10, border=5)
data = 'Merhaba'  # QR kodu içerecek metin
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color='black', back_color='white')
# QR kodunu kaydetme
img.save('qr.png')