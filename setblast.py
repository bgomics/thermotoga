### Function Name: setblast
### Expected Input: sequence for blast search  and NCBI reference sequence number for entrez filtering.
### Processing: BLast search is performed using qblast form biopython.
### Output: None.
### Author: Nyonyi,Richard.

def setblast(_sequence,refSeq):
    from Bio.Blast import NCBIWWW
    from Bio import SeqIO

    #Setting the threshold of results we want to appear
    E_VALUE_THRESH = 10**(-6)
    
   
    #blast search the gene protein limiting to the given value in a list
    result_handle = NCBIWWW.qblast("tblastn", "refseq_genomic", _sequence, entrez_query= refSeq ,expect = E_VALUE_THRESH)

    #Saving the result xml
    save_file = open("my_blast.xml", "w")
    save_file.write(result_handle.read())
    save_file.close()
    result_handle.close()   