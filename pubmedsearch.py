#!/usr/bin/env python
# Copied from ehazlett with modifications
# numpy and biopython are required -- pip install numpy biopython
 
from Bio import Entrez
from Bio import Medline
 
MAX_COUNT = 10000
TERM = '2012 [DP] Clinical Trial, Phase II[PT]'


def pubmedsearch (TERM, MAX_COUNT = 10000):
    print('Getting {0} publications containing {1}...'.format(MAX_COUNT, TERM))
    Entrez.email = 'A.N.Other@example.com'
    h = Entrez.esearch(db='pubmed', retmax=MAX_COUNT, term=TERM)
    result = Entrez.read(h)
    print('Total number of publications containing {0}: {1}'.format(TERM, result['Count']))
    ids = result['IdList']
    h = Entrez.efetch(db='pubmed', id=ids, rettype='medline', retmode='text') 
    records = Medline.parse(h)
    return records

def pmhits (TERM):
    Entrez.email = 'A.N.Other@example.com'
    h = Entrez.esearch(db='pubmed', retmax=1000000, term=TERM)
    result = Entrez.read(h)
    return result['Count']



'''
PMIDs = []
for record in records:
    uid = record.get('PMID', '?')
    PMIDs.append(uid)
print('PMIDs: {0}'.format(', '.join(PMIDs)))
'''