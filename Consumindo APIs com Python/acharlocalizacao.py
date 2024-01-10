import requests
import json


#Achar o localizacao atraves do CEP
cep = requests.get("https://cep.awesomeapi.com.br/json/99999999") #coloque o CEP
cep = cep.json()
print(cep)
