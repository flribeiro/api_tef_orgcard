from flask import Flask, url_for, request

app = Flask(__name__)

@app.route('/')
def responde():
    return 'Resposta do servidor FLR-PC!'

@app.route('/api/<usuario>')
def responde_api(usuario):
    return 'A API irá responder por aqui, Sr. ' + usuario

@app.route('/testjson', methods=['GET', 'POST'])
def testjson():
    if request.method == 'POST':
        recebido = request.get_json()
        print(recebido)
        return 'json recebido. {}'.format(recebido['nome'])
    else:
        return 'Não era um POST.'


with app.test_request_context():
    print(url_for('responde'))
    print(url_for('responde_api', usuario='Fabrício'))
    print(url_for('testjson'))