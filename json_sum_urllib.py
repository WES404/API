import urllib.error, urllib.parse, urllib.request
import json

# USE  http://py4e-data.dr-chuck.net/comments_995584.json

url = input("Coloque o URL --> ")
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_995584.json"

js = urllib.request.urlopen(url) # Abre o link
data = js.read().decode() # Ler e decodifica do UTF-8
info = json.loads(data) # Carrega o dato como JSON

counts = list()

comment = info['comments']
for i in range(len(comment)):
    counts.append(int(comment[i]['count']))

print(sum(counts))
