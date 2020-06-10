/****************************** zapytania do programu *****************************/

-- kto wygrał eurowizje w latach 2017-2019
SELECT 
	uczestnicy.uczestnik,
    piosenki.tytul,
    roczniki.rok
FROM roczniki
INNER JOIN uczestnicy
ON uczestnicy.uczestnik_id=roczniki.uczestnik_id
INNER JOIN piosenki
ON piosenki.piosenka_id=roczniki.piosenka_id;







-- pokaz wszystkich uczestników, których piosenki są w innym języku niz angielski
SELECT 
	uczestnicy.uczestnik,
	piosenki.tytul,
    piosenki.jezyk
FROM uczestnicy
INNER JOIN piosenki
ON uczestnicy.piosenka_id=piosenki.piosenka_id
WHERE piosenki.jezyk != 'angielski';





-- 1
-- pierwsze trojka rok 2017
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
WHERE uczestnicy.rok_id=1 AND eliminacje.etap = 'finał'
ORDER BY wyniki.punkty DESC
LIMIT 3;


-- pierwsze trojka rok 2018
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
WHERE uczestnicy.rok_id=2 AND eliminacje.etap = 'finał'
ORDER BY wyniki.punkty DESC
LIMIT 3;

-- pierwsze trojka rok 2019
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
WHERE uczestnicy.rok_id=3 AND eliminacje.etap = 'finał'
ORDER BY wyniki.punkty DESC
LIMIT 3;



