-- Basic table layout for GVA source data 

CREATE TABLE "Incident" (
    "IncidentID" int  NOT NULL,
    "Date" date   NOT NULL,
    "State" varchar(20)  NOT NULL,
    "Jurisiction" varchar(20),
    "Address" (20),
    "No_Killed" int,
    "No_injured" int,
    "IncidentUrl" varchar(50),
    "SourceUrl" varchar(50), 
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
    "Status" varchar(20),
    "Type" varchar(20)
    CONSTRAINT "pk_Participants" PRIMARY KEY (
        "ParticipantID"
     )
);



ALTER TABLE "Employees" ADD CONSTRAINT "fk_IncidentID" FOREIGN KEY("IncidentID")
REFERENCES "Participants" ("IncidentID");

