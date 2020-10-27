import urllib.error, urllib.parse, urllib.request
import json
import ssl

api_key = False

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    endereco = input("Coloque o Endereço: ")
    if len(endereco) < 1: break

    parms = dict()
    parms['address'] = endereco
    if api_key is not False: 
        parms['key'] = api_key

    url = serviceurl + urllib.parse.urlencode(parms)

    abrir = urllib.request.urlopen(url, context = ctx)
    ler = abrir.read().decode()
    print("Retrieving ", len(ler), "characters")
    
    carrega = json.loads(ler)


    id = carrega['results'][0]['place_id']
    print('place_id', id)