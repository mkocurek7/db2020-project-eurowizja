import os
import pymysql
from tabulate import tabulate

connection= pymysql.connect("localhost", "eurowizja", "eurowizja", "eurowizja")
cursor=connection.cursor()

#funkcjonalnosci
sql=" USE eurowizja"
