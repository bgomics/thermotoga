#!/usr/bin/env python

import mysql.connector
from mysql.connector import errorcode
try:
    my_database = raw_input ("Which database to save the data?")
    cnx = mysql.connector.connect(user='root', password='BGOmics',host='localhost',database='xu_test_2')
    cursor = cnx.cursor()
    print "OK"
 		
    cursor.close()
    cnx.close()
			
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print "Something is wrong with your username or password \n"
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print "Database does not exists \n"
else:
    cnx.close()
			
