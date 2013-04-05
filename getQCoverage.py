def getQCoverage(query,length):
	query_with_hyphens = query
	query_without_hyphens =  query_with_hyphens.replace("-","")
	                            
    align_length =len(query_without_hyphens) * 1.0
                                                            
    coverage =float(align_length/length)
    queryCover= coverage * 100
    return queryCover