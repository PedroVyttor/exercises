#(Modularizaçõa Via Pacotes) importar pacotes com duncoes - instalei requests
import requests

pag = requests.request('GET',  'http://infosacc.com.br')
print(pag.text)