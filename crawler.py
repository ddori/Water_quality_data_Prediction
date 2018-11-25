# import pandas as pd
# from bs4 import BeautifulSoup
# import requests

import urllib.request
import urllib.parse
import csv



f = open('output.csv', 'w', encoding='utf-8', newline='')



#&sdate=2012-01-01&edate=2012-01-01&sta_cde=213&id=WemoData

#sdat3
#edate
#sta_cde
#id
decode_key = urllib.parse.unquote('P1c4m2lUvkf3mlKVA9W%2BGq6Di3Gs1HiMcyx9HukfeFP8Q7hVJ%2FNJ0u1EFiB7ql728phCz8%2Fc3R6hmPjPbEMeqA%3D%3D')  # decode 해줍니다.
url = 'http://openapi.meis.go.kr/rest/datalist'
queryParams = '?' + urllib.parse.urlencode({ urllib.parse.quote_plus('ServiceKey') :
                                               decode_key,
                                             urllib.parse.quote_plus('sdata') :'2012-01-01',
                                             urllib.parse.quote_plus('edate') :'2012-01-01',
                                             urllib.parse.quote_plus('sta_cde') :'213',
                                             urllib.parse.quote_plus('id') : 'WemoData' })

request = urllib.request.Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urllib.request.urlopen(request).read().decode('utf8')
print (response_body)

# wr = csv.writer(f)
# wr.writerow([1, "김정수", False])
# wr.writerow([2, "박상미", True])
# f.close()