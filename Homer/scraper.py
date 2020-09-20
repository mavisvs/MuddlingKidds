
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


locationData = pd.read_csv("Homer/static/zipcode.csv")

def formZip(zipc):
    zipc = str(zipc)
    zipc = zipc.replace(".", "")[:-1]
    zipc = (5-len(zipc))*"0" + zipc
    return zipc

def coordinate(zipcode):

    if int(zipcode) > 99929:
        return [10**10,10**10]

    min_i = 0
    max_i = len(locationData.index) - 1
    old_i = 0

    while max_i > min_i:

        new_i = (min_i + max_i)//2
        if old_i == new_i:
            break
        else:
            old_i = new_i

        zipc, lat, lng = locationData.iloc[new_i]
        zipc = formZip(zipc)
        if zipc == zipcode:
            return [lat, lng]
        elif int(zipc) < int(zipcode):
            min_i = new_i
        else:
            max_i = new_i
       
    return [10**10,10**10]



    # for i, row in locationData.iterrows():
    #     zipc = str(row[0])
    #     zipc = zipc.replace(".", "")[:-1]
    #     zipc = (5-len(zipc))*"0" + zipc
    #     if zipc == zipcode:
    #         latitude = row['LAT']
    #         longitude = row['LNG']
    #         return [latitude, longitude]
    # return [10**10,10**10]

df = pd.read_csv('Homer/static/zipsandstates.csv')
to_drop = {'lat','lng','city','state_name',
            'zcta','parent_zcta','population','density',
            'county_fips','county_name','county_weights',
            'county_names_all','county_fips_all','imprecise',
            'military','timezone'
            }
states = df.drop(to_drop, axis = 1, inplace = True)
