from flask import Flask,render_template,url_for
import json

app = Flask(__name__)

@app.route('/')
def index():
    with open("config.json", "r") as f:
        dict = json.load(f)
        return render_template("3.html",z31=dict['SH3']['z31'],z32=dict['SH3']['z32'],z33=dict['SH3']['z33'],t31=dict['SH3']['t31'],t32=dict['SH3']['t32'],t33=dict['SH3']['t33'],i31=dict['SH3']['i31'],i32=dict['SH3']['i32'])


def run():
    app.run(port=2000, host='127.0.0.3', debug=True)