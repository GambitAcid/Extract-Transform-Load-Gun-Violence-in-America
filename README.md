# Project-2
Extract, Transform, and Load: Project 2 Analysis of Gun Violence

Project Two: Extract, Transform, and Load

Due: Saturday June 11th 2022

Project Two: Data ETL on Shootings and Gun Violence in America

Group Members: Lynne Freilich, Ronnie Phillips, Corban Doran

Project Outline: Tragic mass shootings have plagued the United States of America for decades. With the absolute horrid recent school shooting at Robb Elementary School in Uvalde, Texas as well as the hundreds of other shootings that have happened at schools, work, at home, or just on the street we wanted to analyze gun violence in America. We want to find out if gun control laws should in fact be girded more tightly, as we will look at the FBI’s monthly NICs background check data to compare gun checks vs violence, and how these deliberate and malicious shootings stack up against accidental discharges and subsequent injuries or death. 

Questions to Answer: Does intentional and deliberate shootings (i.e. school, mass, murder) occur more than death resulting from accidental discharge and lack of gun safety?

Null Hypothesis: Mass shootings outweigh accidental discharges. 
H0: M in M = 0
Alternative Hypothesis: Accidental and lack of gun safety resulting murder outweighs mass shootings. 
HA1: M < 0

Data Sources: 
https://www.kaggle.com/datasets/konivat/us-gun-violence-archive-2014-2021
https://www.gunviolencearchive.org/reports (mass shootings ALL , accidental deaths ALL)
https://www.kaggle.com/datasets/gunviolencearchive/gun-violence-database
https://raw.githubusercontent.com/BuzzFeedNews/nics-firearm-background-checks/master/data/nics-firearm-background-checks.csv

Breakdown of Tasks: 
1.	Initializing repository, adding files and folders, getting data ready. 
2.	Extract Data using jupyter notebook and pandas. 
3.	Transforming the data and store into a data frame. 
4.	Load the data with local database and check tables into PostgresSQL and join with PgAdmin or Pandas with SQLAlchemy. 

