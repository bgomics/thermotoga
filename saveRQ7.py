### Function Name: saveRQ7
### Expected Input: A list that contains the sequences of RQ7a and a log file for reporting errors.
### Processing: Going through each item in the list and save them to a table called RQ7 in the database named Genomes.
### Output: None.All errors are found in the log file.
### Author: Nyonyi,Richard.
### Comments : Make sure  the login credentials for the database - genomes are set to reflect your database.(line 15)

#!/usr/bin/env python
def saveRQ7(list,_logFile):	
	
	import mysql.connector
	from mysql.connector import errorcode

	try:
 		cnx = mysql.connector.connect(user='root', password='BGOmics',host='localhost',database='xu_test_2')
		cursor = cnx.cursor()
		_sql = ("INSERT INTO RQ7 (row,identity) "  
		"VALUES (%s,%s)")
 
		for c in range (len(list)):
			_name=list[c].id	#getting the Identity attribute in the list
			_data=(c+1,_name)
			cursor.execute(_sql, _data)
		cnx.commit()
		cursor.close()	
		cnx.close()
		_logFile.write(" Data RQ7 was successfully saved \n");
			 
			
	except mysql.connector.Error as err:
  		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
  			_logFile.write( "Something is wrong your username or password \n");
  		elif err.errno == errorcode.ER_BAD_DB_ERROR:
  			_logFile.write("Database does not exists \n");
  		else:
  			_logFile.write(str(err));
	else:
  
		cnx.close()
		
