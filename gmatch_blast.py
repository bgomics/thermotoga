#*************************************************************
#This module reads the RQ7 fasta file and using a for loop 
# blast search each gene and print out the NAME and e-value 
# of the matching genes in the given genomes.  
#*************************************************************

from Bio.Blast import NCBIWWW
from Bio import SeqIO


 #Setting the threshold of results we want to appear	
E_VALUE_THRESH = 10**(-6)



#input from main...._records[c].id, _records[c].seq,_list[r] 	......................


        print '--------------------------------------------------------------------------------------'
        
 #Print the RQ7-gene identifier
        print "THE GENE: ",_RECORDS[C].ID, 'MATCHES WITH '   #
        print '--------------------------------------------------------------------------------------'
       



 #blast search the gene protein limiting to the given value in a list
        result_handle = NCBIWWW.qblast("blastp", "nr", seq_record.seq, entrez_query=_LIST ,expect = E_VALUE_THRESH)
        
 #Saving the result xml
        save_file = open("my_blast.xml", "w")
        save_file.write(result_handle.read())
        save_file.close()
        result_handle.close()
	

