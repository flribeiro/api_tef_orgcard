import json
import requests

dados = {
    'id': 1,
    'nome': 'Fabrício L. Ribeiro',
    'data_nasc': '1983-03-02',
    'familia': ['Pâmela','Alice'],
}

url = 'http://127.0.0.1:5000/'
headers = {'Content-Type': 'application/json'}

with open('request_tef.json', 'r') as fj:
    response = requests.post(url, data=fj.read(), headers=headers)

print(response.text)