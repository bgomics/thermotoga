### Function Name: getLocusTag
### Expected Input: giNumber of a given Alignment
### Processing: Takes the giNumber given to the function and runs a search
###             of the Entrez database. Returns all info and then slices the
###             locus tag out.
### Output: Locus Tag, if present. Else returns error message
### Requirements: importing Entrez from Bio. Email defined in main body.
###               (ex. Entrez.email = "youremail@goes.here")
### Author: Newmister, Jacob
### Comments: This file may need to be changed if the system for locus_tag
###           storage is ever changed

def getLocusTag(giNumber):
	from Bio import Entrez
	Entrez.email = "bgomics@gmail.com"
	dbfetch = Entrez.efetch(db = "protein", id = giNumber, rettype = "gb", retstyle = "xml")
	dbread = dbfetch.read()

	if dbread.find('locus_tag') == -1:
		locusTag = "Error"

	else:
		locusTag = dbread[dbread.find("locus_tag")+11:]
		locusTag = locusTag[:locusTag.find("\"")]

	print dbread
	return locusTag
