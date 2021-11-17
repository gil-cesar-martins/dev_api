from flask import Flask, jsonify, request
import json

app= Flask(__name__)

devs = [
    {
    'id':'0',
    'nome':'gil',
    'habilidades':['Python','MySQL']
    },
    
    {
    'id':'1',
    'nome':'Edward',
    'habilidades':['C++','Unreal']
    }
]

# Devolve um desenvolvedor pelo ID, também pode alterar e/ou deletar um desenvolvedor
@app.route('/dev/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = devs[id]
        except IndexError:
            message = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status':'erro','mensagem': message}
        except Exception:
            message = 'Erro desconhecido. Procure o administrador da API.'
            response = {'status':'erro', 'mensagem': message}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        devs[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        devs.pop(id)
        return jsonify({'status':'sucesso','mensagem':'Registro excluído'})

# Lista todos os desenvolvedores e permite registrar um novo desenvolvedor
@app.route('/dev/', methods=['POST','GET'])
def lista_devs():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(devs)
        dados['id'] = posicao
        devs.append(dados)
        return jsonify(devs[posicao])
    elif request.method == 'GET':
        return jsonify(devs)


if __name__ == '__main__':
    app.run(debug=True)
