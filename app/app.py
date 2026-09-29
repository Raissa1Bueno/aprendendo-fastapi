
from fastapi import FastAPI
from app.schemas import Message, ObterUsuario, AdicionarUsuario
app = FastAPI(title="Minha aplicação")
banco_de_dados = []

@app.get('/teste', response_model=Message)
def testando():
    return {'message': 'Olá mundo!'}


@app.post('/usuario', response_model=Message)
def adicionar(user: AdicionarUsuario):
    novo_usuario = {
        'usuario': user.usuario,
        'email': user.email,
        'password': user.password,
        'idade': user.idade,
        'codigo': len(banco_de_dados)  + 1
    }
    banco_de_dados.append(novo_usuario)
    return {'message': 'usuario cadastrado'}

@app.get('/usuario', response_model=list[ObterUsuario])
def obter_usuarios():
    return banco_de_dados

@app.put('/usuario/{codigo}', response_model=Message)
def atualizar(codigo: int, user: AdicionarUsuario):
    for usuario in banco_de_dados:
        if usuario['codigo'] == codigo:
            usuario['usuario'] = user.usuario
            usuario['email'] = user.email
            usuario['idade'] = user.idade
            usuario['password'] = user.password
            return {'message': 'usuario atualizado'}

@app.delete('/usuario/{codigo}', response_model=Message)
def deletar(codigo: int):
    for usuario in banco_de_dados:
        if usuario['codigo'] == codigo:
            banco_de_dados.remove(usuario)

            return {'message': 'usuario.deletado'}  

'''Executando aplicativo 
uvicorn app.app:app --reload
'''
