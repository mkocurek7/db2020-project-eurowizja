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









-- półfinał 2
INSERT INTO eliminacje (etap, uczestnik_id, wynik_id, rok_id, daty_id) VALUES
('półfinał 2', '9', '19', '1', '4'), ('półfinał 2', '10', '20', '1', '4'), ('półfinał 2', '11', '21', '1', '4'), ('półfinał 2', '12', '22', '1', '4'), ('półfinał 2', '13', '23', '1', '4'), 
('półfinał 2', '14', '24', '1', '4'), ('półfinał 2', '15', '25', '1', '4'), ('półfinał 2', '42', '26', '1', '4'), ('półfinał 2', '19', '27', '1', '4'), ('półfinał 2', '21', '28', '1', '4'), 
('półfinał 2', '35', '29', '1', '4'), ('półfinał 2', '23', '30', '1', '4'), ('półfinał 2', '25', '31', '1', '4'), ('półfinał 2', '28', '32', '1', '4'), ('półfinał 2', '32', '33', '1', '4'), 
('półfinał 2', '18', '34', '1', '4'), ('półfinał 2', '40', '35', '1', '4'), ('półfinał 2', '16', '36', '1', '4'), ('półfinał 2', '52', '73', '2', '5'), ('półfinał 2', '53', '74', '2', '5'), 
('półfinał 2', '54', '75', '2', '5'), ('półfinał 2', '55', '76', '2', '5'), ('półfinał 2', '56', '77', '2', '5'), ('półfinał 2', '57', '64', '2', '5'), ('półfinał 2', '58', '78', '2', '5'), 
('półfinał 2', '59', '23', '2', '5'), ('półfinał 2', '66', '79', '2', '5'), ('półfinał 2', '69', '67', '2', '5'), ('półfinał 2', '74', '69', '2', '5'), ('półfinał 2', '78', '26', '2', '5'), 
('półfinał 2', '82', '80', '2', '5'), ('półfinał 2', '75', '81', '2', '5'), ('półfinał 2', '79', '82', '2', '5'), ('półfinał 2', '80', '83', '2', '5'), ('półfinał 2', '60', '84', '2', '5'), 
('półfinał 2', '62', '71', '2', '5'), ('półfinał 2', '93', '119', '3', '6'), ('półfinał 2', '94', '120', '3', '6'), ('półfinał 2', '95', '35', '3', '6'), ('półfinał 2', '96', '62', '3', '6'), 
('półfinał 2', '97', '121', '3', '6'), ('półfinał 2', '98', '122', '3', '6'), ('półfinał 2', '99', '58', '3', '6'), ('półfinał 2', '100', '123', '3', '6'), ('półfinał 2', '106', '18', '3', '6'), 
('półfinał 2', '109', '38', '3', '6'), ('półfinał 2', '124', '124', '3', '6'), ('półfinał 2', '101', '39', '3', '6'), ('półfinał 2', '102', '125', '3', '6'), ('półfinał 2', '105', '126', '3', '6'), 
('półfinał 2', '115', '127', '3', '6'), ('półfinał 2', '112', '128', '3', '6'), ('półfinał 2', '108', '129', '3', '6'), ('półfinał 2', '120', '130', '3', '6');











-- tabela zawiera wszystkie wyniki z połfinałó i finałów 
INSERT INTO wyniki (punkty) VALUES
('227'), ('99'), ('160'), ('76'), ('165'), ('56'), ('92'), ('150'), ('370'), ('115'), 
('119'), ('291'), ('60'), ('83'), ('164'), ('152'), ('36'), ('21'), ('98'), ('147'), 
('69'), ('55'), ('174'), ('200'), ('231'), ('101'), ('86'), ('1'), ('141'), ('189'), 
('97'), ('110'), ('403'), ('42'), ('85'), ('207'), ('39'), ('64'), ('93'), ('79'), 
('374'), ('334'), ('77'), ('758'), ('120'), ('128'), ('173'), ('5'), ('158'), ('111'), 
('68'), ('282'), ('6'), ('363'), ('344'), ('615'), ('135'), ('94'), ('15'), ('162'), 
('91'), ('232'), ('283'), ('65'), ('201'), ('177'), ('24'), ('63'), ('81'), ('108'), 
('179'), ('262'), ('266'), ('107'), ('117'), ('28'), ('204'), ('235'), ('212'), ('11'), 
('106'), ('254'), ('40'), ('132'), ('130'), ('61'), ('181'), ('342'), ('245'), ('144'), 
('48'), ('113'), ('340'), ('184'), ('281'), ('226'), ('46'), ('166'), ('209'), ('274'), 
('529'), ('121'), ('136'), ('436'), ('308'), ('149'), ('23'), ('167'), ('242'), ('122'), 
('156'), ('70'), ('62'), ('261'), ('221'), ('198'), ('51'), ('185'), ('49'), ('16'), 
('50'), ('71'), ('238'), ('157'), ('217'), ('96'), ('210'), ('280'), ('239'), ('224'), 
('90'), ('24'), ('305'), ('105'), ('109'), ('498'), ('74'), ('35'), ('331'), ('31'), 
('302'), ('472'), ('89'), ('364'), ('284'), ('54');













-- wszystkie kraje biorące udział w eurowizji
INSERT INTO kraje (kraj, kontynent, stolica) VALUES
('Azerbejdżan', 'Europa', 'Baku'), ('Islandia', 'Europa', 'Reykjavík'), ('Belgia', 'Europa', 'Bruksela'), ('Białoruś', 'Europa', 'Mińsk'), ('Macedonia', 'Europa', 'Skopje'), 
('Chorwacja', 'Europa', 'Zagrzeb'), ('Grecja', 'Europa', 'Ateny'), ('Armenia', 'Europa', 'Yerevan'), ('Szwajcaria', 'Europa', 'Berno'), ('Rumunia', 'Europa', 'Bukareszt'), 
('San Marino', 'Europa', 'San Marino'), ('Rosja', 'Europa', 'Moskwa'), ('Gruzja', 'Europa', 'Tbilisi'), ('Polska', 'Europa', 'Warszawa'), ('Malta', 'Europa', 'Valletta'), 
('Łotwa', 'Europa', 'Ryga'), ('Czarnogóra', 'Europa', 'Podgorica'), ('Ukraina', 'Europa', 'Kijów'), ('Hiszpania', 'Europa', 'Madryt'), ('Słowenia', 'Europa', '‎Lublana'), 
('Litwa', 'Europa', 'Wilno'), ('Austria', 'Europa', 'Wiedeń'), ('Estonia', 'Europa', 'Talin'), ('Norwegia', 'Europa', 'Oslo'), ('Portugalia', 'Europa', 'Lizbona'), 
('Wielka Brytania', 'Europa', 'Londyn'), ('Serbia', 'Europa', 'Belgrad'), ('Niemcy', 'Europa', 'Berlin'), ('Albania', 'Europa', 'Tirana'), ('Francja', 'Europa', 'Paryż'), 
('Czechy', 'Europa', 'Praga'), ('Dania', 'Europa', 'Kopenhaga'), ('Australia', 'Australia', 'Canberra'), ('Finlandia', 'Europa', 'Helsinki'), ('Bułgaria', 'Europa', 'Sofia'), 
('Mołdawia', 'Europa', 'Kiszyniów'), ('Szwecja', 'Europa', 'Sztokholm'), ('Węgry', 'Europa', 'Budapeszt'), ('Izrael', 'Europa', 'Jerozolima'), ('Holandia', 'Europa', 'Amsterdam‎'), 
('Irlandia', 'Europa', 'Dublin'), ('Cypr', 'Europa', 'Nikozja'), ('Włochy', 'Europa', 'Rzym');



