from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

@app.route("/hello")
def hello_world2():
    return 'Hello World!'

@app.route("/name")
def name():
    return 'Ayush'
