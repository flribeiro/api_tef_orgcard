from flask import Flask, url_for, request
from mail import sendmail
import json

app = Flask(__name__)

token = 'asdfGZXCVb@!'

@app.route('/', methods=['GET', 'POST'])
def responde():
    if request.method == 'POST':
        recebido = request.get_json()
        
        if recebido['token'] == token:
            texto = 'O cliente {} terá os dados de ativação do TEF enviados para os seguintes e-mails:\n'.format(recebido['nome_cliente'])

            for item in recebido['destinatarios']:
                texto += item + '\n'

            # return 'json recebido.\n{}'.format(recebido)
            sendmail(recebido['nome_cliente'], recebido['destinatarios'], recebido['lojas'])
            return texto
        else:
            return 'Token inválido.'
    else:
        return 'Não era um POST.'


with app.test_request_context():
    print(url_for('responde'))