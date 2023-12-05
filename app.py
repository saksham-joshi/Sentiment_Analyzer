from flask import Flask, request
from Model.Analyzer import *
app = Flask(__name__)

@app.route("/")
def load_mainpage():
    return open("index.html")

@app.route("/analyze")
def analyze() :
    return Analyze_String(request.args.get('text'))
    