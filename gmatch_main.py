




from Bio import SeqIO

_list=[]								    #list for names of organisms to find matches
_list.append('Thermotoga Neapolitana')
_list.append('Thermotoga Maritima')


_file="RQ7.fasta"    					      #Fasta file for the organism we want to find matches

handle = open(_file , "rU")				      #opening the fasta file
_records = list(SeqIO.parse(handle, "fasta")) #parsing the file to a list 
handle.close()



#file for storing temporary results before saving to database:
_resultFile = open("_tempResults.txt", "w")


for c in range(len(_records)):				 #for all records in the fasta file
	for r in range(len(_list)):				 #for all organisms to compare with.

		print _records[c].id, _records[c].seq,_list[r] 	
