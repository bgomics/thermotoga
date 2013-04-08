### Function Name: getQCoverage
### Expected Input: query sequence  and length of the corresponding RQ7 sequence.
### Processing: Calculates the query coverage by dividing the length of the two sequences
### Output: Number : query coverage.
### Author: Nyonyi,Richard.

def getQCoverage(query,RQ7length):
	query_with_hyphens = query
	query_without_hyphens =  query_with_hyphens.replace("-","")
	                            
	align_length =len(query_without_hyphens) * 1.0
                                                            
	coverage =float(align_length/RQ7length)
	queryCover= coverage * 100
	return queryCover