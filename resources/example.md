# Temat projektu
Projekt bazy eurowizji wykonany w ramach ćwiczeń projektowych z Baz Danych.

| Nazwisko i imię        | Wydział | Kierunek | Semestr | Grupa | Rok akademicki |
| :--------------------: | :-----: | :------: | :-----: | :---: | :------------: |
| Jop Karolina           | WIMiIP  | IS       |   4     | 3     | 2019/2020      |
| Kocurek Magdalena      | WIMiIP  | IS       |   4     | 3     | 2019/2020      |

## Projekt bazy danych
Tutaj ma znaleźć się opis projektu bazy danych. Na wstępie proszę zagnieździć obraz schematu w formie wektorowej, najlepiej plik SVG. Dodatkowo, w tej sekcji należy zawrzeć kilka przykładowych zapytań tworzących (lub w razie konieczności, modyfikujących) tabelę, tj. grupa DDL.

![eurowizja diagram](Eurowizja.svg)

Baza danych eurowizja pozwala na znalezienie informacji o uczestnikach konkursu: kto i kiedy brał udział, z jakiego kraju pochodzi, co zaśpiewał, czy był w półfinałach, ile punktów otrzymał w każdym etapie eliminacji, kto wygrał. Dodatkowo z bazy można się dowiedzieć: w jakim mieście odbywał sie konkurs, jaki slogan był w danym roku oraz dokładne daty kiedy odbywały się wszystkie eliminacje.
Prezentowanie działania bazy opiera się na informacjach z ostatnich trzech lat konkursu. 

Schemat bazy danych został zaprezentowany powyżej za pomocą diagramu ERD (utworzony na platformie draw.io). Baza składa się z siedmiu tabel (w każdej tabeli znajduje się klucz główny).


#### Relacje w bazie
Jednemu uczestnikowi konkursu przypisana jest konkretnie jedna piosenka co przedstawia relacja jeden do jeden pomiędzy uczestnikami a piosenkami.

Do jednego uczestnika przypisany jest konkretnie jeden kraj, ale z powodu, że konkurs odbywa się co roku to jeden kraj może być przypisany do wielu uczestników (zostało to zaprezentowane za pomocą relacji jeden do wielu pomiędzy tabelą kraje a uczestnicy).

Tabela roczniki zawiera informacje odnośnie roku, w którym odbywała się eurowizja, czyli jaki był slogan konkursu w danym roku, w jakim mieście odbywał się konkurs, kto zwyciężył i jaką piosenką.
Relacja jeden do wielu między tabelami roczniki a piosenki przedstawia, że dana piosenka może wygrać tylko w jednym roku, ale wiele piosenek może być wykonanych w konkretnym roku. 

W przypdaku relacji tabel roczniki - uczestnicy (relacja jeden do wielu) w jednym roku może wziąć udział wielu uczestników, ale tylko jeden uczestnik może wygrać w danym roku. 

Połączenie tabeli roczniki i daty relacją jeden do wielu obrazuję, że w danym roku może być kilka daty (data połfinału 1, półfinału 2 i finału), a jedna data może wystąpić w konkretnie jednym roku.

Relacja pomiędzy uczestnikami a wynikami jest relacją wiele do wielu dlatego odbywa się za pomocą tabeli pomocniczej eliminacje (ze względu na łatwiejszy sposób implementacji). Dzięki takiemu zabiegowi jednemu uczestnikowi mogą być przypisane dwa wyniki (ten uzyskany w półfinałach i ten, który uzyskał w finale). 
Z powodu, że tabela eliminacje jest tabelą pomocniczą to oprócz agregowania w niej informacji o uczestnikach i uzyskanych przez nich wynikach zawiera ona informację, w którym roku uczestnik uzyskał dany wynik, jaki to był etap eliminacji i dzień, w którym dana eliminacja się odbyła.

Można uzyskać informację czy dany uczestnik był w półfinale i czy zakwalifikował się dalej. Zatem relacja pomiędzy tabelą wyniki a eliminacje informuje, że jeden wynik, może być przypisany do kilku etapów eliminacji, tak samo relacja pomiędzy uczestnikami a eliminacjami, gdzie jeden uczestnik może wziąć udział w kilku etapach eliminacji.


## Implementacja zapytań SQL
Tutaj należy wylistować wszystkie funkcjonalności, wraz z odpowiednimi zapytaniami SQL. W tej sekcji należy zawrzeć wyłącznie zapytania z grupy DML oraz DQL.

## Aplikacja
Aplikacja została napisania w języku Python z użyciem biblioteki PyMySQL.

## Dodatkowe uwagi
W tej sekcji możecie zawrzeć informacje, których nie jesteście w stanie przypisać do pozostałych. Mogą to być również jakieś komentarze, wolne uwagi, itp.
