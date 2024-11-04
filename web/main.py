from flask import Flask, render_template, request
import matplotlib
import csv
import datetime
import os

app = Flask(__name__)

Data = {}

def insert_data(data):
    with open("data.csv", "a+", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

def get_data():
    with open("data.csv", "r") as file:
        return csv.reader(file)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        pump_status = request.form.get("pump_status")
        print(pump_status)
        return "Data Received from HTML Ajax"
    return render_template("index.html")

@app.route("/project_details", methods=["GET", "POST"])
def project_details():
    return render_template("project_details.html")

if __name__ == "__main__":
    app.run(debug=True, port=3000)
