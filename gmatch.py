#*************************************************************
#This module reads the RQ7 fasta file and using a for loop 
# blast search each gene and print out the NAME and e-value 
# of the matching genes in the given genomes.
#*************************************************************

from Bio.Blast import NCBIWWW
from Bio import SeqIO
from Bio import Entrez
import time

        
 #Please tell Entrez who you are.
Entrez.email = "bgomics@gmail.com"

 #Setting the threshold of results we want to appear	
E_VALUE_THRESH = 10**(-6)


#Timer to measure process time
t0 = time.clock()
t1 = time.clock()
print t0
print t1

#file for storing temporary results:
_resultFile = open("_tempResults.txt", "w")


count=0
#For every gene in the RQ7
for seq_record in SeqIO.parse("RQ7.fasta", "fasta"):
        print '--------------------------------------------------------------------------------------'
        count += 1
 #Print the RQ7-gene identifier
        print "THE GENE: ",seq_record.id, 'MATCHES WITH '
        print '--------------------------------------------------------------------------------------'
       



 #blast search the gene protein  limiting to  and T naepolitana
        result_handle = NCBIWWW.qblast("blastp", "nr", seq_record.seq, entrez_query="Thermotoga neapolitana" ,expect = E_VALUE_THRESH)
        
 #Saving the result xml
        save_file = open("my_blast.xml", "w")
        save_file.write(result_handle.read())
        save_file.close()
        result_handle.close()
	
 #Fetching results from xml file
        result_handle = open("my_blast.xml")
        from Bio.Blast import NCBIXML
        blast_record = NCBIXML.read(result_handle)
	
#comment
	
	
 #For loop to fetch all matches that comply with the threshold	
        for alignment in blast_record.alignments:
                for hsp in alignment.hsps:
                        if hsp.expect < E_VALUE_THRESH:
                                
                                print 'Name:', alignment.title
                                #print 'original sequence',hsp.query
                                #print 'matching sequence',hsp.sbjct
                                #print 'With e value of', hsp.expect
                                #print 'lenght', hsp.align_length
                                print ' ' 
                                giParse = alignment.hit_id[3:12]
                                if giParse.find('|') == -1:
                                        print giParse
                                        
                                else:
                                        giParse = giParse[:giParse.find('|')]
                                        print giParse

                                dbfetch = Entrez.efetch(db = "protein" , id = giParse, rettype = "gb", retstyle = "xml")
                                dbread = dbfetch.read()
                                
                                if dbread.find('locus_tag') == -1:

                                        locustag = "no locus tag"
                                else:
                                        
                                        locustag = dbread[dbread.find("locus_tag")+11:dbread.find("locus_tag")+19]
                                print locustag
                               
                                _resultFile.write(str(count)+" "+locustag+'\n');

                        
print time.clock() - t0, "seconds  time t0"
print time.time() - t1, "seconds time t1"
_resultFile.close()                    
