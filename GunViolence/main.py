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

# Working copy of GVA data. 
GVA = pd.DataFrame(GVA_data)

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
