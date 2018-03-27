import json
import requests

dados = {
    'id': 1,
    'nome': 'Fabrício L. Ribeiro',
    'data_nasc': '1983-03-02',
    'familia': ['Pâmela','Alice'],
}

url = 'http://127.0.0.1:5000/testjson'
headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=json.dumps(dados), headers=headers)

print(response.content)