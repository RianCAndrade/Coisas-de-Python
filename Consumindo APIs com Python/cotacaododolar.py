import requests
import json


#cotaçao do dolar
cota = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cota = cota.json()
cotadodolar = cota['USDBRL']['bid']
#print(cota)
print(cotadodolar)


