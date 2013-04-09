### Function Name: dbsave
### Expected Input: organism name/table name , log file handler.
### Processing: Opens the temporary file that contains results. 
###             Save every data to the table as described in the organism name.
### Output: None.Errors in log.
### Requirements: importing mysql connector.            
### Author: Nyonyi,Richard
### Comments : Make sure  the login credentials for the database-Genomes are set to reflect your database.(line 19)           


#!/usr/bin/env python
def dbsave(organism,_logFile):
	import mysql.connector
	from mysql.connector import errorcode
	try:
		cnx = mysql.connector.connect(user='', password='',host='',database='')
 		cursor = cnx.cursor()
 		
 		name=organism.split()   #splitting organism name to obtain the second word.i.e from(thermotoga xxxxxxx) to only xxxxxxxx
 		tableName=name[1]
 		
 		_sql = ("INSERT INTO " + tableName + "(RQ7id,gi,locus) " 
 		"VALUES (%s,%s,%s)")
 	
 		_rq7id =[]
 		_locus=[]  
 		_gi=[]            
 		f = open('tempResults.txt','r')
 		
 		for line in f:  		 #Going through all data in the temporary file
 			if line.strip():      #skiping/ignoring any empty lines available
 				t = line.split()    # data in the file have the format(rq7id giNumber locusTag)
				_rq7id= t[0]
				_gi= t[1]
				_locus= t[2]
				_data = (_rq7id,_gi,_locus)
				cursor.execute(_sql, _data)
				
	
		cnx.commit()
		cursor.close()
		f.close()
		cnx.close()
			
	except mysql.connector.Error as err:
  		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
  			_logFile.write( "Something is wrong with your username or password \n");
  		elif err.errno == errorcode.ER_BAD_DB_ERROR:
  			_logFile.write("Database does not exists \n");
  		else:
  			_logFile.write(str(err)+ '\n');
	else:
		cnx.close()
			
