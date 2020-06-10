import os
import pymysql
from tabulate import tabulate

connection= pymysql.connect("localhost", "eurowizja", "eurowizja", "eurowizja")
cursor=connection.cursor()

#funkcjonalnosci
sql=" USE eurowizja"

# 1 poziom
sql1=" SELECT uczestnicy.uczestnik, piosenki.tytul, roczniki.rok FROM roczniki INNER JOIN uczestnicy ON uczestnicy.uczestnik_id=roczniki.uczestnik_id INNER JOIN piosenki ON piosenki.piosenka_id=roczniki.piosenka_id;"
sql2=" SELECT roczniki.rok, COUNT(uczestnicy.uczestnik) AS ilosc_uczestnikow FROM uczestnicy INNER JOIN roczniki ON uczestnicy.rok_id=roczniki.rok_id GROUP BY uczestnicy.rok_id;"
sql3=" SELECT uczestnicy.uczestnik, piosenki.tytul, piosenki.jezyk FROM uczestnicy INNER JOIN piosenki ON uczestnicy.piosenka_id=piosenki.piosenka_id WHERE piosenki.jezyk != 'angielski' "
sql4=" SELECT uczestnicy.uczestnik, piosenki.tytul, piosenki.jezyk FROM uczestnicy INNER JOIN piosenki ON uczestnicy.piosenka_id=piosenki.piosenka_id WHERE piosenki.jezyk != 'angielski' "

# dla 2019
sql1_1=" SELECT wyniki.punkty, uczestnicy.uczestnik, piosenki.tytul, piosenki.jezyk, kraje.kraj FROM uczestnicy INNER JOIN eliminacje ON eliminacje.uczestnik_id=uczestnicy.uczestnik_id INNER JOIN piosenki ON piosenki.piosenka_id=uczestnicy.piosenka_id INNER JOIN kraje ON kraje.kraj_id=uczestnicy.kraj_id INNER JOIN wyniki ON wyniki.wynik_id=eliminacje.wynik_id WHERE uczestnicy.rok_id=3 AND eliminacje.etap = 'finał' ORDER BY wyniki.punkty DESC LIMIT 3"
sql1_2=" SELECT roczniki.rok, roczniki.miasto_host, roczniki.slogan FROM roczniki WHERE roczniki.rok_id = 3"
sql1_3=" SELECT daty.data_, roczniki.rok FROM daty INNER JOIN roczniki ON roczniki.rok_id=daty.rok_id WHERE daty.rok_id=3 ORDER By daty.daty_id"
sql1_4=" SELECT uczestnicy.uczestnik, kraje.kraj FROM uczestnicy LEFT JOIN kraje ON kraje.kraj_id=uczestnicy.kraj_id WHERE uczestnicy.rok_id=3 ORDER BY uczestnicy.uczestnik "
sql1_5=" SELECT roczniki.rok, uczestnicy.uczestnik, kraje.kraj FROM uczestnicy INNER JOIN roczniki ON roczniki.rok_id=uczestnicy.rok_id INNER JOIN kraje ON kraje.kraj_id=uczestnicy.kraj_id INNER JOIN eliminacje ON eliminacje.uczestnik_id=uczestnicy.uczestnik_id WHERE uczestnicy.rok_id = 3 AND eliminacje.etap = 'półfinał 1' "
sql1_6=" SELECT roczniki.rok, uczestnicy.uczestnik, kraje.kraj FROM uczestnicy INNER JOIN roczniki ON roczniki.rok_id=uczestnicy.rok_id INNER JOIN kraje ON kraje.kraj_id=uczestnicy.kraj_id INNER JOIN eliminacje ON eliminacje.uczestnik_id=uczestnicy.uczestnik_id WHERE uczestnicy.rok_id = 3 AND eliminacje.etap = 'półfinał 2' "
sql1_7=" SELECT roczniki.rok, uczestnicy.uczestnik, kraje.kraj FROM uczestnicy INNER JOIN roczniki ON roczniki.rok_id=uczestnicy.rok_id INNER JOIN kraje ON kraje.kraj_id=uczestnicy.kraj_id INNER JOIN eliminacje ON eliminacje.uczestnik_id=uczestnicy.uczestnik_id WHERE uczestnicy.rok_id = 3 AND eliminacje.etap = 'finał' "
sql1_8=" SELECT COUNT(eliminacje.etap) AS ilość_uczestników FROM eliminacje WHERE eliminacje.etap = 'półfinał 1' AND eliminacje.rok_id = 3 UNION ALL SELECT COUNT(eliminacje.etap) AS ilość_uczestników FROM eliminacje WHERE eliminacje.etap = 'półfinał 2' AND eliminacje.rok_id = 3 UNION ALL SELECT COUNT(eliminacje.etap) AS ilość_uczestników FROM eliminacje WHERE eliminacje.etap = 'finał' AND eliminacje.rok_id = 3"
sql1_9=" SELECT COUNT(uczestnicy.uczestnik) AS ilość_uczestników FROM uczestnicy WHERE rok_id=3 "
sql1_10=" SELECT uczestnicy.uczestnik FROM uczestnicy WHERE uczestnicy.rok_id = 3 "
sql1_11a=" SELECT uczestnicy.uczestnik, wyniki.punkty as max_wynik, eliminacje.etap FROM uczestnicy INNER JOIN eliminacje ON eliminacje.uczestnik_id = uczestnicy.uczestnik_id INNER JOIN wyniki ON eliminacje.wynik_id = wyniki.wynik_id WHERE eliminacje.rok_id = 3 AND wyniki.punkty IN (SELECT MAX(wyniki.punkty) FROM wyniki INNER JOIN eliminacje ON eliminacje.wynik_id = wyniki.wynik_id WHERE eliminacje.rok_id = 3 AND eliminacje.etap = 'finał') "
sql1_11b=" SELECT uczestnicy.uczestnik, wyniki.punkty as min_wynik, eliminacje.etap FROM uczestnicy INNER JOIN eliminacje ON eliminacje.uczestnik_id = uczestnicy.uczestnik_id INNER JOIN wyniki ON eliminacje.wynik_id = wyniki.wynik_id WHERE eliminacje.rok_id = 3 AND wyniki.punkty IN (SELECT MIN(wyniki.punkty) FROM wyniki INNER JOIN eliminacje ON eliminacje.wynik_id = wyniki.wynik_id WHERE eliminacje.rok_id = 3 AND eliminacje.etap = 'finał') "

