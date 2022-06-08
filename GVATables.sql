-- Basic table layout for GVA source data 

CREATE TABLE "Incident" (
    "IncidentID" int  NOT NULL,
    "Date" date   NOT NULL,
    "State" varchar(20)  NOT NULL,
    "Jurisiction" varchar(20),
    "Address" varchar(20),
    "No_Killed" int,
    "No_injured" int,
    "House_District" int,
    "Senate_District" int,
    CONSTRAINT "pk_Incident" PRIMARY KEY (
        "IncidentID"
     )
);

CREATE TABLE "Participants" (
    "ParticipantID" SERIAL,
    "IncidentID" int not NULL,
    "Age_group" varchar(10),
    "Gender" varchar(10),
    "Name" varchar(30),
    "Realationship" varchar(30),
    "Status" varchar(20),
    "Type" varchar(20),
    CONSTRAINT "pk_Participants" PRIMARY KEY (
        "ParticipantID"
     )
);

CREATE TABLE "Incident_urls" (
    "IncidentID" int  NOT NULL,
    "IncidentUrl" varchar(50),
    "SourceUrl" varchar(50), 
    "SourcesUrl" varchar(50), 
    CONSTRAINT "pk_Incident_urls" PRIMARY KEY (
        "IncidentID"
     )
);

ALTER TABLE "Incident" ADD CONSTRAINT "fk_IncidentID" FOREIGN KEY("IncidentID")
REFERENCES "Participants" ("IncidentID");


-- May not be able to implement this contraint may not have and entry for each incident (could force and entry)
ALTER TABLE "Incident" ADD CONSTRAINT "fk_IncidentID_urls" FOREIGN KEY("IncidentID")
REFERENCES "Incident_urls" ("IncidentID");

