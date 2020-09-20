#Save the name, coordinates, site score, and site url
import pandas as pd
import numpy as np
from scraper import coordinate
from scraper import locationData
import Homer

# from scraper import scrape_conversionWebsite

zipcode = Homer.getZip() 

# Importing superfund site list 
# OldToxicData = pd.read_csv("toxic.csv")

toxicData = pd.read_csv("short-toxic.csv")
# Cleaning up data accordingly
'''
dropCols = ['X', 'Y', 'FID', 'OBJECTID',
            'Site_EPA_ID', 'SEMS_ID', 'Region_ID', 
            'State', 'City', 'County', 'Status', 
            'Proposed_Date', 'Listing_Date', 
            'Construction_Completion_Date',
            'Construction_Completion_Number',
            'NOID_Date', 'Deletion_Date',
            'Site_Listing_Narrative',
            'Site_Progress_Profile',
            'Notice_of_Data_Availability',
            'Proposed_FR_Notice', 'Deletion_FR_Notice',
            'Final_FR_Notice','NOID_FR_Notice', 
            'Restoration_FR_Notice_Jumper_Pa', 
            'Site_has_had_a_Partial_Deletion',
            'CreationDate', 'Creator', 'EditDate',
            'Editor']
'''
#toxicData = OldToxicData.drop(dropCols, inplace = True, axis = 1)

#OldToxicData.to_csv("short-toxic.csv")

# Searching for local superfund sites 

def toxicSites(zipcode):
    sites = []
    latitude = coordinate(zipcode)[0]
    longitude = coordinate(zipcode)[1] 
    lat = locationData['Latitude'] == latitude
    lon = locationData['Longitude'] == longitude
    localSites = lat[toxicData]
    localSites = long[toxicData]
    for name in toxicData["Site_Name"]:
        sites.append(name)
    return sites

print(toxicSites(zipcode))