#!/usr/bin/env python
### Function Name: main.py
### Expected Input: None.
### Processing: Opens the fasta for the RQ7 and call a function(saveRQ7) 
### 			to save the genes' identities to the database.
###             For every organism in the list,runs multiple functions to obtain 
###				locus tags for matched proteins and save to the respective database tables.
### Output: None.Errors in log.            
### Author: Nyonyi,Richard
### Comments : 

from Bio import SeqIO
from Bio.Blast import NCBIXML
from saveRQ7 import saveRQ7 
from setblast import setblast
from getGInumber import getGInumber
from getLocusTag import getLocusTag
from getQCoverage import getQCoverage
from dbsave import dbsave
_list=[] #list for names of organisms 

# adding organisms to the list

_list.append('Thermotoga maritima')
_list.append('Thermotoga neapolitana')
_list.append('Thermotoga elfii')
#_list.append('Thermotoga hypogea')  # No data  available in the NCBI database
_list.append('Thermotoga lettingae')
_list.append('Thermotoga naphthophila')
_list.append('Thermotoga petrophila')
_list.append('Thermotoga subterranea')
_list.append('Thermotoga thermarum')




#file for storing errors and tracking the system:
_logFile = open("log.txt", "a")


_file="oldRQ7.fasta"     #Fasta file for the organism we want to find matches

handle = open(_file , "rU")				      #opening the fasta file
_records = list(SeqIO.parse(handle, "fasta")) #parsing the file to a list 
handle.close()

_totalGenes =len(_records) # counting total number of genes in the  file.


#saveRQ7(_records,_logFile )        #save the genes to the database.



for organism in range(len(_list)):				    	#for all organisms to compare with.
	
	_resultFile = open("tempResults.txt", "w")      	#file for storing temporary results before saving to database:
	
	
	for genes in range(_totalGenes):  #for all records in the fasta file
		
	
		setblast(_records[genes].seq,_list[organism])# Sending the sequence and organism to compare with.
		
		result_handle = open("my_blast.xml") #Fetching results from xml file
		
		blast_record = NCBIXML.read(result_handle)
		
		for alignment in blast_record.alignments: #Going through alignment read from the xml file
			
			#filtering by query coverage
			for hsp in alignment.hsps:
				_coverage = getQCoverage(hsp.query, len(_records[genes])) #get query coverage
				if _coverage > 30:   #if query coverage is greater than 30 then find the GI and locus.			
					
					_giNumber=getGInumber(alignment.hit_id)  #get the gi number
					
					_locusResult=getLocusTag(_giNumber)   #get the locus tag
					
					
					
				if _locusResult == "Error":    # checking if locus-tag was found
					_logFile.write("No locus for   " +str( _giNumber) + '\n');
					
				else:	
					
					_resultFile.write(str(_records[genes].id) +" "+ str(_giNumber) +" "+ str(_locusResult) + '\n');	 #writing the results to a temp file
		
	_resultFile.close()	
	print "saving"
	dbsave(_list[organism],_logFile)      #Saving results into the specified database table
	_logFile.write("Saved all genes corresponding  to " + _list[organism] + '\n');
_logFile.close()
