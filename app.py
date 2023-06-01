from flask import*
from flask import render_template
import requests

app = Flask(__name__, static_folder="assets", template_folder="templates")

@app.route("/")
def k():
	return render_template("index.html")

@app.route("/<a>")
def k1(a):
	t=a+".html"
	return render_template(t)

@app.route("/submit",methods=["POST"])
def k2():
	k="\n\nEmail: "+request.form["email"]+"\nName: "+request.form["name"]+"\nPhone number: "+request.form["phone"]+"\nMessage: "+request.form["message"]
	open("contact/contact.txt","a").write(k)
	return render_template("contact.html")

@app.errorhandler(404)
def k3(a):
	return render_template("err.html")

@app.errorhandler(Exception)
def k4(Exception):
	return render_template("err_5.html")
if __name__ == '__main__':
	app.run()