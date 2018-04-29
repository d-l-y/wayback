import requests
import sys
import re

'''
Usage: python wayback.py <domain> [optional year]
example: python wayback.py example.com
only look back to 2015: python wayback.py example.com 2015
'''

domain = sys.argv[1]

query = 'http://web.archive.org/cdx/search/cdx?url='+domain+'/robots.txt&collapse=digest&filter=statuscode:200&output=json'

if len(sys.argv) > 2:
    query += '&from='+str(sys.argv[2])
    
r = requests.get(query)
results = [result for result in r.json()[1:]]
paths = []

for result in results:
    r2 = requests.get('http://web.archive.org/web/'+str(result[1])+'/'+str(result[2]))
    for path in re.findall(r'Disallow: (.*?)\n',r2.content):
        paths.append(path.strip())
        
for path in set(paths):
    print path
    
