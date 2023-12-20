from flask import Flask,render_template,url_for
import json

app = Flask(__name__)

@app.route('/')
def index():
    with open("config.json", "r") as f:
        dict = json.load(f)
        return render_template("1.html",z11=dict['SH1']['z11'],z12=dict['SH1']['z12'],z13=dict['SH1']['z13'],z14=dict['SH1']['z14'],z15=dict['SH1']['z15'],t11=dict['SH1']['t11'],t12=dict['SH1']['t12'],t13=dict['SH1']['t13'],t14=dict['SH1']['t14'],t15=dict['SH1']['t15'])


def run():
    app.run(port=2000, host='127.0.0.1', debug=True)
