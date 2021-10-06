# github.com/echtr
import image
import qrcode
from flask import Flask, render_template, request, url_for
import os


class kod:
	def __init__(self, icerik):
		self.icerik = icerik
		self.qr = None
	def olustur(self):
		self.qr = qrcode.QRCode(version = 5, box_size = 5, border = 1)
		self.qr.add_data(self.icerik)
		self.qr.make(fit = True)
	def kaydet(self):
		img = self.qr.make_image(fill="black", back_color = "white")
		os.chdir("static")
		os.chdir("kod")
		img.save("qr_kod.png")
	def kaydet2(self):
		img = self.qr.make_image(fill="black", back_color = "white")
		img.save("qr_kod.png")

app = Flask(__name__)
@app.route("/")
def index():
	return render_template("index.html")

listeleme = 0
@app.route("/kaydet", methods = ["POST"])
def kaydet(): # get methodu için de bir şeyler kodla
	global listeleme
	if listeleme == 0:
		_qr = kod(request.form["yazi"])
		_qr.olustur()
		_qr.kaydet()
		listeleme+=1
	else:
		_qr = kod(request.form["yazi"])
		_qr.olustur()
		_qr.kaydet2()
	return render_template("kaydet.html", _qr = request.form["yazi"])

	
if __name__ == "__main__":
	app.run()