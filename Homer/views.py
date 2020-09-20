from Homer import app#, db
# from scraper.py import scrape
from flask import render_template, request, redirect
# from Homer.models import Fact
import re
import Homer
from bs4 import BeautifulSoup
import requests

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
    global AQI    
    global carbonPPM
    # global naturalDisastors
    # scrape()
    naturalDisastors = disaster_scrape()
    wasteLocation = "amani"
    AQI = "was"
    carbonPPM = "here"
    zipcode = request.args.get('zip')
    return render_template("results.html", data={"zip":zipcode, "natDis":naturalDisastors, "waste":wasteLocation, "AQI":AQI, "carbon":carbonPPM})

def 

def disaster_scrape():
    # url = "http://www.usa.com/" + zipcode + "-" + statecode + "-natural-disasters-extremes.htm"
    url = "http://www.usa.com/94602-ca-natural-disasters-extremes.htm"
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