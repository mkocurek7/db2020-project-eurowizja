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

-- półfinał 1
INSERT INTO eliminacje (etap, uczestnik_id, wynik_id, rok_id, daty_id) VALUES
('półfinał 1', '1', '1', '1', '1'), ('półfinał 1', '2', '2', '1', '1'), ('półfinał 1', '3', '3', '1', '1'), ('półfinał 1', '4', '4', '1', '1'), ('półfinał 1', '5', '5', '1', '1'), 
('półfinał 1', '6', '6', '1', '1'), ('półfinał 1', '7', '7', '1', '1'), ('półfinał 1', '8', '8', '1', '1'), ('półfinał 1', '39', '9', '1', '1'), ('półfinał 1', '19', '10', '1', '1'), 
('półfinał 1', '38', '11', '1', '1'), ('półfinał 1', '30', '12', '1', '1'), ('półfinał 1', '27', '13', '1', '1'), ('półfinał 1', '26', '14', '1', '1'), ('półfinał 1', '34', '15', '1', '1'), 
('półfinał 1', '17', '16', '1', '1'), ('półfinał 1', '22', '17', '1', '1'), ('półfinał 1', '20', '18', '1', '1'), ('półfinał 1', '43', '58', '2', '2'), ('półfinał 1', '44', '59', '2', '2'), 
('półfinał 1', '45', '60', '2', '2'), ('półfinał 1', '46', '61', '2', '2'), ('półfinał 1', '47', '62', '2', '2'), ('półfinał 1', '48', '11', '2', '2'), ('półfinał 1', '49', '63', '2', '2'), 
('półfinał 1', '50', '64', '2', '2'), ('półfinał 1', '51', '65', '2', '2'), ('półfinał 1', '71', '66', '2', '2'), ('półfinał 1', '73', '67', '2', '2'), ('półfinał 1', '63', '68', '2', '2'), 
('półfinał 1', '81', '25', '2', '2'), ('półfinał 1', '77', '69', '2', '2'), ('półfinał 1', '65', '70', '2', '2'), ('półfinał 1', '76', '40', '2', '2'), ('półfinał 1', '83', '27', '2', '2'), 
('półfinał 1', '84', '71', '2', '2'), ('półfinał 1', '64', '72', '2', '2'), ('półfinał 1', '86', '106', '3', '3'), ('półfinał 1', '87', '97', '3', '3'), ('półfinał 1', '88', '107', '3', '3'), 
('półfinał 1', '89', '45', '3', '3'), ('półfinał 1', '90', '108', '3', '3'), ('półfinał 1', '91', '109', '3', '3'), ('półfinał 1', '92', '31', '3', '3'), ('półfinał 1', '111', '110', '3', '3'), 
('półfinał 1', '103', '111', '3', '3'), ('półfinał 1', '110', '112', '3', '3'), ('półfinał 1', '119', '113', '3', '3'), ('półfinał 1', '123', '114', '3', '3'), ('półfinał 1', '125', '115', '3', '3'), 
('półfinał 1', '117', '116', '3', '3'), ('półfinał 1', '118', '117', '3', '3'), ('półfinał 1', '113', '118', '3', '3'), ('półfinał 1', '107', '8', '3', '3');
