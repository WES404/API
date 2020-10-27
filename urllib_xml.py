import xml.etree.ElementTree as ET 
import urllib.error, urllib.parse, urllib.request
import ssl

# Entra no site, busca todas tags 'count' e soma o conteúdo

url = input("URL: ")
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_995583.xml'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urllib.request.urlopen(url, context = ctx).read()

tree = ET.fromstring(html)
counts = list()

for count in tree.iter('count'): #procura por tags 'count' e a cada tag guarda o valor em uma lista
    counts.append(int(count.text))  
print(sum(counts))

