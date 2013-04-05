#




from Bio import SeqIO
from Bio.Blast import NCBIXML
 
_list=[]								    #list for names of organisms to find matches
_list.append('Thermotoga Neapolitana')
_list.append('Thermotoga Maritima')
_list.append('Thermotoga Elfii')
_list.append('Thermotoga Hypogea')
_list.append('Thermotoga Lettingae')
_list.append('Thermotoga Naphthophila')
_list.append('Thermotoga Petrophila')
_list.append('Thermotoga Subterranea')
_list.append('Thermotoga Thermarum')





_file="RQ7.fasta"    					      #Fasta file for the organism we want to find matches

handle = open(_file , "rU")				      #opening the fasta file
_records = list(SeqIO.parse(handle, "fasta")) #parsing the file to a list 
handle.close()
_totalGenes =len(_records)
saveRQ7(_records)


#file for storing errors and tracking the system:
_logFile = open("log.txt", "w")


for organism in range(len(_list)):				    	#for all organisms to compare with.
	
	_resultFile = open("tempResults.txt", "w")      	#file for storing temporary results before saving to database:
	_geneCounter = 0	
	
	for genes in range(_totalGenes):				  	#for all records in the fasta file
		setblast(_records[genes].seq,_list[organism]) 	# Sending the sequence and organism to compare with.
		#Fetching results from xml file
    	result_handle = open("my_blast.xml")
       
        blast_record = NCBIXML.read(result_handle)
		
		
		for alignment in blast_record.alignments:
			
			#filtering by query coverage
			for hsp in alignment.hsps:
				_coverage = getQcoverage(hsp.query, len(_records[_geneCounter]))
				if _coverage > 30:
			
					_giNumber=getGInumber(alignment.hit_id)
			
					_locusResult=getLocusTag(_giNumber)
			
					if _locusResult == "Error":
						 _logFile.write("No locus for   " + _giNumber+'\n');
			 
					else:
						 _locus=_locusResult
			 		
			 
			 _resultFile.write(_geneCounter+" "+_giNumber+" "+_locus+'\n');		
		

		if _geneCounter == _totalGenes:
			dbsave(_list[organism])      #Saving results into the specified database table
			_logFile.write("Saved all genes corresponding  to " +_list[organism]+'\n');
		_geneCounter = _geneCounter + 1
		
	_resultFile.close	
_logFile.close