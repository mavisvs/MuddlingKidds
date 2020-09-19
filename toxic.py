#Save the name, coordinates, site score, and site url
import pandas as pd
import numpy as np

wasteData = pd.read_csv("toxic.csv")

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


wasteData.drop(dropCols, inplace = True, axis = 1)