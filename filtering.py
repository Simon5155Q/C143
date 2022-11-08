from sre_constants import SUCCESS
from flask import Flask, request, jsonify
import csv

moviedata = []
with open("movies.csv") as f:
    reader = csv.reader(f)
    moviedatalist = list(reader)
    moviedata = moviedatalist[1:]
liked = []
didntwatch = []
unliked = []

app = Flask(__name__)
@app.route("/movies")

def movies():
    return jsonify({
        "data": moviedata,
        "success": "success"
    })

@app.route("/liked")
def liked():
    return jsonify({
        "liked" : liked,
        "success": "success"
    })

@app.route("/didntwatch")
def didntwatch():
    return jsonify({
        "didntwatch": didntwatch,
        "success": "success"
    })

@app.route("/unliked")
def unliked():
    return jsonify({
        "unliked": unliked,
        "success": "success"
    })