from Homer import app#, db
# from scraper.py import scrape
from flask import render_template, request, redirect
# from Homer.models import Fact
import re
from bs4 import BeautifulSoup
import requests
import Homer.toxic
import pandas as pd
import numpy as np
from Homer.scraper import coordinate
from Homer.scraper import locationData
from urllib.request import urlopen

wasteLocation = "amani"
AQI = "was"
carbonPPM = "here"
# naturalDisastors = ["list", "here"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results", methods = ["GET", "POST"])
def results():
    global wasteLocation
    # global naturalDisastors
    # scrape()
    zipcode = request.args.get('zip')
    naturalDisastors = disaster_scrape(zipcode)
    wasteLocation = toxicSites(zipcode)
    recycle = allNearbyCents(zipcode)
    data={"zip":zipcode, "natDis":naturalDisastors, "waste":wasteLocation, "recycle":recycle}
    return render_template("results.html", data=data)
    
@app.route("/susTips")
def susTips():
    return render_template("suslife.html")


toxicData = pd.read_csv("Homer/static/short-toxic.csv")

def toxicSites(zipcode):
    toxicData = pd.read_csv("Homer/static/short-toxic.csv")
    sites = []
    latitude = coordinate(zipcode)[0]
    longitude = coordinate(zipcode)[1]
    close_lat = abs(toxicData['Latitude'] - float(latitude)) < 0.2
    close_lng = abs(toxicData['Longitude'] - float(longitude)) < 0.2
    close_lat_sites = toxicData[close_lat]
    localSites = close_lat_sites[close_lng]

    for name in localSites["Site_Name"]:
        sites.append(name)
    
    return sites

stateSheet = pd.read_csv('Homer/static/states.csv')

def state_converter(zipcode):
    zipcode = zipcode.lstrip("0")
    if not zipcode:
        return None
    zipc = (stateSheet['zip'] == int(zipcode))
    state = stateSheet[zipc]
    state_ID = state['state_id']
    try:
        return state_ID.iloc[0]
    except:
        print("State code not found")
        return None
    

def disaster_scrape(zipcode):
    statecode = state_converter(zipcode)
    if not statecode:
        return [['N/A']*3]*3
    statecode = statecode.lower()
    url = "http://www.usa.com/" + zipcode + "-" + statecode + "-natural-disasters-extremes.htm"
    page = requests.get(url)
    html = BeautifulSoup(page.content, 'html.parser')
    words = ""
    for text in html:
        words += str(text)
    words.replace("\n"," ")
    targets = ['EarthquakeIndex', 'VolcanoIndex', 'TornadoIndex']
    return [find_disaster_index(target, words) for target in targets]


def find_disaster_index(target, words):
    end = len(target)
    for start in range(len(words) - end):
        if words[start:start+end] == target:
            disaster_section = words[start:start+end+500]
            try: 
                start = disaster_section.index("</div") + 7
                d_zip_num = disaster_section[start:start+10]
                c_zip_num = re.sub(r'[^\d.]+','', d_zip_num)
                
                next_sect = disaster_section[start+10:]
                start = next_sect.index("</div") + 7
                d_state_num = next_sect[start:start+10]
                c_state_num = re.sub(r'[^\d.]+','', d_state_num)

                next_sect = next_sect[start+10:]
                start = next_sect.index("</div") + 7
                d_us_num = next_sect[start:start+10]
                c_us_num = re.sub(r'[^\d.]+','', d_us_num)

                return [c_zip_num, c_state_num, c_us_num]
            except:
                ...
    return ['N/A']*3

##RECYCLER

def allNearbyCents(zipcode):
    lithiumUrl = "https://search.earth911.com/?what=Lithium-ion+Batteries&where="
    lithiumUrl += zipcode
    lithiumUrl += "&list_filter=all&max_distance=5&family_id=&latitude=&longitude=&country=&province=&city=&sponsor="
    bottleUrl = "https://search.earth911.com/?what=%233+Plastic+Bottles&where=" + zipcode + "&list_filter=all&max_distance=5&family_id=&latitude=&longitude=&country=&province=&city=&sponsor="
    leadUrl = "https://search.earth911.com/?what=Lead-acid+Batteries+-+Non-automotive&where=" + zipcode + "&list_filter=all&max_distance=5&family_id=&latitude=&longitude=&country=&province=&city=&sponsor="     
    lithiumMin = numOfCents(lithiumUrl)
    # raise Exception(lithiumMin)
    bottleMin = numOfCents(bottleUrl)
    leadMin = numOfCents(leadUrl)
    recyclePlants = {"Lithium Ion Battery Return Centers": lithiumMin, "Plastic Bottle Recycling Centers": bottleMin, "Lead Battery Return Locations": leadMin}
    return recyclePlants


def numOfCents(url): #function takes in url and gives out least number of places within 5 mile radius
  pageRecycle = urlopen(url) #returns an HTTPResponse object
  html_bytes = pageRecycle.read()
  html = html_bytes.decode("utf-8")
  numResults = html.count("result-item")
  return numResults