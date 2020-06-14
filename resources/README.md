# Temat projektu
Tematem projektu jest Eurowizja. Projekt bazy Eurowizji został wykonany w ramach ćwiczeń projektowych z Baz Danych.

| Nazwisko i imię        | Wydział | Kierunek | Semestr | Grupa | Rok akademicki |
| :--------------------: | :-----: | :------: | :-----: | :---: | :------------: |
| Jop Karolina           | WIMiIP  | IS       |   4     | 3     | 2019/2020      |
| Kocurek Magdalena      | WIMiIP  | IS       |   4     | 3     | 2019/2020      |

## Projekt bazy danych

DIAGRAM ERD - Eurowizja 2017-2019
![eurowizja diagram](Eurowizja.svg)

Baza danych eurowizja pozwala na znalezienie informacji o uczestnikach konkursu: kto i kiedy brał udział, z jakiego kraju pochodzi, co zaśpiewał, czy był w półfinałach, ile punktów otrzymał w każdym etapie eliminacji, kto wygrał. Dodatkowo z bazy można się dowiedzieć: w jakim mieście odbywał sie konkurs, jaki slogan był w danym roku oraz dokładne daty kiedy odbywały się wszystkie eliminacje.
Prezentowanie działania bazy opiera się na informacjach z ostatnich trzech lat konkursu. 

Schemat bazy danych został zaprezentowany powyżej za pomocą diagramu ERD (utworzony na platformie draw.io). Baza składa się z siedmiu tabel (w każdej tabeli znajduje się klucz główny).


#### Relacje w bazie
Jednemu uczestnikowi konkursu przypisana jest konkretnie jedna piosenka co przedstawia relacja jeden do jeden pomiędzy uczestnikami a piosenkami.

Do jednego uczestnika przypisany jest konkretnie jeden kraj, ale z powodu, że konkurs odbywa się co roku to jeden kraj może być przypisany do wielu uczestników (zostało to zaprezentowane za pomocą relacji jeden do wielu pomiędzy tabelą kraje a uczestnicy).

Tabela roczniki zawiera informacje odnośnie roku, w którym odbywała się Eurowizja, czyli jaki był slogan konkursu w danym roku, w jakim mieście odbywał się konkurs, kto zwyciężył i jaką piosenką.
Relacja jeden do wielu między tabelami roczniki a piosenki przedstawia, że dana piosenka może wygrać tylko w jednym roku, ale wiele piosenek może być wykonanych w konkretnym roku. 

W przypadku relacji tabel roczniki - uczestnicy (relacja jeden do wielu) w jednym roku może wziąć udział wielu uczestników, ale tylko jeden uczestnik może wygrać w danym roku. 

Połączenie tabeli roczniki i daty relacją jeden do wielu obrazuję, że w danym roku może być kilka daty (data połfinału 1, półfinału 2 i finału), a jedna data może wystąpić w konkretnie jednym roku.

Relacja pomiędzy uczestnikami a wynikami jest relacją wiele do wielu dlatego odbywa się za pomocą tabeli pomocniczej eliminacje (ze względu na łatwiejszy sposób implementacji). Dzięki takiemu zabiegowi jednemu uczestnikowi mogą być przypisane dwa wyniki (ten uzyskany w półfinałach i ten, który uzyskał w finale). 
Z powodu, że tabela eliminacje jest tabelą pomocniczą to oprócz agregowania w niej informacji o uczestnikach i uzyskanych przez nich wynikach zawiera ona informację, w którym roku uczestnik uzyskał dany wynik, jaki to był etap eliminacji i dzień, w którym dana eliminacja się odbyła.

Można uzyskać informację czy dany uczestnik był w półfinale i czy zakwalifikował się dalej. Zatem relacja pomiędzy tabelą wyniki a eliminacje informuje, że jeden wynik, może być przypisany do kilku etapów eliminacji, tak samo relacja pomiędzy uczestnikami a eliminacjami, gdzie jeden uczestnik może wziąć udział w kilku etapach eliminacji.


#### Przykładowe zapytania z grupy DDL

Tworzenie tabeli 'roczniki' z kluczem głównym rok_id

```sql
CREATE TABLE roczniki (
    rok_id int NOT NULL AUTO_INCREMENT,
    rok int,
    slogan varchar (50),
    miasto_host varchar (50),
    uczestnik_id int,
    piosenka_id int, 

    PRIMARY KEY(rok_id)
);
```

Tworzenie tabeli 'uczestnicy' z gluczem głównym uczestnik_id 
```sql
CREATE TABLE uczestnicy (
    uczestnik_id int NOT NULL AUTO_INCREMENT,
    uczestnik varchar (50),
    kraj_id int,
    piosenka_id int,
    rok_id int,

    PRIMARY KEY(uczestnik_id)
);
```

Tworzenie tabeli pomocniczej 'eliminacje'
```sql
CREATE TABLE eliminacje (
    eliminacje_id int NOT NULL AUTO_INCREMENT,
    etap varchar (50),
    uczestnik_id int,
    wynik_id int,
    daty_id int,
    rok_id int,

    PRIMARY KEY(eliminacje_id)
);
```


Dołączenie do tabeli 'uczestnicy' kluczy obcych rok_id oraz kraj_id
```sql
ALTER TABLE uczestnicy ADD CONSTRAINT uczestnik_rocznik_fk FOREIGN KEY(rok_id) REFERENCES roczniki(rok_id);

ALTER TABLE uczestnicy ADD CONSTRAINT uczestnik_kraj_fk FOREIGN KEY(kraj_id) REFERENCES kraje(kraj_id);
```


## Implementacja zapytań SQL
Tutaj należy wylistować wszystkie funkcjonalności, wraz z odpowiednimi zapytaniami SQL. W tej sekcji należy zawrzeć wyłącznie zapytania z grupy DML oraz DQL.

### Zapytania grupy DML - dodawanie wartości do rekordów w tabelach
1. Dodanie do tabeli "roczniki" wartości
```sql
INSERT INTO roczniki (rok, slogan, miasto_host) VALUES 
('2017', 'Celebrate Diversity', 'Kijów'), 
('2018', 'All Aboard!', 'Lizbona'), 
('2019', 'Dare to Dream', 'Tel Awiw-Jafa')
```

2. Dodanie do tabeli "daty" daty połfinałów 1, połfinałów 2 i finałów
```sql
INSERT INTO daty (data_, rok_id) VALUES 
('9 maj', '1'), ('8 maj', '2'), ('14 maj','3'), 
('11 maj','1'), ('10 maj','2'), ('16 maj','3'),
('13 maj','1'), ('12 maj','2'), ('18 maj','3');
```
4. Dodanie wartości do tabeli 'uczestnicy'
```sql
INSERT INTO uczestnicy (uczestnik, kraj_id, rok_id, piosenka_id) VALUES
('Tamara Gaczecziladze', '13', '1', '1'), ('Lindita', '29', '1', '2'), ('Slavko Kalezić', '17', '1', '3'), ('Norma John', '34', '1', '4'), ('Svala', '2', '1', '5'), 
('Martina Bárta', '31', '1', '6'),  ('Omar Naber', '20', '1', '7'), ('Triana Park', '16', '1', '8'), ('Tijana Bogićević', '27', '1', '9'), ("Jana Burčeska", '5', '1', '10'), 
('Claudia Faniello', '15', '1', '11'), ('Brendan Murray', '41', '1', '12'), ('Valentina Monetta i Jimmie Wilson', '11', '1', '13'),  ('Timebelle', '9', '1', '14'), ('Koit Toome and Laura', '23', '1', '15'),  
('IMRI', '39', '1', '16'), ("Kasia Moś", "14", '1', '17'), ('Naviband', "4", '1', '18'), ('Nathan Trent', '22', '1', '19'), ('Artsvik', '8', '1', '20'), 
('OG3NE', '40', '1', '21'), ('Sunstroke Project', '36', '1', '22'),  ('Joci Pápai', '38', '1', '23'), ('Francesco Gabbani', '43', '1', '24'), ('Anja', '32', '1', '25'), 
('Salvador Sobral', '25', '1', '26'),  ('Dihaj', '1', '1', '27'), ('Jacques Houdek', '6', '1', '28'), ('Isaiah', '33', '1', '29'),('Demy', '7', '1', '30'), 
('Manel Navarro', '19', '1', '31'),  ('JOWST', '24', '1', '32'), ('Lucie Jones', '26', '1', '33'), ('Hovig', '42', '1', '34'), ('Ilinca ft. Alex Florea', '10', '1', '35'),  
('Levina', '28', '1', '36'), ('O.Torvald', '18', '1', '37'), ('Blanche', '3', '1', '38'), ('Robin Bengtsson', '37', '1', '39'),  ('Kristian Kostov', '35', '1', '40'), 
('Alma', '30', '1', '41'), ('Fusedmarc', '21', '1', '42');
```

3. Zmiana danych w tabeli "roczniki" (zmiana z NULL na konkretną wartość)
```sql
UPDATE roczniki SET uczestnik_id = 26 WHERE rok_id = 1;
UPDATE roczniki SET piosenka_id = 26 WHERE rok_id = 1;

UPDATE roczniki SET uczestnik_id = 81 WHERE rok_id = 2;
UPDATE roczniki SET piosenka_id = 81 WHERE rok_id = 2;

UPDATE roczniki SET uczestnik_id = 112 WHERE rok_id = 3;
UPDATE roczniki SET piosenka_id = 112 WHERE rok_id = 3;
```


### Zapytania grupy DQL - funkcjonalności
#### Pierwszy poziom zapytań - ogólne, bez poziału na lata
1. Zwycięzcy Eurowizji w latach 2017-2019
```sql
SELECT 
    uczestnicy.uczestnik,
    piosenki.tytul,
    roczniki.rok
FROM roczniki
INNER JOIN uczestnicy
ON uczestnicy.uczestnik_id=roczniki.uczestnik_id
INNER JOIN piosenki
ON piosenki.piosenka_id=roczniki.piosenka_id
```

2. Ilość uczestników Eurowizji w poszczególnych latach (2017 - 2019)
```sql
SELECT
	roczniki.rok,
	COUNT(uczestnicy.uczestnik) AS ilosc_uczestnikow
FROM uczestnicy
INNER JOIN roczniki
ON uczestnicy.rok_id=roczniki.rok_id
GROUP BY uczestnicy.rok_id
```

3. Wszyscy uczestnicy, których piosenki są w innym języku niż angielski
```sql
SELECT 
	uczestnicy.uczestnik,
	piosenki.tytul,
    piosenki.jezyk
FROM uczestnicy
INNER JOIN piosenki
ON uczestnicy.piosenka_id=piosenki.piosenka_id
WHERE piosenki.jezyk != 'angielski'
```

4. Sprawdzenie ile razy państwo podane przez użytkownika brało udział w Eurowizji
  * wyświetlenie listy wszystkich państw
```sql    
SELECT kraje.kraj FROM kraje
```
  * następnie użytownik podaje kraj z listy i następuje obliczanie wystąpień danego państwa 
```sql
SELECT 
	COUNT(uczestnicy.uczestnik) as liczba_wystąpień
FROM uczestnicy
INNER JOIN kraje
ON uczestnicy.kraj_id = kraje.kraj_id
WHERE kraje.kraj = 'Bułgaria'
GROUP BY uczestnicy.kraj_id
```

#### Drugi poziom zapytań - z podziałem na lata (zmiana rok_id powoduje powoduje wykonanie zapytania w innym roku konkursu)

1. Pierwsze trojka rok 2017 
```sql
SELECT 
    	wyniki.punkty,
    	uczestnicy.uczestnik,
    	piosenki.tytul,
    	piosenki.jezyk,
    	kraje.kraj
FROM uczestnicy
INNER JOIN eliminacje
ON eliminacje.uczestnik_id=uczestnicy.uczestnik_id
INNER JOIN piosenki
ON piosenki.piosenka_id=uczestnicy.piosenka_id
INNER JOIN kraje
ON kraje.kraj_id=uczestnicy.kraj_id
INNER JOIN wyniki
ON wyniki.wynik_id=eliminacje.wynik_id
WHERE uczestnicy.rok_id=1
AND eliminacje.etap = 'finał'
ORDER BY wyniki.punkty DESC
LIMIT 3
```

2. Slogan i miasto goszczące rok 2017  (proste przeszukanie jednej tabeli)                                              
```sql
SELECT 
	roczniki.rok,
    roczniki.miasto_host,
    roczniki.slogan
FROM roczniki
WHERE roczniki.rok_id = 1
```

3. Kiedy odbył się finał, półfinał 1 i połfinał 2 w roku 2017
```sql
SELECT
	daty.data_,
	roczniki.rok
FROM daty
INNER JOIN roczniki
ON roczniki.rok_id=daty.rok_id
WHERE daty.rok_id=1
ORDER By daty.daty_id
```

4. Wszyscy uczestnicy w roku 2017 posortowani alfabetycznie 
```sql
SELECT 
	uczestnicy.uczestnik,
   	kraje.kraj
FROM uczestnicy
LEFT JOIN kraje
ON kraje.kraj_id=uczestnicy.kraj_id
WHERE uczestnicy.rok_id=1
ORDER BY uczestnicy.uczestnik
```

5. Wyświetlenie uczestników znajdujących się w półfinale 1 w roku 2017
```sql
SELECT
	roczniki.rok,
    uczestnicy.uczestnik,
    kraje.kraj
FROM uczestnicy
INNER JOIN roczniki
ON roczniki.rok_id=uczestnicy.rok_id
INNER JOIN kraje
ON kraje.kraj_id=uczestnicy.kraj_id
INNER JOIN eliminacje
ON eliminacje.uczestnik_id=uczestnicy.uczestnik_id
WHERE uczestnicy.rok_id = 1
AND eliminacje.etap = 'półfinał 1' 
```

6. Wyświetlenie uczestników znajdujących się w półfinale 2 w roku 2017
```sql
SELECT
	roczniki.rok,
    uczestnicy.uczestnik,
    kraje.kraj
FROM uczestnicy
INNER JOIN roczniki
ON roczniki.rok_id=uczestnicy.rok_id
INNER JOIN kraje
ON kraje.kraj_id=uczestnicy.kraj_id
INNER JOIN eliminacje
ON eliminacje.uczestnik_id=uczestnicy.uczestnik_id
WHERE uczestnicy.rok_id = 1
AND eliminacje.etap = 'półfinał 2'
```

7. Wyświetlenie uczestników znajdujących się w finale w roku 2017
```sql
SELECT
	roczniki.rok,
    uczestnicy.uczestnik,
    kraje.kraj
FROM uczestnicy
INNER JOIN roczniki
ON roczniki.rok_id=uczestnicy.rok_id
INNER JOIN kraje
ON kraje.kraj_id=uczestnicy.kraj_id
INNER JOIN eliminacje
ON eliminacje.uczestnik_id=uczestnicy.uczestnik_id
WHERE uczestnicy.rok_id = 1
AND eliminacje.etap = 'finał'
```

8. Ilość uczestników półfinału 1, półfinału 2 i finału
```sql
SELECT 
	COUNT(eliminacje.etap) AS ilość_uczestników
FROM eliminacje
WHERE eliminacje.etap = 'półfinał 1' AND eliminacje.rok_id = 1
UNION ALL
SELECT 
	COUNT(eliminacje.etap) AS ilość_uczestników
FROM eliminacje
WHERE eliminacje.etap = 'półfinał 2' AND eliminacje.rok_id = 1
UNION ALL
SELECT 
	COUNT(eliminacje.etap) AS ilość_uczestników
FROM eliminacje
WHERE eliminacje.etap = 'finał' AND eliminacje.rok_id = 1
```

9. Ilość uczestników Eurowizji rok 2017
```sql
SELECT 
	COUNT(uczestnicy.uczestnik) AS ilość_uczestników
FROM uczestnicy
WHERE rok_id=1
```

10. Sprawdzenie czy uczestnik dostał się do finału w roku 2017
  * wyświetlenie listy wszystkich uczestników z roku 2017
```sql
SELECT 
	uczestnicy.uczestnik
FROM uczestnicy
WHERE uczestnicy.rok_id = 1
```

  * użytkownik podaje uczestnika i następuje sprawdzenie za pomocą COUNT czy uczestnik jest w finale czy nie (jeśli liczba będzie równa 1 uczestnik jest w finale, a jeśli wyniesi 0, to oznacza, że uczestnik nie dostał sie do finału)
```sql
SELECT
	COUNT(uczestnicy.uczestnik) as punkt
FROM uczestnicy
INNER JOIN eliminacje
ON eliminacje.uczestnik_id = uczestnicy.uczestnik_id
WHERE uczestnicy.uczestnik = 'Kasia Moś'
AND eliminacje.etap = 'finał'
AND eliminacje.rok_id = 1
```

11. Wyświetlenie uczestników z największą i najmniejszą liczbą punktów uzyskanych w finale w roku 2017
  * największa liczba punktów
```sql
SELECT
	uczestnicy.uczestnik,
    wyniki.punkty as max_wynik,
    eliminacje.etap
FROM uczestnicy
INNER JOIN eliminacje
ON eliminacje.uczestnik_id = uczestnicy.uczestnik_id
INNER JOIN wyniki
ON eliminacje.wynik_id = wyniki.wynik_id
WHERE eliminacje.rok_id = 1
AND wyniki.punkty IN 
(SELECT 
	MAX(wyniki.punkty)
FROM wyniki
INNER JOIN eliminacje
ON eliminacje.wynik_id = wyniki.wynik_id
WHERE eliminacje.rok_id = 1
AND eliminacje.etap = 'finał')
```

  * najmniejsza liczba punktów
  ```sql
  SELECT
	uczestnicy.uczestnik,
    wyniki.punkty as min_wynik,
    eliminacje.etap
FROM uczestnicy
INNER JOIN eliminacje
ON eliminacje.uczestnik_id = uczestnicy.uczestnik_id
INNER JOIN wyniki
ON eliminacje.wynik_id = wyniki.wynik_id
WHERE eliminacje.rok_id = 1
AND wyniki.punkty IN 
(SELECT 
	MIN(wyniki.punkty)
FROM wyniki
INNER JOIN eliminacje
ON eliminacje.wynik_id = wyniki.wynik_id
WHERE eliminacje.rok_id = 1
AND eliminacje.etap = 'finał')
```

12. Uczestnicy biorący udział w Eurowizji spoza Europy
  * za pomocą INTERSECT (zapytanie nie działa z mysql)
```sql
SELECT kraje.kraj_id, kraje.kontynent, uczestnicy.uczestnik
FROM kraje
INNER JOIN uczestnicy
ON kraje.kraj_id = uczestnicy.kraj_id
WHERE kraje.kontynent != 'Europa'
INTERSECT
SELECT uczestnicy.kraj_id, kraje.kontynent, uczestnicy.uczestnik
FROM uczestnicy
INNER JOIN kraje
ON kraje.kraj_id = uczestnicy.kraj_id
WHERE uczestnicy.rok_id = 1;
```
  * mozna zamienić INTERSECT na INNER JOIN w przypadku, gdy MYSQL nie wspiera komendy INTERSECT
```sql
SELECT kraje.kraj_id, kraje.kontynent, uczestnicy.uczestnik
FROM kraje
INNER JOIN uczestnicy
ON kraje.kraj_id = uczestnicy.kraj_id
WHERE kraje.kontynent != 'Europa'
AND uczestnicy.rok_id = 1;
```
  
## Aplikacja
Aplikacja została napisania w języku Python z użyciem biblioteki PyMySQL. Do uruchomienia aplikacji wymagana jest instalacja biblioteki PyMySQL, biblioteki tabulate oraz zainstalowanie mysql-connector.
Przed uruchomieniem aplikacji należy najpierw załadować bazę do mysql.

DRZEWO INTERAKCJI
```java
// 1. Sprawdź kto wygrał w latach 2017-2019
    // Wyświetlenie zwycięzców w latach 2017 - 2019
// 2. Sprawdź ile uczestnikow brało udział w latach 2017-2019
    // Wyświetlenie liczby uczestników w poszczególnych latach
// 3. Pokaż wszystkich uczestników wykonujących piosenki nie w języku angielskim
    // Wyświetlenie uczestników i ich piosenki, które nie są wyłącznie w języku angielskim
// 4. Sprawdź ile razy dane państwo brało udział w konkursie
    // Wyświetlenie listy wszystkich państw
    // Wybierz państwo z listy
    // Wyświetlenie liczby wystąpień państwa w konkursie
// 5. Wybierz rok Eurowizji
    // 1. Pokaż pierwszą trójkę
        // Wyświetlenie trzech uczestników z największą liczbą punktów
    // 2. Pokaż slogan i miasto goszczące
        // Wyświetlenie sloganu i miasta goszczącego w danym roku
    // 3. Kiedy odbył się półfinał 1, półfinał 2 oraz finał? 
        // Wyświetlenie dokładnych dat poszczególnych eliminacji w danym roku
    // 4. Pokaż wszystkich uczestników w kolejności alfabetycznej. 
        // Wyświetlenie listy uczestników z danego roku w kolejności alfabetycznej
    // 5. Kto był w półfinale 1? 
        // Wyświetlenie listy uczestników z danego roku znajdujących się w półfinale 1
    // 6. Kto był w półfinale 2? 
        // Wyświetlenie listy uczestników z danego roku znajdujących się w półfinale 2
    // 7. Kto był w finale? 
        // Wyświetlenie listy uczestników z danego roku znajdujących się w finale
    // 8. Ile było uczestników półfinału 1, półfinału 2, finału?
        // Wyświetlenie informacji o liczbie uczestników z danego roku w każdym etapie eliminacji
    // 9. Ile było uczestników Eurowizji? 
        // Wyświetlenie liczby uczestników Eurowizji w danym roku
    // 10. Sprawdz, czy uczestnik dostał się do finału
        // Wyświetlenie listy wszystkich uczestników z danego roku
        // Wybierz uczestnika z listy
        // Sprawdzenie czy uczestnik jest w finale
        // Wyświetlenie komunikatu czy uczestnik dostał się do finału czy nie
    // 11. Pokaz kto miał największą i najmniejszą liczbę punktów w finale
        // Wyświetlenie uczestnika z największą liczą punktów w danym roku
        // Wyświetlenie uczestnika z najmniejszą liczą punktów w danym roku
    // 12. Pokaz uczestników eurowizji spoza Europy
    	// Wyświetlenie listy uczestników przypisanych do kraju nie znajdującego się na kontynencie europejskim
// 6. Wyjdź z programu
    // przerwanie nieskończonej pętli i zakończenie działania programu
    // break
```

W zależności od wyboru dokonanego przez użytkownika wywoływana jest konkretna interakcja. Po każdej interakcji użytkownik otrzymuje pytanie, czy chce nadal korzystać z programu, czy zakończyć jego działanie. Wybranie przez użytkownika zakończenia działania programu przerywa nieskończoną pętle i kończy działanie programu.

## Dodatkowe uwagi
Aby pokazać pełne możliwości bazy danych, zaimplementowano wszystkie potrzebne wiadomości z ostatnich trzech lat konkursu. Dzięki temu można uzyskać prawdziwe informacje o tym jak wyglądał konkurs.
