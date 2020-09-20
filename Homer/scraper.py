
##First part of the scraping
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import requests
import pandas as pd
from flask import Flask, render_template, request
zipcode = ""
app = Flask(__name__)



@app.route('/results', methods=["GET"])
def getZip():
    global zipcode
    zipcode = request.args.get('zip')
    return zipcode
    
#FLOODING WEBSITE INFO
urlFlooding = "https://coast.noaa.gov/slr/#/layer/sce/0/-11581024.663779823/5095888.569004184/4/satellite/88/0.8/2050/interHigh/midAccretion"
pageFlood = urlopen(urlFlooding) #returns an HTTPResponse object
html_bytes = pageFlood.read()
html = html_bytes.decode("utf-8")


locationData = pd.read_csv("zipcode.csv")

def coordinate(zipcode):
    for row in locationData:
        if row[0] == zipcode:
            latitude = row['Latitude']
            longitude = row['Longitude']
    return [latitude, longitude]
    

def plant_scrape(zipcode):
    page = requests.get("https://www.nwf.org/NativePlantFinder/Plants/Flowers-and-Grasses/q=" + zipcode)
    html = BeautifulSoup(page.content, 'html.parser')
    print(html)
    # can loop through the children with beautiful soup
    # may be a good idea to print out what html looks like
    # call html.findall(i.e. the second div class)

# print(plant_scrape(zipcode))

# request.headers.get("location")



