#!/usr/bin/env python

def dbsave(tableName):
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
	_sql = ("INSERT INTO "+ tableName
	"(RQ7id,GInum,Locus) " 
	"VALUES (%s,%s,%s)")
 
 
	_rq7id =[]
	_locus=[]  
	_gi=[]            
	f = open('_tempResults.txt','r')
 
	for line in f:
	   t = line.split()
    
 	   _rq7id= str(t[0])
 	   _gi= str(t[1])
 	   _locus= str(t[2])
 	   
       _data = (_rq7id,_gi,_locus)
       cursor.execute(_sql, _data)
    
	cnx.commit()
	cursor.close()
	f.close()
	cnx.close()
