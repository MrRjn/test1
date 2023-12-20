from flask import Flask,render_template,url_for
import json

app = Flask(__name__)

@app.route('/')
def index():
    with open("config.json", "r") as f:
        dict = json.load(f)
        return render_template("2.html",z21=dict['SH2']['z21'],t21=dict['SH2']['t21'],i21=dict['SH2']['i21'])


def run():
    app.run(port=2000, host='127.0.0.2', debug=True)