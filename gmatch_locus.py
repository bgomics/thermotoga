 #Fetching results from xml file
        result_handle = open("my_blast.xml")
        from Bio.Blast import NCBIXML
        blast_record = NCBIXML.read(result_handle)
	

	
	
 #For loop to fetch all matches that comply with the threshold	
        for alignment in blast_record.alignments:
                for hsp in alignment.hsps:
                        if hsp.expect < E_VALUE_THRESH:
                                
                                print 'Name:', alignment.title
                               
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


_resultFile.close()                    
