#!/usr/bin/env python

def saveRQ7(list):
import mysql.connector
from mysql.connector import errorcode
try:
 cnx = mysql.connector.connect(user='', password='',host='',database='')

except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong your username or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exists")
  else:
    print(err)
else:
  
	cursor = cnx.cursor()
	_sql = ("INSERT INTO RQ7"
	"(name) " 
	"VALUES (%s)")
 
	for c in range (len(list)):
	   
 	   _name=list[c].id
       _data = (_name)
       cursor.execute(_sql, _data)
    
	cnx.commit()
	cursor.close()
	f.close()
	cnx.close()
