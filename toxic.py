#Save the name, coordinates, site score, and site ur
import Homer
import pandas as pd
import numpy as np
from Homer.scraper import coordinates
from Homer.scraper import locationData
from flask import Flask, render_template, request
zipcode = ""
app = Flask(__name__)
# from scraper import scrape_conversionWebsite

# zipcode = 

@app.route('/results', methods=["POST"])
def getZip():
    global zipcode
    zipcode = request.forms.get('zip')

# Importing superfund site list 
OldToxicData = pd.read_csv("toxic.csv")

# Cleaning up data accordingly
# dropCols = ['X', 'Y', 'FID', 'OBJECTID',
#             'Site_EPA_ID', 'SEMS_ID', 'Region_ID', 
#             'State', 'City', 'County', 'Status', 
#             'Proposed_Date', 'Listing_Date', 
#             'Construction_Completion_Date',
#             'Construction_Completion_Number',
#             'NOID_Date', 'Deletion_Date',
#             'Site_Listing_Narrative',
#             'Site_Progress_Profile',
#             'Notice_of_Data_Availability',
#             'Proposed_FR_Notice', 'Deletion_FR_Notice',
#             'Final_FR_Notice','NOID_FR_Notice', 
#             'Restoration_FR_Notice_Jumper_Pa', 
#             'Site_has_had_a_Partial_Deletion',
#             'CreationDate', 'Creator', 'EditDate',
#             'Editor']

#toxicData = OldToxicData.drop(dropCols, inplace = True, axis = 1)

OldToxicData.to_csv("short-toxic.csv")

# Searching for local superfund sites 

def toxicSites(zipcode):
    latitude, longitude = coordinates(zipcode) 
    lat = locationData['Latitude'] == latitude
    lon = locationData['Longitude'] == longitude
    localSites = lat[locationData]
    localSites = long[locationData]
    
    return localSites


print(localToxicData)