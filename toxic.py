#Save the name, coordinates, site score, and site url
import pandas as pd
import numpy as np
from scraper import scrape_conversionWebsite

# Importing superfund site list 
OldToxicData = pd.read_csv("toxic.csv")

# Cleaning up data accordingly
dropCols = ['X', 'Y', 'FID', 'OBJECTID',
            'Site_EPA_ID', 'SEMS_ID', 'Region_ID', 
            'State', 'City', 'County', 'Status', 
            'Prposed_Date', 'Listing_Date', 
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


toxicData = OldToxicData.drop(dropCols, inplace = True, axis = 1)

# Searching for local superfund sites 
coordinates = scrape_conversionWebsite(zipcode) # Note that coordinates will be list type

long = coordinates[0]
lat = coordinates[1]

is_long = wasteData['Longitude'] == long
is_lat = wasteData['Latitude'] == lat

# Presenting local superfund sites
localToxicData = toxicData[is_long]
localToxicData = localToxicData[is_lat]

print(localToxicData)