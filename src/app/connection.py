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

#dla 2018
sql2_1=" SELECT wyniki.punkty, uczestnicy.uczestnik, piosenki.tytul, piosenki.jezyk, kraje.kraj FROM uczestnicy INNER JOIN eliminacje ON eliminacje.uczestnik_id=uczestnicy.uczestnik_id INNER JOIN piosenki ON piosenki.piosenka_id=uczestnicy.piosenka_id INNER JOIN kraje ON kraje.kraj_id=uczestnicy.kraj_id INNER JOIN wyniki ON wyniki.wynik_id=eliminacje.wynik_id WHERE uczestnicy.rok_id=3 AND eliminacje.etap = 'finał' ORDER BY wyniki.punkty DESC LIMIT 2"
sql2_2=" SELECT roczniki.rok, roczniki.miasto_host, roczniki.slogan FROM roczniki WHERE roczniki.rok_id = 2"
sql2_3=" SELECT daty.data_, roczniki.rok FROM daty INNER JOIN roczniki ON roczniki.rok_id=daty.rok_id WHERE daty.rok_id=2 ORDER By daty.daty_id"
sql2_4=" SELECT uczestnicy.uczestnik, kraje.kraj FROM uczestnicy LEFT JOIN kraje ON kraje.kraj_id=uczestnicy.kraj_id WHERE uczestnicy.rok_id=2 ORDER BY uczestnicy.uczestnik "
sql2_5=" SELECT roczniki.rok, uczestnicy.uczestnik, kraje.kraj FROM uczestnicy INNER JOIN roczniki ON roczniki.rok_id=uczestnicy.rok_id INNER JOIN kraje ON kraje.kraj_id=uczestnicy.kraj_id INNER JOIN eliminacje ON eliminacje.uczestnik_id=uczestnicy.uczestnik_id WHERE uczestnicy.rok_id = 2 AND eliminacje.etap = 'półfinał 1' "
sql2_6=" SELECT roczniki.rok, uczestnicy.uczestnik, kraje.kraj FROM uczestnicy INNER JOIN roczniki ON roczniki.rok_id=uczestnicy.rok_id INNER JOIN kraje ON kraje.kraj_id=uczestnicy.kraj_id INNER JOIN eliminacje ON eliminacje.uczestnik_id=uczestnicy.uczestnik_id WHERE uczestnicy.rok_id = 2 AND eliminacje.etap = 'półfinał 2' "
sql2_7=" SELECT roczniki.rok, uczestnicy.uczestnik, kraje.kraj FROM uczestnicy INNER JOIN roczniki ON roczniki.rok_id=uczestnicy.rok_id INNER JOIN kraje ON kraje.kraj_id=uczestnicy.kraj_id INNER JOIN eliminacje ON eliminacje.uczestnik_id=uczestnicy.uczestnik_id WHERE uczestnicy.rok_id = 2 AND eliminacje.etap = 'finał' "
sql2_8=" SELECT COUNT(eliminacje.etap) AS ilość_uczestników FROM eliminacje WHERE eliminacje.etap = 'półfinał 1' AND eliminacje.rok_id = 2 UNION ALL SELECT COUNT(eliminacje.etap) AS ilość_uczestników FROM eliminacje WHERE eliminacje.etap = 'półfinał 2' AND eliminacje.rok_id = 2 UNION ALL SELECT COUNT(eliminacje.etap) AS ilość_uczestników FROM eliminacje WHERE eliminacje.etap = 'finał' AND eliminacje.rok_id = 2"
sql2_9=" SELECT COUNT(uczestnicy.uczestnik) AS ilość_uczestników FROM uczestnicy WHERE rok_id=2 "
sql2_10=" SELECT uczestnicy.uczestnik FROM uczestnicy WHERE uczestnicy.rok_id = 2 "
sql2_11a=" SELECT uczestnicy.uczestnik, wyniki.punkty as max_wynik, eliminacje.etap FROM uczestnicy INNER JOIN eliminacje ON eliminacje.uczestnik_id = uczestnicy.uczestnik_id INNER JOIN wyniki ON eliminacje.wynik_id = wyniki.wynik_id WHERE eliminacje.rok_id = 2 AND wyniki.punkty IN (SELECT MAX(wyniki.punkty) FROM wyniki INNER JOIN eliminacje ON eliminacje.wynik_id = wyniki.wynik_id WHERE eliminacje.rok_id = 2 AND eliminacje.etap = 'finał') "
sql2_11b=" SELECT uczestnicy.uczestnik, wyniki.punkty as min_wynik, eliminacje.etap FROM uczestnicy INNER JOIN eliminacje ON eliminacje.uczestnik_id = uczestnicy.uczestnik_id INNER JOIN wyniki ON eliminacje.wynik_id = wyniki.wynik_id WHERE eliminacje.rok_id = 2 AND wyniki.punkty IN (SELECT MIN(wyniki.punkty) FROM wyniki INNER JOIN eliminacje ON eliminacje.wynik_id = wyniki.wynik_id WHERE eliminacje.rok_id = 2 AND eliminacje.etap = 'finał') "


#dla 2017
sql3_1=" SELECT wyniki.punkty, uczestnicy.uczestnik, piosenki.tytul, piosenki.jezyk, kraje.kraj FROM uczestnicy INNER JOIN eliminacje ON eliminacje.uczestnik_id=uczestnicy.uczestnik_id INNER JOIN piosenki ON piosenki.piosenka_id=uczestnicy.piosenka_id INNER JOIN kraje ON kraje.kraj_id=uczestnicy.kraj_id INNER JOIN wyniki ON wyniki.wynik_id=eliminacje.wynik_id WHERE uczestnicy.rok_id=1 AND eliminacje.etap = 'finał' ORDER BY wyniki.punkty DESC LIMIT 3"
sql3_2=" SELECT roczniki.rok, roczniki.miasto_host, roczniki.slogan FROM roczniki WHERE roczniki.rok_id = 1"
sql3_3=" SELECT daty.data_, roczniki.rok FROM daty INNER JOIN roczniki ON roczniki.rok_id=daty.rok_id WHERE daty.rok_id=1 ORDER By daty.daty_id"
sql3_4=" SELECT uczestnicy.uczestnik, kraje.kraj FROM uczestnicy LEFT JOIN kraje ON kraje.kraj_id=uczestnicy.kraj_id WHERE uczestnicy.rok_id=1 ORDER BY uczestnicy.uczestnik "
sql3_5=" SELECT roczniki.rok, uczestnicy.uczestnik, kraje.kraj FROM uczestnicy INNER JOIN roczniki ON roczniki.rok_id=uczestnicy.rok_id INNER JOIN kraje ON kraje.kraj_id=uczestnicy.kraj_id INNER JOIN eliminacje ON eliminacje.uczestnik_id=uczestnicy.uczestnik_id WHERE uczestnicy.rok_id = 1 AND eliminacje.etap = 'półfinał 1' "
sql3_6=" SELECT roczniki.rok, uczestnicy.uczestnik, kraje.kraj FROM uczestnicy INNER JOIN roczniki ON roczniki.rok_id=uczestnicy.rok_id INNER JOIN kraje ON kraje.kraj_id=uczestnicy.kraj_id INNER JOIN eliminacje ON eliminacje.uczestnik_id=uczestnicy.uczestnik_id WHERE uczestnicy.rok_id = 1 AND eliminacje.etap = 'półfinał 2' "
sql3_7=" SELECT roczniki.rok, uczestnicy.uczestnik, kraje.kraj FROM uczestnicy INNER JOIN roczniki ON roczniki.rok_id=uczestnicy.rok_id INNER JOIN kraje ON kraje.kraj_id=uczestnicy.kraj_id INNER JOIN eliminacje ON eliminacje.uczestnik_id=uczestnicy.uczestnik_id WHERE uczestnicy.rok_id = 1 AND eliminacje.etap = 'finał' "
sql3_8=" SELECT COUNT(eliminacje.etap) AS ilość_uczestników FROM eliminacje WHERE eliminacje.etap = 'półfinał 1' AND eliminacje.rok_id = 3 UNION ALL SELECT COUNT(eliminacje.etap) AS ilość_uczestników FROM eliminacje WHERE eliminacje.etap = 'półfinał 2' AND eliminacje.rok_id = 1 UNION ALL SELECT COUNT(eliminacje.etap) AS ilość_uczestników FROM eliminacje WHERE eliminacje.etap = 'finał' AND eliminacje.rok_id = 1"
sql3_9=" SELECT COUNT(uczestnicy.uczestnik) AS ilość_uczestników FROM uczestnicy WHERE rok_id=1 "
sql3_10=" SELECT uczestnicy.uczestnik FROM uczestnicy WHERE uczestnicy.rok_id = 1 "
sql3_11a=" SELECT uczestnicy.uczestnik, wyniki.punkty as max_wynik, eliminacje.etap FROM uczestnicy INNER JOIN eliminacje ON eliminacje.uczestnik_id = uczestnicy.uczestnik_id INNER JOIN wyniki ON eliminacje.wynik_id = wyniki.wynik_id WHERE eliminacje.rok_id = 1 AND wyniki.punkty IN (SELECT MAX(wyniki.punkty) FROM wyniki INNER JOIN eliminacje ON eliminacje.wynik_id = wyniki.wynik_id WHERE eliminacje.rok_id = 1 AND eliminacje.etap = 'finał') "
sql3_11b=" SELECT uczestnicy.uczestnik, wyniki.punkty as min_wynik, eliminacje.etap FROM uczestnicy INNER JOIN eliminacje ON eliminacje.uczestnik_id = uczestnicy.uczestnik_id INNER JOIN wyniki ON eliminacje.wynik_id = wyniki.wynik_id WHERE eliminacje.rok_id = 1 AND wyniki.punkty IN (SELECT MIN(wyniki.punkty) FROM wyniki INNER JOIN eliminacje ON eliminacje.wynik_id = wyniki.wynik_id WHERE eliminacje.rok_id = 1 AND eliminacje.etap = 'finał') "


try :	
	cursor.execute( sql )
	
	while True:

		#label: poczatek
		print("\n************************ EUROWIZJA ************************\n")
		print("1. Sprawdź kto wygrał w latach 2017-2019")
		print("2. Sprawdz ile uczestnikow bralo udzial w latach 2017-2019")
		print("3. Pokaz wszystkich uczestników wykonujących piosenki nie w języku angielskim")
		print("4. Sprawdź ile razy dane państwo brało udział w konkursie")
		print("5. Wybierz rok Eurowizji.")
		print("6. Wyjdź z programu")
		wybor=input("\nWybór opcji: ")
		
		if wybor=='1':
			print("\n******************** Zwycięzcy Eurowizji ********************\n")
			cursor.execute( sql1 )
			results=cursor.fetchall()
			print(tabulate(results,headers= ["Uczestnik", "Tytuł piosenki", "Kraj", "Rok"], tablefmt='psql'))

		elif wybor=='2':
			print("\n*********** Ilosc uczestnikow w podanych latach ***********\n")
			cursor.execute( sql2 )
			results=cursor.fetchall()
			print(tabulate(results,headers= ["Rok", "Ilość uczestników"], tablefmt='psql'))

		elif wybor=='3':
			print("\n*********** Nieanglojęzyczne utwory ***********\n")
			cursor.execute( sql3 )
			results=cursor.fetchall()
			print(tabulate(results,headers=["Uczestnik", "Tytuł piosenki", "Język"], tablefmt='psql'))

		elif wybor=='4':
			print("\n*********** Ilość wystąpień kraju w Eurowizji ***********\n")
			sql4a="SELECT kraje.kraj FROM kraje"
			cursor.execute( sql4a )
			results=cursor.fetchall()
			print(tabulate(results,headers=["Kraje"], tablefmt='psql'))

			kraj = input("\n Podaj kraj z listy: ")
			cursor.execute(" SELECT COUNT(uczestnicy.uczestnik) as liczba_wystąpień FROM uczestnicy INNER JOIN kraje ON uczestnicy.kraj_id = kraje.kraj_id WHERE kraje.kraj = %s GROUP BY uczestnicy.kraj_id ", [kraj] )
			results=cursor.fetchall()
			print(tabulate(results,headers=["Liczba wystąpień"], tablefmt='psql'))

		elif wybor=='5':
			rok= input("\n\nPodaj rok Eurowizji (2017 - 2019): ")
		
			if rok=='2019':
				print("\n********************** EUROWIZJA 2019 **********************\n")
				print("1. Pokaż pierwszą trójkę. ")
				print("2. Pokaż slogan i miasto goszczące. ")
				print("3. Kiedy odbył się półfinał 1, półfinał 2 oraz finał? ")
				print("4. Pokaż wszystkich uczestników w kolejności alfabetycznej. ")
				print("5. Kto był w półfinale 1? ")
				print("6. Kto był w półfinale 2? ")
				print("7. Kto był w finale? ")
				print("8. Ile było uczestników półfinału 1, półfinału 2, finału?")
				print("9. Ile było uczestników Eurowizji? ")
				print("10. Sprawdz, czy uczestnik dostał się do finału")
				print("11. Pokaz kto miał największą i najmniejszą liczbę punktów w finale")

				wybor1=input("\nWybór opcji: ")
				if wybor1=='1':	
					print("\n*********************************** PIERWSZA TROJKA ***********************************\n")
					cursor.execute( sql1_1)
					results=cursor.fetchall()
					print(tabulate(results,headers= ["Zdobyte punkty", "Uczestnik", "Tytuł piosenki", "Język", "Kraj"], tablefmt='psql'))

				elif wybor1=='2':
					print("\n*************************** SLOGAN I MIASTO GOSZCZĄCE ****************************\n")
					cursor.execute( sql1_2)
					results=cursor.fetchall()

					print(tabulate(results,headers= ["Rok", "Miasto goszczące", "Slogan"], tablefmt='psql'))

				elif wybor1=='3':
					print("\n******************* DATY *******************\n")
					cursor.execute( sql1_3)
					results=cursor.fetchall()
					print(tabulate(results,headers= ["Data", "Rok", "Kraj"], tablefmt='psql'))
		
				elif wybor1=='4':
					print("\n**************************************** UCZESTNICY EUROWIZJI *****************************************\n")
					cursor.execute( sql1_4 )
					results=cursor.fetchall()
					print(tabulate(results,headers= ["Uczestnik", "Kraj"], tablefmt='psql'))

				elif wybor1=='5':
					print("\n******************************* PÓŁFINAL NR.1 ******************************\n")
					cursor.execute( sql1_5 )
					results=cursor.fetchall()
					print(tabulate(results,headers= ["Rok", "Uczestnik", "Kraj"], tablefmt='psql'))

				elif wybor1=='6':
					print("\n******************************* PÓŁFINAL NR.2 *******************************\n")
					cursor.execute( sql1_6 )
					results=cursor.fetchall()
					print(tabulate(results,headers= ["Rok", "Uczestnik", "Kraj"], tablefmt='psql'))

				elif wybor1=='7':
					print("\n******************************** FINAŁ **********************************\n")
					cursor.execute( sql1_7 )
					results=cursor.fetchall()
					print(tabulate(results,headers= ["Rok", "Uczestnik", "Kraj"], tablefmt='psql'))

				elif wybor1=='8':
					print("\n************ ILOŚĆ UCZESTNIKÓW ELIMINACJI ************\n")
					cursor.execute( sql1_8 )
					results=cursor.fetchall()
					counter = 0
					print(tabulate(results,headers= ["Ilosc uczestnikow"], tablefmt='psql'))

				elif wybor1=='9':
					print("************ ILOŚĆ UCZESTNIKÓW EUROWIZJI ************")
					cursor.execute( sql1_9 )
					results=cursor.fetchall()
					for record in results :
						ilosc_uczestnikow=record[0]
						print("\nW Eurowizji wzielo udzial ",ilosc_uczestnikow, " uczestnikow.")

				elif wybor1=='10':
					print("\n************ CZY UCZESTNIK JEST W FINALE ************\n")
					cursor.execute( sql1_10 )
					results=cursor.fetchall()
					print(tabulate(results,headers= ["Uczestnicy"], tablefmt='psql'))

					uczestnik_input = input("\nPodaj uczestnika z listy: ")
					cursor.execute( " SELECT COUNT(uczestnicy.uczestnik) as punkt FROM uczestnicy INNER JOIN eliminacje ON eliminacje.uczestnik_id = uczestnicy.uczestnik_id WHERE uczestnicy.uczestnik = %s AND eliminacje.etap = 'finał' AND eliminacje.rok_id = 3", [uczestnik_input] )
					results=cursor.fetchall()
					for record in results :
						punkt=record[0]


					if punkt== 1:
						print("\nUczestnik dostał się do finału")	
					elif punkt== 0:
    						print("\nUczestnika nie ma w finale")
							
	
				elif wybor1=='11':
					print("\n************ NAJWIĘKSZY i NAJMNIEJSZY WYNIK ************\n")

					cursor.execute( sql1_11a )
					results=cursor.fetchall()
					print(tabulate(results,headers= ["Uczestnik", "Punkty Max", "Etap"], tablefmt='psql'))

					cursor.execute( sql1_11b )
					results=cursor.fetchall()
					print(tabulate(results,headers= ["Uczestnik", "Punkty Min", "Etap"], tablefmt='psql'))
					
			elif rok=='2018':
    				print("\n********************** EUROWIZJA 2018 **********************\n")
				print("1. Pokaż pierwszą trójkę")
				print("2. Pokaż slogan i miasto goszczące")
				print("3. Kiedy odbył się półfinał 1, półfinał 2 oraz finał?")
				print("4. Pokaż wszystkich uczestników w kolejności alfabetycznej. ")
				print("5. Kto był w półfinale 1? ")
				print("6. Kto był w półfinale 2? ")
				print("7. Kto był w finale? ")
				print("8. Ile było uczestników półfinału 1, półfinału 2, finału?")
				print("9. Ile było uczestników Eurowizji? ")
				print("10. Sprawdz, czy uczestnik dostał się do finału")
				print("11. Pokaz kto miał największą i najmniejszą liczbę punktów w finale")

				wybor1=input("\nWybór opcji: ")
				if wybor1=='1':	
					print("\n*********************************** PIERWSZA TROJKA ***********************************\n")
					cursor.execute( sql2_1)
					results=cursor.fetchall()
					print(tabulate(results,headers= ["Zdobyte punkty", "Uczestnik", "Tytuł piosenki", "Język", "Kraj"], tablefmt='psql'))

				elif wybor1=='2':
					print("\n*************************** SLOGAN I MIASTO GOSZCZĄCE ****************************\n")
					cursor.execute( sql2_2)
					results=cursor.fetchall()

					print(tabulate(results,headers= ["Rok", "Miasto goszczące", "Slogan"], tablefmt='psql'))

				elif wybor1=='3':
					print("\n******************* DATY *******************\n")
					cursor.execute( sql2_3)
					results=cursor.fetchall()
					print(tabulate(results,headers= ["Data", "Rok", "Kraj"], tablefmt='psql'))
		
				elif wybor1=='4':
					print("\n**************************************** UCZESTNICY EUROWIZJI *****************************************\n")
					cursor.execute( sql2_4 )
					results=cursor.fetchall()
					print(tabulate(results,headers= ["Uczestnik", "Kraj"], tablefmt='psql'))

				elif wybor1=='5':
					print("\n******************************* PÓŁFINAL NR.1 ******************************\n")
					cursor.execute( sql2_5 )
					results=cursor.fetchall()
					print(tabulate(results,headers= ["Rok", "Uczestnik", "Kraj"], tablefmt='psql'))

				elif wybor1=='6':
					print("\n******************************* PÓŁFINAL NR.2 *******************************\n")
					cursor.execute( sql2_6 )
					results=cursor.fetchall()
					print(tabulate(results,headers= ["Rok", "Uczestnik", "Kraj"], tablefmt='psql'))

				elif wybor1=='7':
					print("\n******************************** FINAŁ **********************************\n")
					cursor.execute( sql2_7 )
					results=cursor.fetchall()
					print(tabulate(results,headers= ["Rok", "Uczestnik", "Kraj"], tablefmt='psql'))

				elif wybor1=='8':
					print("\n************ ILOŚĆ UCZESTNIKÓW ELIMINACJI ************\n")
					cursor.execute( sql2_8 )
					results=cursor.fetchall()
					counter = 0
					print(tabulate(results,headers= ["Ilosc uczestnikow"], tablefmt='psql'))

				elif wybor1=='9':
					print("************ ILOŚĆ UCZESTNIKÓW EUROWIZJI ************")
					cursor.execute( sql2_9 )
					results=cursor.fetchall()
					for record in results :
						ilosc_uczestnikow=record[0]
						print("\nW Eurowizji wzielo udzial ",ilosc_uczestnikow, " uczestnikow.")

				elif wybor1=='10':
					print("\n************ CZY UCZESTNIK JEST W FINALE ************\n")
					cursor.execute( sql2_10 )
					results=cursor.fetchall()
					print(tabulate(results,headers= ["Uczestnicy"], tablefmt='psql'))

					uczestnik_input = input("\nPodaj uczestnika z listy: ")
					cursor.execute( " SELECT COUNT(uczestnicy.uczestnik) as punkt FROM uczestnicy INNER JOIN eliminacje ON eliminacje.uczestnik_id = uczestnicy.uczestnik_id WHERE uczestnicy.uczestnik = %s AND eliminacje.etap = 'finał' AND eliminacje.rok_id = 2", [uczestnik_input] )
					results=cursor.fetchall()
					for record in results :
						punkt=record[0]

					if	punkt== 1:
    						print("\nUczestnik dostał się do finału")	
					elif punkt== 0:
    						print("\nUczestnika nie ma w finale")
							

				elif wybor1=='11':
					print("\n************ NAJWIĘKSZY i NAJMNIEJSZY WYNIK ************\n")

					cursor.execute( sql2_11a )
					results=cursor.fetchall()
					print(tabulate(results,headers= ["Uczestnik", "Punkty Max", "Etap"], tablefmt='psql'))

					cursor.execute( sql2_11b )
					results=cursor.fetchall()
					print(tabulate(results,headers= ["Uczestnik", "Punkty Min", "Etap"], tablefmt='psql'))
				
				
			elif rok=='2017':
				print("\n********************** EUROWIZJA 2017 **********************\n")
				print("1. Pokaż pierwszą trójkę. ")
				print("2. Pokaż slogan i miasto goszczące. ")
				print("3. Kiedy odbył się półfinał 1, półfinał 2 oraz finał? ")
				print("4. Pokaż wszystkich uczestników w kolejności alfabetycznej. ")
				print("5. Kto był w półfinale 1? ")
				print("6. Kto był w półfinale 2? ")
				print("7. Kto był w finale? ")
				print("8. Ile było uczestników półfinału 1, półfinału 2, finału?")
				print("9. Ile było uczestników Eurowizji? ")
				print("10. Sprawdz, czy uczestnik dostał się do finału")
				print("11. Pokaz kto miał największą i najmniejszą liczbę punktów w finale")

				wybor1=input("\nWybór opcji: ")
				if wybor1=='1':	
					print("\n*********************************** PIERWSZA TROJKA ***********************************\n")
					cursor.execute( sql3_1)
					results=cursor.fetchall()
					print(tabulate(results,headers= ["Zdobyte punkty", "Uczestnik", "Tytuł piosenki", "Język", "Kraj"], tablefmt='psql'))

				elif wybor1=='2':
					print("\n*************************** SLOGAN I MIASTO GOSZCZĄCE ****************************\n")
					cursor.execute( sql3_2)
					results=cursor.fetchall()

					print(tabulate(results,headers= ["Rok", "Miasto goszczące", "Slogan"], tablefmt='psql'))

				elif wybor1=='3':
					print("\n******************* DATY *******************\n")
					cursor.execute( sql3_3)
					results=cursor.fetchall()
					print(tabulate(results,headers= ["Data", "Rok", "Kraj"], tablefmt='psql'))
		
				elif wybor1=='4':
					print("\n**************************************** UCZESTNICY EUROWIZJI *****************************************\n")
					cursor.execute( sql3_4 )
					results=cursor.fetchall()
					print(tabulate(results,headers= ["Uczestnik", "Kraj"], tablefmt='psql'))

				elif wybor1=='5':
					print("\n******************************* PÓŁFINAL NR.1 ******************************\n")
					cursor.execute( sql3_5 )
					results=cursor.fetchall()
					print(tabulate(results,headers= ["Rok", "Uczestnik", "Kraj"], tablefmt='psql'))

				elif wybor1=='6':
					print("\n******************************* PÓŁFINAL NR.2 *******************************\n")
					cursor.execute( sql3_6 )
					results=cursor.fetchall()
					print(tabulate(results,headers= ["Rok", "Uczestnik", "Kraj"], tablefmt='psql'))

				elif wybor1=='7':
					print("\n******************************** FINAŁ **********************************\n")
					cursor.execute( sql3_7 )
					results=cursor.fetchall()
					print(tabulate(results,headers= ["Rok", "Uczestnik", "Kraj"], tablefmt='psql'))

				elif wybor1=='8':
					print("\n************ ILOŚĆ UCZESTNIKÓW ELIMINACJI ************\n")
					cursor.execute( sql3_8 )
					results=cursor.fetchall()
					counter = 0
					print(tabulate(results,headers= ["Ilosc uczestnikow"], tablefmt='psql'))

				elif wybor1=='9':
					print("************ ILOŚĆ UCZESTNIKÓW EUROWIZJI ************")
					cursor.execute( sql3_9 )
					results=cursor.fetchall()
					for record in results :
						ilosc_uczestnikow=record[0]
						print("\nW Eurowizji wzielo udzial ",ilosc_uczestnikow, " uczestnikow.")

				elif wybor1=='10':
					print("\n************ CZY UCZESTNIK JEST W FINALE ************\n")
					cursor.execute( sql3_10 )
					results=cursor.fetchall()
					print(tabulate(results,headers= ["Uczestnicy"], tablefmt='psql'))

					uczestnik_input = input("\nPodaj uczestnika z listy: ")
					cursor.execute( " SELECT COUNT(uczestnicy.uczestnik) as punkt FROM uczestnicy INNER JOIN eliminacje ON eliminacje.uczestnik_id = uczestnicy.uczestnik_id WHERE uczestnicy.uczestnik = %s AND eliminacje.etap = 'finał' AND eliminacje.rok_id = 1", [uczestnik_input] )
					results=cursor.fetchall()
					for record in results :
						punkt=record[0]

					if	punkt== 1:
    						print("\nUczestnik dostał się do finału")	
					elif punkt== 0:
    						print("\nUczestnika nie ma w finale")
							
				elif wybor1=='11':
					print("\n************ NAJWIĘKSZY i NAJMNIEJSZY WYNIK ************\n")

					cursor.execute( sql3_11a )
					results=cursor.fetchall()
					print(tabulate(results,headers= ["Uczestnik", "Punkty Max", "Etap"], tablefmt='psql'))

					cursor.execute( sql3_11b )
					results=cursor.fetchall()
					print(tabulate(results,headers= ["Uczestnik", "Punkty Min", "Etap"], tablefmt='psql'))	
