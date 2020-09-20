
##First part of the scraping
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import requests
import pandas as pd
from flask import Flask, render_template, request
zipcode = ""
app = Flask(__name__)



@app.route('/results', method="post")
def getZip():
    global zipcode
    zipcode = request.forms.get('zip')
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
    words = []
    for text in html:
        words += str(text).split()
#https://public.opendatasoft.com/explore/dataset/us-zip-code-latitude-and-longitude/table/?q=45693
    # print(len(words))
    [print(word) for word in words if word[:10] == 'class = "commonName"']
    # [print(word) for word in words if word[:7] == 'title="']
    # print(html)
    # print(re.findall("<span", html))
    # options = html.find_all(string=lambda text: text != None)
    # options = html.find_all(string=lambda text: bool(re.match("^[-+]?\d+(\.\d+)?$", str(text))))
    # [print(option) for option in options]

plant_scrape("94560")




def disaster_scrape():
    zip_url = "https://www.unitedstateszipcodes.org/" + zipcode + "/"
    url = "http://www.usa.com/94602-ca-natural-disasters-extremes.htm"