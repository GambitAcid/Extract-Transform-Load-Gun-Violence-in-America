# Project Two- Extract, Transform, and Load (ETL): Data on Shootings and Gun Violence in America
Group Members: Lynne Freilich, Ronnie Phillips, Corban Doran
Due: Saturday June 11th, 2022

Project Outline Overview: 
This Case Study Project demonstrates the Extract, Transform, Load (ETL) process.  We selected datasets for future analysis to examine possible correlation between gun injury data (including deaths, injuries, accidental discharges, gun violence, and other factors) and monthly background check data.  Datasets were chosen of sufficient size, from reputable sources.  

Future analysis could provide insight into states that may need better gun safety and training due to frequency of accidental discharges resulting in injuries and/or death.  Analyses of interest are found in the Technical Report.

Extract- 
We imported .csv datasets from the following data sources: 
•	Gun Violence Archive- https://www.kaggle.com/datasets/gunviolencearchive/gun-violence-database
•	This dataset was originally in PDF format and was converted to .csv.  NICS Firearm Background Checks- https://raw.githubusercontent.com/BuzzFeedNews/nics-firearm-background-checks/master/data/nics-firearm-background-checks.csv
•	We attempted to scrape data from the following; however, the data was un-scrapable.  Mass Shootings- https://www.gunviolencearchive.org/reports (mass shootings ALL, accidental deaths ALL) Reform.

Transform- 
Data cleaning involved: transformation of data columns into datetime, filtering to limit the data to the time period we wanted to examine (2016), selecting the columns relevant to future analysis, changing formatting for ease of use and legibility, and serializing the data.  

Load- 
We then loaded the results into four Postgres Tables: FBI NICS, Incidents, Participants, and Incident URLS.  We joined FIB NICS and Incidents along the date parameter, Incidents and Participants along the IncidentID parameter, and Participants and Incidents URLS along the IncidentID parameter, as well.  

Please reference the included “Gun Violence ETL.png” for a visualization of this overall process.  Please also reference the included “Technical Report” for a more detailed explanations.



OurWBS was as follows:
•	Initialize the repository, add files and folders.
•	Locate appropriate datasets, and extract data using JuPyter notebook and pandas.  
•	Transform the data, combine, and store into a dataframe.
•	Load the data with the local databases and check tables into PostgreSQL.
•	Load the data with local database and check tables into and join with PostgreSQL in PgAdmin.

