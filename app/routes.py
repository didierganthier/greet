from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/greet/<name>")
def greet(name):
  return render_template("greet.html", name=name)

