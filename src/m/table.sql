DROP TABLE IF EXISTS service;
DROP TABLE IF EXISTS contrat;
DROP TABLE IF EXISTS voiture;
DROP TABLE IF EXISTS client;
DROP TABLE IF EXISTS abonnement;
DROP TABLE IF EXISTS placement;
DROP TABLE IF EXISTS place;
DROP TABLE IF EXISTS parking;
DROP TABLE IF EXISTS typePlace;

CREATE TABLE parking (
    idParking INTEGER PRIMARY KEY,
    nom VARCHAR(30),
    actif INTEGER(1) DEFAULT 1
 );


CREATE TABLE typePlace (
    idTypePlace INTEGER PRIMARY KEY,
    longueur INTEGER,
    hauteur INTEGER,
    nombre INTEGER,
    prix FLOAT,
    niveau INTEGER
);

CREATE TABLE place (
    idPlace INTEGER PRIMARY KEY,
    idParking INTEGER,
    idTypePlace INTEGER,
    numero INTEGER,
    estLibre INTEGER(1),
    estSuperAbo INTEGER(1),
    FOREIGN KEY (idParking) REFERENCES parking(idParking),
    FOREIGN KEY (idTypePlace) REFERENCES typePlace(idTypePlace)
);

CREATE TABLE placement (
    idPlacement VARCHAR(10) PRIMARY KEY,
    idVoiture INTEGER,
    idPlace INTEGER,
    debut TIMESTAMP,
    fin TIMESTAMP,
    FOREIGN KEY (idVoiture) REFERENCES voiture(idVoiture),
    FOREIGN KEY (idPlace) REFERENCES place(idPlace)
);


CREATE TABLE client (
    idClient VARCHAR(10) PRIMARY KEY,
    nom VARCHAR(20),
    prenom VARCHAR(20),
    adresse VARCHAR(50),
    typeAbonnement INTEGER
);

CREATE TABLE voiture (
    idVoiture INTEGER PRIMARY KEY,
    idClient VARCHAR(10),
    hauteur INTEGER,
    longueur INTEGER,
    imma  VARCHAR(10),
    estDansParking INTEGER(1)
);


CREATE TABLE service (
    idService INTEGER PRIMARY KEY,
    idClient VARCHAR(10),
    idPlacement VARCHAR(10),
    typeService INTEGER,
    dateDemande TIMESTAMP,
    dateService TIMESTAMP,
    dateRealisation TIMESTAMP
    FOREIGN KEY (idClient) REFERENCES client(idClient),
    FOREIGN KEY (idPlacement) REFERENCES placement(idPlacement)
);