import qrcode 
url = "https://www.youtube.com/"
qr_code = qrcode.make(url)
qr_code.save("qrcode.png")