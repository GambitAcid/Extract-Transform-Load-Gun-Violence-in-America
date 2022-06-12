# Project Two- Extract, Transform, and Load (ETL): Data on Shootings and Gun Violence in America
Group Members: Lynne Freilich, Ronnie Phillips, Corban Doran
Due: Saturday June 11th, 2022

**Project Outline Overview:** 
This Case Study Project demonstrates the Extract, Transform, Load (ETL) process.  We selected datasets for future analysis to examine possible correlation between gun injury data (including deaths, injuries, accidental discharges, gun violence, and other factors) and monthly background check data.  Datasets were chosen of sufficient size, from reputable sources.  

Future analysis could provide insight into states that may need better gun safety and training due to frequency of accidental discharges resulting in injuries and/or death.  Analyses of interest are found in the Technical Report.


![gvetl](https://user-images.githubusercontent.com/101227638/173212862-3b0403e4-86ea-454c-bf0d-2f3a8badc336.png)

**Extract-** 
We imported .csv datasets from the following data sources: 

•	Gun Violence Archive- https://www.kaggle.com/datasets/gunviolencearchive/gun-violence-database

     This website had accidental injuries, accidental deaths, mass shootings, by year, or you ccould view all. 

•	NICS Firearm Background Checks-https://www.fbi.gov/file-repository/nics_firearm_checks_-_month_year_by_state_type.pdf/view

     This dataset was originally in PDF format and was converted to .csv. 
      
•	Mass Shootings- https://www.gunviolencearchive.org/reports (mass shootings ALL, accidental deaths ALL) Reform.

 <p align="center">       
![gvy](https://user-images.githubusercontent.com/101227638/173213088-534522cf-e194-4e59-9ee2-1fa302f37909.png) align="center"
</p>

**Transform-** 
Data cleaning involved: transformation of data columns into datetime, filtering to limit the data to the time period we wanted to examine (2016), selecting the columns relevant to future analysis, changing formatting for ease of use and legibility, and serializing the data.  

![gvtables](https://user-images.githubusercontent.com/101227638/173212969-9f929078-7d69-4e7d-9d27-ecf33c029d46.png)


**Load-** 
We then loaded the results into four Postgres Tables: FBI NICS, Incidents, Participants, and Incident URLS.  We joined FIB NICS and Incidents along the date parameter, Incidents and Participants along the IncidentID parameter, and Participants and Incidents URLS along the IncidentID parameter, as well.  

![gvpost](https://user-images.githubusercontent.com/101227638/173212929-4c309401-d093-4c8c-9908-d61b37741264.png)

Please reference the included “Gun Violence ETL.png” for a visualization of this overall process.  Please also reference the included “Technical Report” for a more detailed explanations.


OurWBS was as follows:

•	Initialize the repository, add files and folders.

•	Locate appropriate datasets, and extract data using JuPyter notebook and pandas.  

•	Transform the data, combine, and store into a dataframe.

•	Load the data with the local databases and check tables into PostgreSQL.

•	Load the data with local database and check tables into and join with PostgreSQL in PgAdmin.
