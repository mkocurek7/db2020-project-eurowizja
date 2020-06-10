DROP DATABASE IF EXISTS eurowizja;
CREATE DATABASE eurowizja COLLATE = utf8_general_ci;
USE eurowizja;

CREATE TABLE roczniki (
    rok_id int NOT NULL AUTO_INCREMENT,
    rok int,
    slogan varchar (50),
    miasto_host varchar (50),
    kraj_id int,
    uczestnik_id int, /* id tego uczestnika, który wygrał */
    piosenka_id int, /* id zwycięzkiej piosenki */

    PRIMARY KEY(rok_id)
);

CREATE TABLE uczestnicy (
    uczestnik_id int NOT NULL AUTO_INCREMENT,
    uczestnik varchar (50),
    kraj_id int,
    piosenka_id int,
    rok_id int,

    PRIMARY KEY(uczestnik_id)
);

CREATE TABLE kraje (
    kraj_id int NOT NULL AUTO_INCREMENT,
    kraj varchar(50),
    stolica varchar (50),
    kontynent varchar (50),

    PRIMARY KEY(kraj_id)
);

CREATE TABLE piosenki (
    piosenka_id int NOT NULL AUTO_INCREMENT,
    tytul varchar(50),
    jezyk varchar(50),
    uczestnik_id int,
    rok_id int,

    PRIMARY KEY(piosenka_id)
);

CREATE TABLE wyniki (
    wynik_id int NOT NULL AUTO_INCREMENT,
    punkty int,
    
    PRIMARY KEY(wynik_id)
);


CREATE TABLE eliminacje (
    eliminacje_id int NOT NULL AUTO_INCREMENT,
    etap varchar (50),
    /* etapem moze byc połfinal1, półfinał2 lub finał */
    uczestnik_id int,
    wynik_id int,
    daty_id int,
    rok_id int,

    PRIMARY KEY(eliminacje_id)
);


CREATE TABLE daty (
    daty_id int NOT NULL AUTO_INCREMENT,
    data_ varchar (50),
    rok_id int,

    PRIMARY KEY(daty_id)
);

INSERT INTO roczniki (rok, slogan, miasto_host, kraj_id) VALUES ('2017', 'Celebrate Diversity', 'Kijów','18'), ('2018', 'All Aboard!', 'Lizbona', '25'), ('2019', 'Dare to Dream', 'Tel Awiw-Jafa', '39');

