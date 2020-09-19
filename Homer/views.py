from Homer import app#, db
# from scraper.py import scrape
from flask import render_template, request, redirect
# from Homer.models import Fact

@app.route("/")
def index():
    return render_template( "index.html")

@app.route("/results", methods = ["GET", "POST"])
def results():
    # scrape()
    print(request.form)
    AQI = "was"
    if request.method == "POST":
        jsdata=request.form["aqi"]
        AQI = jsdata["data"][0]["aqi"]
    naturalDisastors = ["list", "here"]
    wasteLocation = "amani"
    carbonPPM = "here"
    return render_template("results.html", data={"natDis":naturalDisastors, "waste":wasteLocation, "AQI":AQI, "carbon":carbonPPM})
