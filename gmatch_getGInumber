### Function Name: getGInumber
### Expected Input: An alignment's hit_id member variable as defined in the
###                  biopython package
### Processing: Slices the hit_id to retrieve the GI number
### Output: The GI Number of the given alignment
### Author: Newmister, Jacob
### Comments: the hitID is assumed to be in the form x|(GINUMBERHERE)|ETC.
###           edits may be necissary if this system ever changes.


def getGInumber(hitID):
    giParse = hitID[3:12]
    if giParse.find('|') == -1:
        giParse = "error"
        return giParse

    else:
        giParse = giParse[:giParse.find('|')]
        return giParse
