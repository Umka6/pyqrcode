import pyqrcode

QRString = '	'
url = pyqrcode.create(QRString)
url.png('sait.png', scale=8)
