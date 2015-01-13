DROP TABLE IF EXISTS service;
DROP TABLE IF EXISTS contrat;
DROP TABLE IF EXISTS client;
DROP TABLE IF EXISTS abonnement;
DROP TABLE IF EXISTS placement;
DROP TABLE IF EXISTS voiture;
DROP TABLE IF EXISTS place;
DROP TABLE IF EXISTS parking;
DROP TABLE IF EXISTS typePlace;



CREATE TABLE parking (
    idParking INTEGER PRIMARY KEY ,
    nom VARCHAR(30)
    );


CREATE TABLE typePlace (
    idTypePlace INTEGER PRIMARY KEY ,
    longueur INTEGER ,
    hauteur INTEGER ,
    nombre INTEGER 
);

CREATE TABLE place (
    idPlace INTEGER   PRIMARY KEY ,
    idParking INTEGER ,
    idTypePlace INTEGER ,
    niveau INTEGER ,
    numero INTEGER ,
    estLibre INTEGER(1),
    estSuperAbo INTEGER(1),
    FOREIGN KEY (idParking) REFERENCES parking(id),
    FOREIGN KEY (idTypePlace) REFERENCES typePlace(id)
);

CREATE TABLE voiture (
    idVoiture INTEGER   PRIMARY KEY ,
    hauteur INTEGER ,
    longueur INTEGER ,
    imma  VARCHAR(10),
    estDansParking INTEGER(1)
);


CREATE TABLE placement (
    idPlacement VARCHAR(10) PRIMARY KEY ,
    idVoiture INTEGER ,
    idPlace INTEGER ,
    debut DATE,
    fin DATE,
    FOREIGN KEY (idVoiture) REFERENCES voiture(id),
    FOREIGN KEY (idPlace) REFERENCES place(id)
);


CREATE TABLE client (
    idClient VARCHAR(10) PRIMARY KEY ,
    nom VARCHAR(20),
    prenom VARCHAR(20),
    adresse VARCHAR(50),
    typeAbonnement INTEGER
);


CREATE TABLE service (
    idService INTEGER   PRIMARY KEY ,
    idClient VARCHAR(10),
    dateDemande DATE,
    dateService DATE,
    dateRealisation DATE,
    rapport VARCHAR(255),
    FOREIGN KEY (idClient) REFERENCES client(id)
);