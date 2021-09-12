from flask import Flask, render_template ,request,session,redirect
from tools.tools import readFile
@app.route("/")
def index():
names=readFile("datos.txt")
	amoutOfHumans=len(names)
	"""
	"""
	return render_template("index.html"nmaes=names)
if __name__ == "__main__":
	app.run(debug=True,host="127.0.0.1",port=9600)