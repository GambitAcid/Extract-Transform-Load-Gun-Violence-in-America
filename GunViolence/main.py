# Dependencies and Setup
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import sqlalchemy as db

# Postgres Connection String
from config import User

# Set up Postgres DB Connections
cestring = f'{User}GunData'
engine = create_engine(cestring)

# Create database if it does not exist.
if not database_exists(cestring):
    create_database(cestring)
else:
    # Connect the database if exists.
    connection = engine.connect()
    metadata = db.MetaData()

# GVA data from Gun Violence Archive Data
get_GVA = "../Data/GVA13_18.csv"
GVA_data = pd.read_csv(get_GVA)

# FBI NICS data from FBI 
get_FBI = "../Data/FBI_NICs_Data.csv"
FBI_data = pd.read_csv(get_FBI)

# Working copy of GVA and FBI data. 
GVA = pd.DataFrame(GVA_data)
FBI = pd.DataFrame(FBI_data)

# Definition of FBI table and write to DB
Columns = ['month',
           'state', 
           'permit', 
           'permit_recheck', 
           'handgun', 
           'long_gun',
           'other',
           'multiple',
           'admin', 
           'prepawn_handgun',
           'prepawn_long_gun',
           'prepawn_other', 
           'redemption_handgun',
           'redemption_long_gun',
           'redemption_other',
           'returned_handgun', 
           'returned_long_gun',
           'returned_other',
           'rentals_handgun',
           'rentals_long_gun',
           'private_sale_handgun',
           'private_sale_long_gun',
           'private_sale_other',
           'return_to_seller_handgun',
           'return_to_seller_long_gun',
           'return_to_seller_other',
           'totals'
          ]
NewNames = {'month' : 'Month',
           'state': 'State',
           'permit': 'Permit',
           'permit_recheck': 'Permit_Recheck',
           'handgun': 'Handgun',
           'long_gun': 'Long_Gun', 
           'other': 'Other', 
           'multiple': 'Multiple',
           'admin' : 'Admin', 
           'prepawn_handgun': 'PrePawn_Handgun',
           'prepawn_long_gun':  'Pre_Pawn_Long_Gun',
           'prepawn_other': 'Prepawn_Other',
           'redemption_handgun': 'Redemption_Handgun',
           'redemption_long_gun':'Redemption_Long_Gun',
           'redemption_other': 'Redemption_Other',
           'returned_handgun': 'Returned_Handgun',
           'returned_long_gun':'Returned_Long_Gun',
           'returned_other': 'Returned_Other',
           'rentals_handgun':'Rentals_Handgun',
           'rentals_long_gun':'Rentals_Long_Gun',
           'private_sale_handgun':'Private_Sale_Handgun',
           'private_sale_other':'Private_Sale_Other',
           'return_to_seller_handgun':'Return_To_Seller_Handgun',
           'return_to_seller_long_gun':'Return_To_Seller_Long_Gun',
           'return_to_seller_other': 'Return_To_Seller_Other',
           'totals': 'Totals'
        }

FBIIncidAll = FBI[Columns].rename(columns=NewNames)
FBIIncidAll.index.rename('NICsChecksID', inplace=True)
FBIIncidAll.to_sql('NICsChecks', engine, index=True, if_exists='replace')

# Definition of Incident table and write to DB
Columns = ['incident_id',
            'date',
            'state',
            'city_or_county',
            'n_killed',
            'state_house_district',
            'state_senate_district'
          ]
NewNames = {'incident_id':'IncidentID',
            'date': 'Date',
            'state': 'State',
            'city_or_county': 'City',
            'n_killed': 'No_Killed',
            'state_house_district': 'House_District',
            'state_senate_district': 'Senate_District'
           }
GVAIncidAll = GVA[Columns].rename(columns=NewNames).set_index('IncidentID')
GVAIncidAll.to_sql('Incident', engine, index=True, if_exists='replace')

# Definition of Participant table
Columns = ['incident_id',
            'participant_age_group',
            'participant_gender',
            'participant_name',
            'participant_relationship',
            'participant_status',
            'participant_type'
          ]
NewNames = {'incident_id':'IncidentID',
            'participant_age_group': 'Age',
            'participant_gender': 'Gender',
            'participant_name': 'Name',
            'participant_relationship': 'Relationship',
            'participant_status': 'Status',
            'participant_type': 'Type'
           }
GVAPartAll = GVA[Columns].rename(columns=NewNames)
GVAPartAll.index.rename('ParticipantID', inplace=True)
GVAPartAll.to_sql('Participants', engine, if_exists='replace')

# Definition of Incident_urls table
Columns = ['incident_id',
            'source_url',
            'incident_url',
            'sources',
          ]
NewNames = {'incident_id':'IncidentID',
            'source_url': 'SourceUrl',
            'incident_url': 'IncidentUrl',
            'sources': 'SourcesUrl',
           }
GVAUrlAll = GVA[Columns].rename(columns=NewNames).set_index('IncidentID')
GVAUrlAll.to_sql('IncidentUrl', engine, index=True, if_exists='replace')
