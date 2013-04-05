#
#
#
#
#
from Bio import SeqIO
from Bio.Blast import NCBIXML
 
_list=[] #list for names of organisms 

# adding organisms to the list
_list.append('Thermotoga Neapolitana')
_list.append('Thermotoga Maritima')
_list.append('Thermotoga Elfii')
_list.append('Thermotoga Hypogea')
_list.append('Thermotoga Lettingae')
_list.append('Thermotoga Naphthophila')
_list.append('Thermotoga Petrophila')
_list.append('Thermotoga Subterranea')
_list.append('Thermotoga Thermarum')





_file="RQ7.fasta"     #Fasta file for the organism we want to find matches

handle = open(_file , "rU")				      #opening the fasta file
_records = list(SeqIO.parse(handle, "fasta")) #parsing the file to a list 
handle.close()

_totalGenes =len(_records) # counting total number of genes in the  file.

saveRQ7(_records)        #save the genes to the database.


#file for storing errors and tracking the system:
_logFile = open("log.txt", "w")


for organism in range(len(_list)):				    	#for all organisms to compare with.
	
	_resultFile = open("tempResults.txt", "w")      	#file for storing temporary results before saving to database:
	_geneCounter = 0	
	_geneLimit=50
	for genes in range(_totalGenes):				  	#for all records in the fasta file
		setblast(_records[genes].seq,_list[organism]) 	# Sending the sequence and organism to compare with.
		
		#Fetching results from xml file
    	result_handle = open("my_blast.xml")
        blast_record = NCBIXML.read(result_handle)
		
		
		for alignment in blast_record.alignments: #Going through alignment read from the xml file
			
			#filtering by query coverage
			for hsp in alignment.hsps:
				_coverage = getQcoverage(hsp.query, len(_records[_geneCounter])) #get query coverage
				if _coverage > 30:   #if query coverage is greater than 30 then find the GI and locus.
			
					_giNumber=getGInumber(alignment.hit_id)  #get the gi number
			
					_locusResult=getLocusTag(_giNumber)   #get the locus tag
			
					if _locusResult == "Error":    # checking if locus-tag was found
						 _logFile.write("No locus for   " + _giNumber+'\n');
			 
					else:
						 _locus=_locusResult
			 		
			 
			 _resultFile.write(_geneCounter+" "+_giNumber+" "+_locus+'\n');	 writing the results to a temp file	
			_geneCounter = _geneCounter + 1

		if _geneCounter == _totalGenes:
			dbsave(_list[organism])      #Saving results into the specified database table
			_logFile.write("Saved all genes corresponding  to " +_list[organism]+'\n');
			_resultFile.close	
		
		elif _geneCounter ==_geneLimit
		    dbsave(_list[organism])      #Saving results into the specified database table
			_logFile.write("Saved 50 genes corresponding  to " +_list[organism]+'\n');
			_geneLimit = _geneLimit + 50
			_resultFile.close
			_resultFile = open("tempResults.txt", "w") 
		
	_resultFile.close	
_logFile.close