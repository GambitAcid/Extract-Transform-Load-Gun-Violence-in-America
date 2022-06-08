drop Table if exists "Mass_Shootings";
CREATE TABLE "Mass_Shootings" (
    "Incident_ID" int   NOT NULL,
	"Incident_Date" date   NOT NULL,
    "State" varchar(50)   NOT NULL,
    "CityorCountry" varchar(100)   NOT NULL,
	"Address" varchar(500)   NOT NULL,
    "Num_Killed" int   NOT NULL,
    "Num_Injured" int   NOT NULL,
	"Operations" text  NOT NULL,
    CONSTRAINT "pk_Mass_Shootings" PRIMARY KEY (
        "Incident_ID"
     )
);
Select * from "Mass_Shootings" as MS

drop Table if exists "Mass_Shootings_2016";
CREATE TABLE "Mass_Shootings_2016" (
    "Incident_ID" int   NOT NULL,
	"Incident_Date" date   NOT NULL,
    "State" varchar(50)    NOT NULL,
    "CityorCountry" varchar(100)   NOT NULL,
	"Address" varchar(500)   NOT NULL,
    "Num_Killed" int    NOT NULL,
    "Num_Injured" int   NOT NULL,
	"Operations" text   NOT NULL,
    CONSTRAINT "pk_Mass_Shootings_2016" PRIMARY KEY (
        "Incident_ID"
     )
);
Select * from "Mass_Shootings_2016" as MS16

drop Table if exists "Accidental_Deaths";
CREATE TABLE "Accidental_Deaths" (
    "Incident_Date" date   NOT NULL,
    "State" varchar(50)   NOT NULL,
    "CityorCountry" varchar(100) NOT NULL,
	"Address" varchar(500) NOT NULL,
    "Num_Killed" int    NOT NULL,
    "Num_Injured" int   NOT NULL,
	"Operations" text   NOT NULL,
    CONSTRAINT "pk_Accidental_Deaths" PRIMARY KEY (
        "Incident_Date"
     )
);
Select * from "Accidental_Deaths" as AD

drop Table if exists "Accidental_Injuries";
CREATE TABLE "Accidental_Injuries" (
    "Incident_Date" date   NOT NULL,
    "State" varchar(50)   NOT NULL,
    "CityorCountry" varchar(100)   NOT NULL,
	"Address" varchar(500)   NOT NULL,
    "No_Killed" int   NOT NULL,
    "No_Injured" int   NOT NULL,
	CONSTRAINT "pk_Accidental_Injuries" PRIMARY KEY (
        "Incident_Date"
     )
);
Select * from "Accidental_Injuries" as AI

drop Table if exists "GVA_16";
CREATE TABLE "GVA_16" (
    "Incident_ID" int   NOT NULL,
    "Incident_Date" date   NOT NULL,
    "State" varchar(50)   NOT NULL,
    "CityorCountry" varchar(100)   NOT NULL,
    "n_Killed" int   NOT NULL,
    "n_Injured" int   NOT NULL,
	"gun_type" varchar(20) NOT Null,
    CONSTRAINT "pk_GVA16" PRIMARY KEY (
        "Incident_ID"
     )
);
Select * from "GVA_16" as GV

drop Table if exists "FBI_NICS";
CREATE TABLE "FBI_NICS" (
    "ID" int   NOT NULL,
    "Date" date   NOT NULL,
    "State" varchar(50)   NOT NULL,
    "Handgun" varchar(10)   NOT NULL,
    "Longgun" varchar(10)   NOT NULL,
    "Multiples" int   NOT NULL,
	"Totals" int NOT Null,
    CONSTRAINT "pk_FBI_NICS" PRIMARY KEY (
        "ID"
     )
);

Select * from "FBI_NICS" as FBI