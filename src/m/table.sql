CREATE TABLE parking (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(30),
    );

CREATE TABLE place (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    idParking INT UNSIGNED FOREIGN KEY,
    idType INT UNSIGNED FOREIGN KEY,
    niveau INT UNSIGNED,
    numero INT UNSIGNED
);

CREATE TABLE typePlace (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    longueur INT UNSIGNED,
    hauteur INT UNSIGNED,
    largeur INT UNSIGNED,
    estLibre INT(1),
    estSuperAbo int(1)
);



CREATE TABLE placement (

);