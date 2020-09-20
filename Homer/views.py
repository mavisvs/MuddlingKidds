from Homer import app#, db
# from scraper.py import scrape
from flask import render_template, request, redirect
# from Homer.models import Fact

wasteLocation = "amani"
AQI = "was"
carbonPPM = "here"
naturalDisastors = ["list", "here"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results", methods = ["GET", "POST"])
def results():
    global wasteLocation
    global AQI
    global carbonPPM
    global naturalDisastors
    # scrape()
    
    return render_template("results.html", data={"natDis":naturalDisastors, "waste":wasteLocation, "AQI":AQI, "carbon":carbonPPM})

@app.route("/getData", methods = ["POST"])
def getData():
    global wasteLocation
    global AQI
    global carbonPPM
    global naturalDisastors
    if request.method == "POST":
        jsdata=request.json()
        AQI = jsdata["data"][0]["aqi"]
    return redirect("/results")

